# backend/run_bot_test.py

from dotenv import load_dotenv
load_dotenv()

from graphs.email_graph import build_email_graph
from services.mock_gmail_reader import fetch_emails
from services.mock_gmail_sender import send_email

def main():
    emails = fetch_emails()
    email_graph = build_email_graph()

    for mail in emails:
        state = {
            "sender": mail.sender,
            "subject": mail.subject,
            "body": mail.body,
            "category": None,
            "reply_needed": None
        }

        # Run the graph
        email_graph.run(state)

        # Print results
        print("\nFrom:", mail.sender)
        print("Subject:", mail.subject)
        if state["category"]:
            print("Category:", state["category"].value)
        else:
            print("Category: Not classified")
        print("Reply needed:", state.get("reply_needed", False))

if __name__ == "__main__":
    main()
