from backend.core.reply_templates import REPLY_TEMPLATES
from backend.core.email_categories import EmailCategory
from langchain_openai import ChatOpenAI  # or any LLM you plan to plug in

class ReplyAgent:
    """
    Generate email replies based on predefined templates.
    Falls back to LLM-generated replies if no template exists.
    """

    def __init__(self):
        # Initialize LLM to prevent attribute errors
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3
        )

    def generate_reply(
        self,
        category: EmailCategory,
        subject: str,
        body: str
    ) -> str:

        # 1. Check for template reply
        template = REPLY_TEMPLATES.get(category)
        if template:
            return template.strip()

        # 2. Fallback to LLM generated reply
        prompt = f"""
Reply to this email professionally.

Category: {category.value}

Subject: {subject}

Body:
{body}

Reply:
"""
        response = self.llm.invoke(prompt)

        # Some LLM responses return `.content`, others return raw string
        if hasattr(response, "content"):
            return response.content.strip()

        return str(response).strip()
