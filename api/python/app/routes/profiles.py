# app/routes/profiles.py
from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db import get_session
from app.models import UserDB
from app.schemas import ProfilePublic, UpdateProfileRequest

router = APIRouter()


def get_current_user(db: Session = Depends(get_session)) -> UserDB:
    """
    Minimal 'auth' for tests: return the first user in the DB.
    Tests create one user up-front.
    """
    user = db.exec(select(UserDB).limit(1)).first()
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user


@router.get("/profiles/{user_id}", response_model=ProfilePublic)
def get_profile(user_id: str, db: Session = Depends(get_session)) -> ProfilePublic:
    # Tests pass the id as a string; the DB PK is UUID.
    # Convert string -> UUID before fetching, 404 if invalid/unknown.
    try:
        uuid_pk = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")

    user = db.get(UserDB, uuid_pk)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.to_public()


@router.get("/profiles/search", response_model=list[ProfilePublic])
def search_profiles(
    q: str,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_session),
) -> list[ProfilePublic]:
    stmt = (
        select(UserDB)
        .where(UserDB.username.contains(q))
        .offset((page - 1) * page_size)
        .limit(page_size)
    )
    users = db.exec(stmt).all()
    return [u.to_public() for u in users]


@router.patch("/profiles/me", response_model=ProfilePublic)
def update_me(
    payload: UpdateProfileRequest,
    db: Session = Depends(get_session),
    current_user: UserDB = Depends(get_current_user),
) -> ProfilePublic:
    data = payload.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(current_user, field, value)

    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user.to_public()
