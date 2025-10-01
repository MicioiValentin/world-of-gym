from fastapi import APIRouter, Depends, Query
from typing import Optional
from sqlmodel import Session, select
from ..db import get_session
from ..models import UserDB
from ..schemas import LeaderboardEntry, LeaderboardResponse

router = APIRouter()

@router.get("/v1/leaderboard", response_model=LeaderboardResponse)
def leaderboard(
    weightClass: Optional[str] = Query(default=None, description="e.g., '93kg'"),
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    session: Session = Depends(get_session),
):
    stmt = select(UserDB)


    if weightClass is not None:
        stmt = stmt.where(UserDB.weightClass == weightClass)

    stmt = (
        stmt.order_by(
            UserDB.level.desc(),
            UserDB.xp.desc(),
            UserDB.username.asc(),  
        )
        .offset(offset)
        .limit(limit)
    )

    rows = session.exec(stmt).all()
    items = [
        LeaderboardEntry(
            userId=row.id,
            username=row.username,
            level=row.level,
            totalXp=row.xp,
            weightClass=row.weightClass,
        )
        for row in rows
    ]
    return LeaderboardResponse(items=items)
