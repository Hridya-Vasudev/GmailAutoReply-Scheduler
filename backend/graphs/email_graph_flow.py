import os
import imaplib
import smtplib
import ssl
from email.message import EmailMessage
from email import message_from_bytes
from dotenv import load_dotenv
import re

from langgraph.graph import StateGraph, END
from backend.agents.email_classifier import EmailClassifierAgent
from backend.agents.reply_agent import ReplyAgent
from backend.core.reply_policy import should_reply
from backend.core.email_categories import EmailCategory

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))

classifier = EmailClassifierAgent()
reply_agent = ReplyAgent()

REPLIED_FILE = "backend/replied_mails.txt"

def extract_email(text):
    match = re.search(r"<(.+?)>", text)
    if match:
        return match.group(1)
    return text.split()[-1]

def fetch_emails_from_gmail():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    status, data = mail.search(None, "ALL")
    if status != "OK":
        return []

    email_ids = data[0].split()
    emails = []

    for e_id in email_ids[-5:]:
        status, msg_data = mail.fetch(e_id, "(RFC822 UID)")
        if status != "OK":
            continue

        raw_email = msg_data[0][1]
        uid = msg_data[0][0].decode().split()[-1]

        msg = message_from_bytes(raw_email)

        subject = (msg["subject"] or "").replace("\n", " ").replace("\r", " ")
        sender = msg["from"] or ""
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    try:
                        body = part.get_payload(decode=True).decode()
                    except:
                        body = ""
                    break
        else:
            try:
                body = msg.get_payload(decode=True).decode()
            except:
                body = ""

        emails.append({
            "uid": uid,
            "sender": sender,
            "subject": subject,
            "body": body
        })

    mail.logout()
    return emails

def classify_node(state):
    category = classifier.classify(
        subject=state["subject"],
        body=state["body"]
    )
    reply_needed = should_reply(category)
    return {
        "uid": state["uid"],
        "sender": state["sender"],
        "subject": state["subject"],
        "body": state["body"],
        "category": category,
        "reply_needed": reply_needed
    }

def reply_node(state):
    reply_text = reply_agent.generate_reply(
        category=state["category"],
        subject=state["subject"],
        body=state["body"]
    )

    email_msg = EmailMessage()
    email_msg["From"] = EMAIL_ADDRESS
    email_msg["To"] = extract_email(state["sender"])
    email_msg["Subject"] = "Re: " + state["subject"].strip()
    email_msg.set_content(reply_text)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email_msg)

    print("Reply sent to:", state["subject"])
    return state

def route_after_classify(state):
    return "reply" if state.get("reply_needed") else "end"

def build_email_graph():
    graph = StateGraph(dict)
    graph.add_node("classify", classify_node)
    graph.add_node("reply", reply_node)
    graph.set_entry_point("classify")
    graph.add_conditional_edges(
        "classify",
        route_after_classify,
        {"reply": "reply", "end": END}
    )
    graph.add_edge("reply", END)
    return graph.compile()

def run_email_flow():
    emails = fetch_emails_from_gmail()
    compiled_graph = build_email_graph()

    if os.path.exists(REPLIED_FILE):
        with open(REPLIED_FILE) as f:
            replied = set(f.read().splitlines())
    else:
        replied = set()

    for mail_data in emails:
        if mail_data["uid"] in replied:
            print("Already replied → skipping:", mail_data["subject"])
            continue

        state = {
            "uid": mail_data["uid"],
            "sender": mail_data["sender"],
            "subject": mail_data["subject"],
            "body": mail_data["body"],
            "category": None,
            "reply_needed": None
        }

        result = compiled_graph.invoke(state)

        if result.get("reply_needed"):
            with open(REPLIED_FILE, "a") as f:
                f.write(mail_data["uid"] + "\n")

        print("\nProcessed Email →")
        print("From:", result.get("sender"))
        print("Subject:", result.get("subject"))
        print("Category:", result.get("category"))
        print("Reply needed:", result.get("reply_needed"))

    print("\nDone")
