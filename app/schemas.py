from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    session_id: str
    event_type: str
    url: str
    timestamp: Optional[datetime] = None  # Defaults handled in model
