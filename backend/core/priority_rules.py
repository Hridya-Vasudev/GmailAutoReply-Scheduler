from core.email_categories import EmailCategory


PRIORITY_MAP = {
    EmailCategory.JOB_APPLICATION: 5,
    EmailCategory.CLIENT_INQUIRY: 5,
    EmailCategory.PAYMENT_BILLING: 5,

    EmailCategory.SALES_LEAD: 4,
    EmailCategory.PARTNERSHIP: 4,

    EmailCategory.SUPPORT_REQUEST: 3,
    EmailCategory.FOLLOW_UP: 3,

    EmailCategory.INTERNAL_COMMUNICATION: 2,

    EmailCategory.SPAM_MARKETING: 1,
    EmailCategory.UNKNOWN: 1,
}


def get_priority(category: EmailCategory) -> int:
    return PRIORITY_MAP.get(category, 1)
