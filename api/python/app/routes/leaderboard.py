from typing import Optional
from fastapi import APIRouter, Query
from ..schemas import LeaderboardEntry, LeaderboardResponse

router = APIRouter(tags=["leaderboard"])

_LEADERBOARD = [
    LeaderboardEntry(userId="u_1", username="valentin", level=6, totalXp=12345, weightClass="83 kg"),
    LeaderboardEntry(userId="u_2", username="alex",     level=4, totalXp= 8123, weightClass="74 kg"),
    LeaderboardEntry(userId="u_3", username="jordan",   level=9, totalXp=25000, weightClass="120+ kg"),
]

@router.get("/leaderboard", response_model=LeaderboardResponse)
def leaderboard(weightClass: Optional[str] = Query(default=None)):
    items = _LEADERBOARD
    if weightClass:
        items = [x for x in items if x.weightClass == weightClass]
    return LeaderboardResponse(items=items)
