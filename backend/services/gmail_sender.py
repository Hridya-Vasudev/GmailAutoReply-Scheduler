import smtplib
from email.message import EmailMessage
import os

def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = os.getenv("GMAIL_ADDRESS")
    msg["To"] = to_email
    msg["Subject"] = "Re: " + subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.getenv("GMAIL_ADDRESS"),
            os.getenv("GMAIL_APP_PASSWORD")
        )
        server.send_message(msg)
