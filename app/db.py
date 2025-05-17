from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite for now, upgradeable to Postgres later
DATABASE_URL = "sqlite:///./funnel_tracker.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Dependency for route access
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
