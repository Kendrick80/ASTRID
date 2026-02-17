# ASTRID — Health Remedies Chatbot

ASTRID is a health-remedies chatbot built with Django and Dialogflow. It provides safe, general-purpose guidance and home remedies for minor ailments (colds, headaches and migraines, burns and scalds, minor cuts, digestive upsets, etc.). The project bundles a Dialogflow agent for natural-language understanding and a Django backend that serves the web UI, webhook endpoints, user accounts, and basic security controls.

**Warning:** ASTRID provides informational, non-diagnostic advice only. It is not a replacement for professional medical care. For emergencies or serious conditions, seek immediate medical attention.

**Highlights**
- **Purpose:** Offer curated, general remedies and self-care steps for minor illnesses.
- **NLP:** Dialogflow agent for intent & entity extraction and conversation flow.
- **Backend:** Django (views, templates, user accounts, webhook endpoints).
- **Security:** Secrets are excluded from the repository; environment variables are used for credentials. Sensitive files must never be committed.

**Features**
- Multi-turn conversational flows for common complaints (cold, headache, migraine, burns/scalds, minor wounds, stomach upset, etc.).
- Quick remedy suggestions and safety guidance (when to see a doctor).
- Django-powered admin and simple user authentication.
- Dialogflow webhook integration for dynamic responses and context handling.

Getting started

1. Clone the repo and create a Python virtual environment:

   ```bash
   git clone https://github.com/Kendrick80/ASTRID.git
   cd "FINAL YEAR PROJECT/src" || cd src
   python -m venv .venv
   .venv\Scripts\activate    # Windows
   source .venv/bin/activate  # macOS / Linux
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables (example):

   - `DJANGO_SECRET_KEY` — Django secret key
   - `DATABASE_URL` — optional, if using external DB
   - `DIALOGFLOW_PROJECT_ID` and service account credentials path for Dialogflow integration

   Do NOT commit these values. Keep credentials out of source control.

4. Run Django migrations and start the dev server:

   ```bash
   python Darri/manage.py migrate
   python Darri/manage.py runserver
   ```

Dialogflow setup (summary)
- Create a Dialogflow agent and build intents for the common ailments.
- Configure the webhook URL to point to your Django webhook endpoint (e.g. `https://<your-host>/webhook/`).
- Use a service account for server-to-server authentication; keep the JSON key off-repo and referenced via an environment variable.

Security & best practices
- Never commit service account JSON, private keys, or other secrets.
- Use environment variables and a secure secrets manager in production.
- Use HTTPS for all webhook endpoints.
- Sanitize and validate user input before processing.

Contributing
- Create issues or PRs for fixes and new remedies.
- Keep medical content evidence-based and include sources when adding new guidance.

License & contact
- This repository is provided as-is for educational/demo use. Replace or extend the content and licenses as required for your deployment.

If you want, I can also add a short `docs/` page with the Dialogflow intent list and webhook contract.
# ASTRID