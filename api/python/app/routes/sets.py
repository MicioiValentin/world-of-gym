from app.db import get_session
from app.models import UserDB
from app.schemas import SetRequest, SetResult
from fastapi import APIRouter, Depends
from sqlmodel import Session
from wog.progression import apply_xp, set_xp

router = APIRouter()
ME_ID = "u_1"


@router.post("/v1/sets", response_model=SetResult)
def log_set(payload: SetRequest, session: Session = Depends(get_session)):
    user = session.get(UserDB, ME_ID)
    if not user:
        user = UserDB(id=ME_ID, username="player1", level=1, xp=0)
        session.add(user)
        session.commit()
        session.refresh(user)

    gained = set_xp(payload.reps, payload.weightKg, user.level)
    new_level, new_xp = apply_xp(user.level, user.xp, gained)

    user.level = new_level
    user.xp = new_xp
    session.commit()
    session.refresh(user)

    return SetResult(gainedXp=gained, newLevel=new_level, newXp=new_xp)
