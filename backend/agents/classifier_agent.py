from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from backend.core.email_categories import EmailCategory
from config import settings

class EmailClassifierAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            api_key=settings.OPENAI_API_KEY,
        )

    def classify(self, subject: str, body: str) -> EmailCategory:
        system_prompt = (
            "You are an email classification assistant.\n"
            "Classify the email into ONE of these categories:\n"
            f"{[c.value for c in EmailCategory]}\n\n"
            "Return ONLY the category name."
        )

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Subject: {subject}\n\nBody:\n{body}")
        ]

        response = self.llm.invoke(messages).content.strip()

        return EmailCategory(response)