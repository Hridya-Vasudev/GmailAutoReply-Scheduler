# backend/services/mock_gmail_sender.py

def send_email(to_email, subject, body):
    print(f"\n--- Mock Sending Email ---")
    print("To:", to_email)
    print("Subject:", subject)
    print("Body:", body)
    print("--- End ---\n")
