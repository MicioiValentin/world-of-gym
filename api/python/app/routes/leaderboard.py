from typing import Optional
from fastapi import APIRouter, Query, Depends
from sqlmodel import select
from ..schemas import LeaderboardEntry, LeaderboardResponse
from ..models import UserDB
from ..db import get_session

router = APIRouter(tags=["leaderboard"])

@router.get("/leaderboard", response_model=LeaderboardResponse)
def leaderboard(
    weightClass: Optional[str] = Query(default=None),
    limit: int = Query(default=50, ge=1, le=200),
    session = Depends(get_session),
):
    stmt = select(UserDB).order_by(UserDB.xp.desc(), UserDB.level.desc())
    if weightClass:
        stmt = stmt.filter(UserDB.weightClass == weightClass)
    users = session.exec(stmt).all()[:limit]
    items = [
        LeaderboardEntry(
            userId=u.id,
            username=u.username,
            level=u.level,
            totalXp=u.xp,
            weightClass=u.weightClass,
        )
        for u in users
    ]
    return LeaderboardResponse(items=items)
