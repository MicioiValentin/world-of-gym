from fastapi import APIRouter
from wog.weight_classes import DEFAULT_CLASSES
from ..schemas import WeightClass

router = APIRouter(tags=["meta"])

@router.get("/meta/weight-classes", response_model=list[WeightClass])
def weight_classes():
    return [
        WeightClass(name=wc.name, minKg=wc.min_kg, maxKg=wc.max_kg)
        for wc in DEFAULT_CLASSES
    ]
