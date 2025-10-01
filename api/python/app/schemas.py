from typing import Optional, List
from pydantic import BaseModel, Field
from pydantic import ConfigDict
from wog.weight_classes import WeightClass


class WeightClass(BaseModel):
    name: str
    minKg: float = Field(alias="min_kg")
    maxKg: float | None = Field(alias="max_kg")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )

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
