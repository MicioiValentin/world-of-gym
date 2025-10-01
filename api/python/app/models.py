# api/python/app/models.py
from typing import Optional
from sqlmodel import SQLModel, Field

class UserDB(SQLModel, table=True):
    id: str = Field(primary_key=True)
    username: str
    level: int = Field(default=1)
    xp: int = Field(default=0)
    bodyWeightKg: Optional[float] = None   # <-- add
    weightClass: Optional[str] = None      # <-- add
