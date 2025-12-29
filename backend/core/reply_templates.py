from backend.core.email_categories import EmailCategory


REPLY_TEMPLATES = {
    EmailCategory.JOB_APPLICATION: """
Hello,

Thank you for your interest and for taking the time to reach out.
We have received your application and will review it carefully.
If your profile matches our current requirements, we will get back to you.

Best regards,
Recruitment Team
""",

    EmailCategory.CLIENT_INQUIRY: """
Hello,

Thank you for contacting us.
We have received your query and our team will review it shortly.
We will get back to you with the required details as soon as possible.

Best regards,
Support Team
""",

    EmailCategory.SALES_LEAD: """
Hello,

Thank you for your interest in our services.
Our team will review your message and reach out with relevant information shortly.

Best regards,
Business Team
""",

    EmailCategory.PARTNERSHIP: """
Hello,

Thank you for reaching out regarding a potential partnership.
We appreciate your interest and will review your proposal internally.
We will get back to you if there is a suitable opportunity to collaborate.

Best regards,
Partnerships Team
""",

    EmailCategory.SUPPORT_REQUEST: """
Hello,

Thank you for contacting support.
We have received your request and our team is looking into it.
We will update you shortly.

Best regards,
Support Team
""",

    EmailCategory.PAYMENT_BILLING: """
Hello,

Thank you for reaching out regarding billing or payment.
Our accounts team will review this and respond shortly.

Best regards,
Accounts Team
""",

    EmailCategory.FOLLOW_UP: """
Hello,

Thank you for your follow-up.
We have noted your message and will respond with an update soon.

Best regards,
Team
""",
}
