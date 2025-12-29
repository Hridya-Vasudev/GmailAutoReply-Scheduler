# backend/tests/test_email_agents.py

from agents.email_classifier import EmailClassifierAgent
from agents.reply_agent import ReplyAgent
from core.email_categories import EmailCategory

# Mock email for testing
test_email = {
    "sender": "client@example.com",
    "subject": "Inquiry about course pricing",
    "body": "Can you please provide details about the course fees?"
}

# Initialize agents
classifier = EmailClassifierAgent()
reply_agent = ReplyAgent()

# 1. Test classification
category = classifier.classify(
    subject=test_email["subject"],
    body=test_email["body"]
)

print("Test Email Classification:")
print("Subject:", test_email["subject"])
print("Body:", test_email["body"])
print("Category:", category.value)

# 2. Test reply generation
reply_text = reply_agent.generate_reply(
    category=category,
    subject=test_email["subject"],
    body=test_email["body"]
)

print("\nGenerated Reply:")
print(reply_text)
