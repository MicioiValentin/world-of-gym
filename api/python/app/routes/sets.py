from fastapi import APIRouter
from ..schemas import SetRequest, SetResult
from wog.progression import set_xp, apply_xp

router = APIRouter(tags=["sets"])

@router.post("/sets", response_model=SetResult)
def create_set(body: SetRequest):
    gained = set_xp(body.reps, body.weightKg, body.level)
    new_level, new_xp = apply_xp(body.level, body.currentXp, gained)
    return SetResult(gainedXp=gained, newLevel=new_level, newXp=new_xp)
