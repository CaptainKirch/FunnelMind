from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    event_type = Column(String)
    url = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
