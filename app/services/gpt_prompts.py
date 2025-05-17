import os
import openai
from dotenv import load_dotenv

load_dotenv()
print("OPENAI KEY:", os.getenv("OPENAI_API_KEY"))  # <-- TEMP for debug
openai.api_key = os.getenv("OPENAI_API_KEY")
import os



def generate_recommendations(funnel_data: dict) -> list:
    prompt = f"""
You are a CRO (conversion optimization) expert. Analyze this funnel performance and suggest 3 very specific optimizations.

Funnel data:
{funnel_data}

Return your answer as a **JSON list** like:
[
  "Improve the headline on the landing page",
  "Reduce form fields on the signup page",
  "Add testimonials on the thank-you page"
]
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert CRO advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    import json

    raw = response.choices[0].message.content.strip()

    try:
        suggestions = json.loads(raw)
    except Exception as e:
        print("GPT Response (raw):", raw)
        print("Parse error:", str(e))
        suggestions = [raw]  # fallback so your app doesn’t crash

    return suggestions