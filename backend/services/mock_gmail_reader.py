# backend/services/mock_gmail_reader.py

from collections import namedtuple

# Simple structure to mimic an email object
Email = namedtuple("Email", ["sender", "subject", "body"])

def fetch_emails():
    # Return a list of mock emails
    return [
        Email(
            sender="client1@example.com",
            subject="Request for information",
            body="Could you provide details about your courses?"
        ),
        Email(
            sender="client2@example.com",
            subject="Complaint about delay",
            body="I am unhappy with the delay in responses."
        ),
    ]
