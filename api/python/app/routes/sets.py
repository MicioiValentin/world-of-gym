from fastapi import APIRouter, Depends
from ..schemas import SetRequest, SetResult
from wog.progression import set_xp, apply_xp
from ..db import get_session
from ..models import UserDB

router = APIRouter(tags=["sets"])
ME_ID = "u_1"

@router.post("/sets", response_model=SetResult)
def create_set(body: SetRequest, session=Depends(get_session)):
    gained = set_xp(body.reps, body.weightKg, body.level)
    new_level, new_xp = apply_xp(body.level, body.currentXp, gained)

    user = session.get(UserDB, ME_ID)
    if not user:
        user = UserDB(id=ME_ID, username="valentin", level=body.level, xp=body.currentXp)
        session.add(user)

    user.level = new_level
    user.xp = new_xp
    session.add(user)
    session.commit()

    return SetResult(gainedXp=gained, newLevel=new_level, newXp=new_xp)
