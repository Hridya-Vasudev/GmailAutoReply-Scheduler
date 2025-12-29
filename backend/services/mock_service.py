# backend/services/mock_services.py

from collections import namedtuple

# Create a simple Email structure
MockEmail = namedtuple("MockEmail", ["sender", "subject", "body"])

def fetch_emails():
    """
    Return a list of mocked emails for testing the flow.
    """
    return [
        MockEmail(sender="user1@example.com", subject="Pricing query", body="Can you tell me the pricing?"),
        MockEmail(sender="user2@example.com", subject="Job application", body="I would like to apply for the position."),
        MockEmail(sender="user3@example.com", subject="Support needed", body="My account is not working.")
    ]

def send_email(to_email: str, subject: str, body: str):
    """
    Instead of sending emails, just print them for testing.
    """
    print(f"\n--- Sending email ---")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")
    print("--- End ---\n")
