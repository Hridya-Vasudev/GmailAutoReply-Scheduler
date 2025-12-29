from backend.core.email_categories import EmailCategory

REPLY_ALLOWED = {
    EmailCategory.JOB_APPLICATION,
    EmailCategory.BUSINESS_INQUIRY,
    EmailCategory.CLIENT_INQUIRY,
    EmailCategory.PARTNERSHIP,
    EmailCategory.FOLLOW_UP,
    EmailCategory.SUPPORT_REQUEST,
    EmailCategory.IMPORTANT_EMAIL,  # now works
    EmailCategory.INTERVIEW_INVITE,
    EmailCategory.URGENT_REQUEST
}

def should_reply(category: EmailCategory) -> bool:
    return category in REPLY_ALLOWED
