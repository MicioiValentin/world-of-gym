from fastapi import APIRouter, Depends, Header, HTTPException
from sqlmodel import Session

from ..db import get_session
from ..models import UserDB
from ..schemas import UpdateProfileRequest, User

router = APIRouter()


def current_user_id(x_user_id: str = Header(..., alias="X-User-Id")) -> str:
    return x_user_id


@router.get("/v1/users/me", response_model=User)
def get_me(
    session: Session = Depends(get_session),
    user_id: str = Depends(current_user_id),
):
    user = session.get(UserDB, user_id)
    if not user:
        user = UserDB(id=user_id, username="player1", level=1, xp=0)
        session.add(user)
        session.commit()
        session.refresh(user)
    return User.model_validate(user)


@router.patch("/v1/users/me", response_model=User)
def update_me(
    payload: UpdateProfileRequest,
    session: Session = Depends(get_session),
    user_id: str = Depends(current_user_id),
):
    user = session.get(UserDB, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if payload.bodyWeightKg is not None:
        user.bodyWeightKg = payload.bodyWeightKg
    session.add(user)
    session.commit()
    session.refresh(user)
    return User.model_validate(user)
