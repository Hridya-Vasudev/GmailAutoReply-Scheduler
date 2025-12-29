import re
from backend.core.email_categories import EmailCategory

class EmailClassifierAgent:
    def classify(self, subject: str, body: str) -> EmailCategory:
        text = f"{subject}\n{body}".lower()

        # SYSTEM emails first
        if any(re.search(p, text) for p in [
            r"terms", r"polic", r"storage", r"security alert",
            r"account access", r"unusual activity", r"verify it’s you",
            r"google account", r"no-reply@accounts.google.com"
        ]):
            return EmailCategory.SYSTEM

        # IMPORTANT / INTERNAL emails
        if any(re.search(p, text) for p in [
            r"important:", r"for your action", r"kindly check",
            r"file to look", r"document attached", r"please review",
            r"team", r"office", r"hr", r"meeting", r"schedule",
            r"interview"
        ]):
            return EmailCategory.IMPORTANT_EMAIL

        # OTP / Codes
        if any(re.search(p, text) for p in [
            r"otp", r"verification code", r"login code", r"\b\d{4,8}\b"
        ]):
            return EmailCategory.OTP_EMAIL

        # SUPPORT
        if any(re.search(p, text) for p in [
            r"help", r"support", r"not working", r"issue", r"error",
            r"can’t access", r"cannot access", r"fix"
        ]):
            return EmailCategory.SUPPORT_REQUEST

        # JOB
        if any(re.search(p, text) for p in [
            r"application for", r"resume", r"cv", r"apply", r"position"
        ]):
            return EmailCategory.JOB_APPLICATION

        # SALES
        if any(re.search(p, text) for p in [
            r"course enquiry", r"pricing for", r"quote for", r"demo request",
            r"contact me for", r"interested in training", r"reach me at",
            r"partnership with"
        ]):
            return EmailCategory.SALES_LEAD

        return EmailCategory.UNKNOWN
