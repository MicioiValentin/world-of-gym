from fastapi import APIRouter
from typing import List

from wog.weight_classes import WEIGHT_CLASSES  # domain source (snake_case)
from app.schemas import WeightClass as WeightClassDTO  # API schema with camelCase

router = APIRouter()


@router.get("/v1/meta/weight-classes", response_model=List[WeightClassDTO])
def list_weight_classes():
    """
    Expose the list of weight classes from the domain logic.
    Converts them into API schemas with camelCase fields.
    """
    return [WeightClassDTO.model_validate(wc) for wc in WEIGHT_CLASSES]
