from typing import Optional, List
from pydantic import BaseModel, Field

class User(BaseModel):
    id: str
    username: str
    level: int = Field(ge=1)
    xp: int = Field(ge=0)
    bodyWeightKg: Optional[float] = None
    weightClass: Optional[str] = None

class UpdateProfileRequest(BaseModel):
    bodyWeightKg: Optional[float] = None


class SetRequest(BaseModel):
    reps: int = Field(ge=1)
    WeightKg: float
    level: int = Field(ge=1)
    currentXp: int = Field(ge=0)

class SetResult(BaseModel):
    gainedXp: int
    newLevel: int
    newXp: int


class LeaderboardEntry(BaseModel):
    userId: str
    username: str
    level: int
    totalXp: int
    weightClass: Optional[str] = None

class LeaderboardResponse(BaseModel):
    items: List[LeaderboardEntry]
