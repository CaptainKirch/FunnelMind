import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recommendations(funnel_data: dict) -> list:
    prompt = f"""
    You are a CRO (conversion optimization) expert. Analyze this funnel performance and suggest 3 very specific optimizations.

    Funnel data:
    {funnel_data}

    Suggestions:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert CRO advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    suggestions = response.choices[0].message.content.strip()
    return suggestions.split("\n")
