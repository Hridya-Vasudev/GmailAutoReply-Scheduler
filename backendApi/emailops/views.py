from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import sys
import os

# Add project root to path so backend module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from backend.graphs.email_graph_flow import fetch_emails_from_gmail, REPLIED_FILE

from backend.agents.email_classifier import EmailClassifierAgent
from backend.agents.reply_agent import ReplyAgent
from backend.core.email_categories import EmailCategory
from backend.core.reply_policy import should_reply

classifier = EmailClassifierAgent()
reply_agent = ReplyAgent()

def get_replied_uids_set():
    """Return replied UIDs as a set (internal use, not an API view)"""
    uids = set()
    if os.path.exists(REPLIED_FILE):
        with open(REPLIED_FILE, "r") as f:
            uids = set(f.read().splitlines())
    return uids

def get_replied_uids(request):
    """API endpoint to return replied UIDs"""
    uids = get_replied_uids_set()
    return JsonResponse({"replied_uids": list(uids)})

def get_emails(request):
    """Fetch emails and mark reply status"""
    emails = fetch_emails_from_gmail()
    replied_uids = get_replied_uids_set()

    for mail in emails:
        mail["reply_status"] = "replied" if mail["uid"] in replied_uids else "not_replied"

    return JsonResponse({"emails": emails})

@csrf_exempt
def classify_email(request):
    """Classify email and show if reply is needed"""
    if request.method == "POST":
        data = json.loads(request.body)
        replied_uids = get_replied_uids_set()

        category = classifier.classify(subject=data["subject"], body=data["body"])
        reply_needed = should_reply(category)

        return JsonResponse({
            "uid": data["uid"],
            "category": category.value,
            "reply_needed": reply_needed,
            "reply_status": "replied" if data["uid"] in replied_uids else "not_replied"
        })

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def send_reply(request):
    """Send reply only if not already replied"""
    if request.method == "POST":
        data = json.loads(request.body)
        replied_uids = get_replied_uids_set()

        if data["uid"] in replied_uids:
            return JsonResponse({"message": "Already replied. Skipping new reply."})

        reply_text = reply_agent.generate_reply(
            category=EmailCategory(data["category"]),
            subject=data["subject"],
            body=data["body"]
        )

        # Mark as replied
        with open(REPLIED_FILE, "a") as f:
            f.write(data["uid"] + "\n")

        return JsonResponse({"message": "Reply sent and marked as replied."})

    return JsonResponse({"error": "Invalid request"}, status=400)
