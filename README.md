# FunnelAI Tracker

**FunnelAI Tracker** is a backend-only analytics and AI recommendation tool built with Python and FastAPI. It tracks user behavior across website funnels (pageviews, clicks, scrolls), analyzes conversion drop-offs, and uses GPT to generate actionable optimization suggestions.

> Designed as a developer-first tool — no frontend, no SaaS wrapper. Just clean APIs, SQL storage, and AI insights.

---

## Features

- Lightweight JavaScript snippet to track events (pageviews, clicks, scrolls)
- FastAPI backend to collect and store user behavior
- SQLite-based session and event storage (Postgres-ready)
- API to return funnel step drop-off and conversion metrics
- GPT-4 integration to generate optimization recommendations

---

## Project Structure

funnel_ai_tracker/
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── db.py # SQLite DB setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── routers/
│ │ ├── events.py # Track events
│ │ ├── funnel.py # Funnel stats
│ │ └── gpt.py # GPT suggestions
│ ├── services/
│ │ ├── funnel_analysis.py # Funnel logic
│ │ └── gpt_prompts.py # Prompt templates + API call
├── static/
│ └── tracker.js # JavaScript to embed on websites
├── requirements.txt # Dependencies
├── .env # API keys (OpenAI)
└── README.md

yaml
Copy
Edit

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/funnel_ai_tracker.git
cd funnel_ai_tracker
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add your OpenAI API Key
Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxx
4. Run the FastAPI app
bash
Copy
Edit
uvicorn app.main:app --reload
5. Embed the tracker on a test HTML page
html
Copy
Edit
<script src="https://yourdomain.com/static/tracker.js"></script>

Example API Usage
Track an event
bash
Copy
Edit
POST /event
{
  "event_type": "page_view",
  "url": "/landing",
  "session_id": "abc123"
}
Get funnel stats
bash
Copy
Edit
GET /funnel
Returns:

json
Copy
Edit
{
  "step_1": 1200,
  "step_2": 450,
  "step_3": 90,
  "dropoff_rate": {
    "step_1_to_2": 62.5,
    "step_2_to_3": 80
  }
}
Get GPT recommendations
bash
Copy
Edit
POST /recommendations
{
  "funnel_data": {
    ...
  }
}
Returns:

json
Copy
Edit
{
  "recommendations": [
    "Shorten the signup form to reduce Step 2 drop-off.",
    "Improve the CTA text on the landing page.",
    "Add social proof near the checkout step."
  ]
}

Tech Stack
Backend: FastAPI

Database: SQLite (SQLAlchemy ORM)

AI: OpenAI GPT-4 API

Frontend Tracking: Vanilla JavaScript

Auth/UI: None — backend tool only

Author
Liam Kircher
29 y/o technical founder on a machine learning journey.

License
MIT — free to use and modify for any purpose.

yaml
Copy
Edit

---

Let me know if you want me to:
- Customize the embed script link
- Add setup instructions for Heroku/Render
- Auto-generate a `requirements.txt` now based on the structure

Want to do the `main.py` scaffolding next?