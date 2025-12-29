from imap_tools import MailBox, AND
import smtplib
import os

def fetch_emails():
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    mails = []
    with MailBox(os.getenv("IMAP_SERVER")).login(email, password, "INBOX") as mailbox:
        for msg in mailbox.fetch(AND(seen=False)):
            mails.append({
                "sender": msg.from_,
                "subject": msg.subject,
                "body": msg.text
            })
    return mails


def send_email(to_email: str, subject: str, body: str):
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
        server.login(email, password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email, to_email, message)
