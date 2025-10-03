# tests/conftest.py
import os

# Force a safe DB for tests before importing app code
os.environ.setdefault("TESTING", "1")
os.environ.setdefault("TEST_DATABASE_URL", "sqlite:///./test.db")

# Import the app to ensure all routes/models are loaded
import app.main  # noqa: F401

from app.db import engine  # uses the SQLite test URL picked above
from sqlmodel import SQLModel

# Create tables for SQLite test DB
SQLModel.metadata.create_all(engine)
