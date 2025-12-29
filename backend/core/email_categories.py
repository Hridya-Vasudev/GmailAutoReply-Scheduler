from enum import Enum

class EmailCategory(str, Enum):
    JOB_APPLICATION = "job_application"
    CLIENT_INQUIRY = "client_inquiry"
    SALES_LEAD = "sales_lead"
    PARTNERSHIP = "partnership"
    SUPPORT_REQUEST = "support_request"
    PAYMENT_BILLING = "payment_billing"
    INTERNAL_COMMUNICATION = "internal_communication"
    FOLLOW_UP = "follow_up"
    SPAM_MARKETING = "spam_marketing"
    UNKNOWN = "unknown"
    IMPORTANT_EMAIL = "important"
    BUSINESS_INQUIRY = "business_inquiry"
    CLIENT_SUPPORT = "client_support"
    INTERVIEW_INVITE = "interview_invite"
    URGENT_REQUEST = "urgent_request"
    SYSTEM = "system"
