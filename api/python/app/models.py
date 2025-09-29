from typing import Optional
from sqlmodel import SQLModel, Field

class UserDB(SQLModel, table=True):
    __tablename__ = "users"
    id: str = Field(primary_key=True)
    username: str
    level: int = Field(default=1, ge=1)
    xp: int = Field(default=0, ge=0)
    bodyweightKg: Optional[float] = Field(default=None, alias="body_weight_kg")
    weightClass: Optional[str] = Field(default=None, alias="weight_class")