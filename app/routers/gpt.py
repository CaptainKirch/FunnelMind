from fastapi import APIRouter, Body, HTTPException
from app.services.gpt_prompts import generate_recommendations

router = APIRouter()

@router.post("/")
def get_gpt_recommendations(funnel_data: dict = Body(...)):
    try:
        suggestions = generate_recommendations(funnel_data)
        return {"recommendations": suggestions}
    except Exception as e:
        print("GPT Error:", str(e))  # Log the actual error to terminal
        raise HTTPException(status_code=500, detail="GPT API failed")
