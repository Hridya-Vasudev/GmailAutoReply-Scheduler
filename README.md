# Email Reply Automation

A backend system that fetches emails from Gmail using IMAP, classifies them into predefined categories, and generates replies using templates or an LLM fallback.  
It tracks replied mails and avoids duplicate responses in future scheduler runs.

---

## Features

- Fetch last 5 emails from Gmail inbox
- Classify emails (Interview, Intern, General, Important, etc.)
- Auto-reply using stored templates
- LLM fallback if template is missing
- Prevent repeated replies using UID tracking
- Secure credential handling using env
- Built using LangGraph state flow
- Works with a React + Django backend structure (your existing project setup)

---

## Project Structure

# Email Reply Automation

A backend system that fetches emails from Gmail using IMAP, classifies them into predefined categories, and generates replies using templates or an LLM fallback.  
It tracks replied mails and avoids duplicate responses in future scheduler runs.

---

## Features

- Fetch last 5 emails from Gmail inbox
- Classify emails (Interview, Intern, General, Important, etc.)
- Auto-reply using stored templates
- LLM fallback if template is missing
- Prevent repeated replies using UID tracking
- Secure credential handling using env
- Built using LangGraph state flow
- Works with a React + Django backend structure (your existing project setup)

---

## Project Structure

backend/
├ agents/
│ ├ email_classifier.py
│ ├ reply_agent.py
├ core/
│ ├ email_categories.py
│ ├ reply_policy.py
│ ├ reply_templates.py
├ replied_mails.txt
email_graph_flow.py
.gitignore
.env
README.md

---

## Setup & Installation

1. Clone the repository
2. Create a `.env` file in root and add:


---

## Setup & Installation

1. Clone the repository
2. Create a `.env` file in root and add:

EMAIL_ADDRESS=yourmail@gmail.com

EMAIL_PASSWORD=yourpassword
IMAP_SERVER=imap.gmail.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=465
3. Install dependencies:
pip install python-dotenv imaplib smtplib langgraph
4. Run the email flow:
python email_graph_flow.py

---

## Security

- `.env` is ignored using `.gitignore`
- `replied_mails.txt` is not tracked to avoid exposing internal logs

---

## Reply Tracking Logic

- Each processed email UID is stored in `replied_mails.txt`
- Scheduler checks UID before replying again
- If UID exists → reply is skipped automatically

---

## Notes

- No emojis used in replies (professional policy enforced)
- Templates are prioritized over LLM generation
- LLM is used only when no matching template is found

---

## Author

Regards,  
**Hridya**

