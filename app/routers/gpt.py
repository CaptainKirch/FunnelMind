from fastapi import APIRouter, Body
from app.services.gpt_prompts import generate_recommendations

router = APIRouter()

@router.post("/")
def get_gpt_recommendations(funnel_data: dict = Body(...)):
    suggestions = generate_recommendations(funnel_data)
    return {"recommendations": suggestions}
