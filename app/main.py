from fastapi import FastAPI
from app.routers import events, funnel, gpt

app = FastAPI(title="FunnelAI Tracker")

# Include routers
app.include_router(events.router, prefix="/event", tags=["Events"])
app.include_router(funnel.router, prefix="/funnel", tags=["Funnel"])
app.include_router(gpt.router, prefix="/recommendations", tags=["GPT"])

from app.db import Base, engine
from app import models

Base.metadata.create_all(bind=engine)
