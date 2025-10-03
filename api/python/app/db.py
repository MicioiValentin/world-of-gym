# app/db.py
import os
import sys
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session

# Robust pytest detection
IS_TEST = (
    "PYTEST_CURRENT_TEST" in os.environ
    or os.getenv("TESTING") == "1"
    or "pytest" in sys.modules  # import-time detection
)

DATABASE_URL = os.getenv("DATABASE_URL")
if IS_TEST:
    DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///./test.db")
elif not DATABASE_URL:
    DATABASE_URL = "sqlite:///./app.db"

# Normalize common driver typo
DATABASE_URL = DATABASE_URL.replace("postgresql+psycog", "postgresql+psycopg2")
DATABASE_URL = DATABASE_URL.replace("postgresql.psycog", "postgresql+psycopg2")

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, future=True, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db = get_session  # back-compat
