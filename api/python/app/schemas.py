from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


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


class ProfilePublic(BaseModel):
    id: int | str
    username: str
    level: int
    xp: int
    bodyWeightKg: float | None = None
    weightClass: str | None = None

    model_config = ConfigDict(from_attributes=True)


class UpdateProfileRequest(BaseModel):
    username: str | None = Field(None, min_length=3, max_length=32)
