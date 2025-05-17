from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Event
from app.schemas import EventCreate
from datetime import datetime

router = APIRouter()

@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(
        session_id=event.session_id,
        event_type=event.event_type,
        url=event.url,
        timestamp=event.timestamp or datetime.utcnow()
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return {"message": "Event recorded", "id": db_event.id}
