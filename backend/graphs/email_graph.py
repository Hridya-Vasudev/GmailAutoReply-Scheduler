from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END

from backend.agents.email_classifier import EmailClassifierAgent
from backend.core.email_categories import EmailCategory
from backend.core.reply_policy import should_reply
from backend.agents.reply_agent import ReplyAgent
from backend.services.mock_service import fetch_emails, send_email


class EmailAgentState(dict):
    pass

classifier = EmailClassifierAgent()
reply_agent = ReplyAgent()





def decide_node(state: EmailAgentState):
    # This node writes reply_needed into state
    return {
        "reply_needed": state["reply_needed"],
        "category": state["category"],
    }
def classify_node(state: EmailAgentState):
    category = classifier.classify(
        subject=state["subject"],
        body=state["body"],
    )
    return {
        "category": category,
        "reply_needed": should_reply(category),
    }
def reply_node(state: EmailAgentState):
    reply_text = reply_agent.generate_reply(
        category=state["category"],
        subject=state["subject"],
        body=state["body"],
    )

    send_email(
        to_email=state["sender"],
        subject=state["subject"],
        body=reply_text,
    )

    return {}


def route_after_decide(state) -> str:
    if state["reply_needed"]:
        return "reply"
    return "end"


def build_email_graph():
    graph = StateGraph(EmailAgentState)

    graph.add_node("classify", classify_node)
    #graph.add_node("decide", decide_writer)
    graph.add_node("reply", reply_node)

    graph.set_entry_point("classify")
    graph.add_edge("classify", "decide")

    graph.add_conditional_edges(
    "decide",
    route_after_decide,
    {
        "reply": "reply",
        "end": END,   # ← this must match the router output
    },
)

    graph.add_edge("reply", END)
    return graph.compile()


def run_email_flow():
    emails = fetch_emails()
    compiled_graph = build_email_graph()

    for mail in emails:
        state = {
            "sender": mail.sender,
            "subject": mail.subject,
            "body": mail.body,
            "category": None,
            "reply_needed": None
        }

        result = compiled_graph.invoke(state)  # call invoke on compiled graph
        print("Processed:", result)
        print("\nFrom:", mail.sender)
        print("Subject:", mail.subject)
        print("Category:", result.get("category"))
        print("Reply needed:", result.get("reply_needed"))
        print("Result:", result)


if __name__ == "__main__":
    run_email_flow()
    print("Email flow completed successfully")
