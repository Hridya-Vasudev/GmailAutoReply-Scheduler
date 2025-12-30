Email Automation & Classification System

A backend service that reads emails via IMAP, classifies them into defined categories, and sends replies based on templates. Reply history is stored to avoid duplicate responses.

Tech stack

Python 3.11

Django 5.2.9

IMAP (Gmail)

SMTP (Gmail)

LangGraph (for workflow orchestration)

schedule (for automation loop)

dotenv (for config)

Folder structure
email-new/
│
├── backend/ # Email processing + scheduler + graph flow
├── backendApi/ # Django project (API endpoints)
├── frontend/ # React frontend (to be built)
├── env/ # Virtual environment
└── replied_mails.txt # Stores replied email UIDs

How it works

Fetch last 5 emails from inbox

Classify based on subject + body

Check reply policy

If allowed, generate reply using template or LLM fallback

Send reply via SMTP

Store UID to prevent future duplicate replies

Reply rules

Replies are sent only once per email

Internal/system emails are skipped

Reply status is tracked using UID history

Email sign-off fixed as:
Regards,
Hridya

Django API endpoints available for frontend integration

Run locally
Activate env:
env\Scripts\activate

Start scheduler:
python -m backend.graphs.email_scheduler

Start Django API:
cd backendApi
python manage.py runserver

Git setup
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin
git push -u origin main

Future improvements

Frontend UI for email monitoring

Manual reply trigger from dashboard

Auth & filters for email list

API Endpoints

| Method | Endpoint | Purpose |
| GET | /api/emails/ | Fetch recent emails with reply status |
| GET | /api/replied-uids/ | List replied email UIDs |
| POST | /api/classify/ | Classify a single email |
| POST | /api/reply/ | Send reply manually |