# backend/tests/test_email_flow.py

from agents.email_classifier import EmailClassifierAgent
from agents.reply_agent import ReplyAgent
from core.email_categories import EmailCategory

# Mock emails for testing
emails = [
    {
        "sender": "client1@example.com",
        "subject": "Inquiry about course pricing",
        "body": "Can you please provide details about the course fees?"
    },
    {
        "sender": "client2@example.com",
        "subject": "Technical issue with login",
        "body": "I am unable to log in to my account."
    },
    {
        "sender": "client3@example.com",
        "subject": "Partnership proposal",
        "body": "We would like to discuss a collaboration opportunity."
    }
]

# Initialize agents
classifier = EmailClassifierAgent()
reply_agent = ReplyAgent()

# Run classification and reply generation for each email
for mail in emails:
    category = classifier.classify(
        subject=mail["subject"],
        body=mail["body"]
    )
    
    reply_text = reply_agent.generate_reply(
        category=category,
        subject=mail["subject"],
        body=mail["body"]
    )
    
    print("\n==============================")
    print("From:", mail["sender"])
    print("Subject:", mail["subject"])
    print("Category:", category.value)
    print("Reply Generated:\n", reply_text)
    print("==============================\n")
