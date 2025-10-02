from app.db import get_session
from app.models import UserDB
from app.schemas import ProfilePublic, UpdateProfileRequest
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(prefix="/profiles", tags=["profiles"])


async def get_current_user(db: Session = Depends(get_session)) -> UserDB:
    me = db.execute(select(UserDB).limit(1)).scalar_one_or_none()
    if not me:
        raise HTTPException(401, "No users exist to act as current user")
    return me


@router.get("/search", response_model=list[ProfilePublic])
async def search_profiles(
    q: str = Query("", min_length=0, max_length=50),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_session),
):
    offset = (page - 1) * page_size
    stmt = (
        select(UserDB)
        .where(UserDB.username.ilike(f"%{q}%"))
        .order_by(UserDB.level.desc(), UserDB.xp.desc(), UserDB.id.asc())
        .offset(offset)
        .limit(page_size)
    )
    return list(db.execute(stmt).scalars())


@router.get("/{user_id}", response_model=ProfilePublic)
async def get_profile(user_id: int | str, db: Session = Depends(get_session)):
    user = db.get(UserDB, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.patch("/me", response_model=ProfilePublic)
async def update_me(
    payload: UpdateProfileRequest,
    db: Session = Depends(get_session),
    me: UserDB = Depends(get_current_user),
):
    if payload.username is not None:
        me.username = payload.username.strip()

    db.commit()
    db.refresh(me)
    return me
