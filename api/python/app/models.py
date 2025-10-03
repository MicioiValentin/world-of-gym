# app/models.py
from __future__ import annotations

import uuid
from typing import Optional

from sqlmodel import SQLModel, Field


class UserDB(SQLModel, table=True):
    """
    DB model used by SQLModel/SQLAlchemy.
    - Primary key is a UUID generated in Python so inserts work on SQLite in tests.
    - Other columns match your domain schema.
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    username: str
    level: int = 1
    xp: int = 0
    bodyWeightKg: Optional[float] = None
    weightClass: Optional[str] = None

    # Convert DB row -> API schema that your code already defines (ProfilePublic)
    def to_public(self) -> "ProfilePublic":  # type: ignore[name-defined]
        from app.schemas import ProfilePublic
        return ProfilePublic(
            id=str(self.id),  # cast UUID -> str to satisfy your ProfilePublic (int | str)
            username=self.username,
            level=self.level,
            xp=self.xp,
            bodyWeightKg=self.bodyWeightKg,
            weightClass=self.weightClass,
        )
