from time import perf_counter

from app.db import get_session
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["infra"])


@router.get("/metrics")
async def metrics(db: AsyncSession = Depends(get_session)):
    t0 = perf_counter()
    await db.execute("SELECT 1")
    ms = (perf_counter() - t0) * 1000
    body = (
        "#HELP wog_db_ping_ms Database ping in milliseconds\n"
        "# TYPE wog_db_ping_ms gauge\n"
        f"wog_db_ping_ms {ms:.2f}\n"
    )
    return Response(content=body, media_type="text/plain")
