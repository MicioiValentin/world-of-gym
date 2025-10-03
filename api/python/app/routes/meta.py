from typing import List

from app.schemas import WeightClass as WeightClassDTO
from fastapi import APIRouter
from wog.weight_classes import DEFAULT_CLASSES  # <-- use what's exported

router = APIRouter()


@router.get("/v1/meta/weight-classes", response_model=List[WeightClassDTO])
def list_weight_classes():
    # Convert domain objects (snake_case) to API DTO (camelCase)
    return [WeightClassDTO.model_validate(wc) for wc in DEFAULT_CLASSES]
