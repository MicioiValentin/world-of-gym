from fastapi import APIRouter, Depends
from sqlmodel import select
from ..schemas import User, UpdateProfileRequest
from ..models import UserDB
from ..db import get_session
from wog.weight_classes import classify

router = APIRouter(tags=["users"])

ME_ID = "u_1"
ME_USERNAME = "valentin"

@router.get("/users/me", response_model=User)
def get_me(session=Depends(get_session)):
    user = session.get(UserDB, ME_ID)
    if not user:
        user = UserDB(id=ME_ID, username=ME_USERNAME, level=1, xp=0)
        session.add(user)
        session.commit()
        session.refresh(user)
    return _to_api_user(user)

@router.patch("/users/me", response_model=User)
def patch_me(req: UpdateProfileRequest, session=Depends(get_session)):
    user = session.get(UserDB, ME_ID)
    if not user:
        user = UserDB(id=ME_ID, username=ME_USERNAME, level=1, xp=0)
        session.add(user)

    if req.bodyWeightKg is not None:
        user.bodyWeightKg = req.bodyWeightKg
        user.weightClass = classify(req.bodyWeightKg)

    session.add(user)
    session.commit()
    session.refresh(user)
    return _to_api_user(user)

def _to_api_user(u: UserDB) -> User:
    return User(
        id=u.id,
        username=u.username,
        level=u.level,
        xp=u.xp,
        bodyWeightKg=u.bodyWeightKg,
        weightClass=u.weightClass,
    )
