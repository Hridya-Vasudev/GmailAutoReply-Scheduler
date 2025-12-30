from django.urls import path
from . import views

urlpatterns = [
    path("emails/", views.get_emails, name="get_emails"),
    path("emails/classify/", views.classify_email, name="classify_email"),
    path("emails/reply/", views.send_reply, name="send_reply"),
    path("emails/replied/", views.get_replied_uids, name="get_replied"),
]
