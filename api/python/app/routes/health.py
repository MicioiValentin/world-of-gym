from app.db import SessionLocal
from fastapi import APIRouter
from sqlalchemy import text

router = APIRouter()


@router.get("/healthz", tags=["health"])
def healthz():
    with SessionLocal() as db:
        db.execute(text("SELECT 1"))
    return {"status": "ok"}
