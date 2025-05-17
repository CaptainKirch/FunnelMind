from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Event
from app.services.funnel_analysis import compute_funnel_stats

router = APIRouter()

@router.get("/")
def get_funnel_stats(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    stats = compute_funnel_stats(events)
    return stats
