# app/routes/meta.py
from fastapi import APIRouter
from typing import List
from app.schemas import WeightClass   # <— absolute import

router = APIRouter()

WEIGHT_CLASSES: list[WeightClass] = [
    WeightClass(name="59 kg",  minKg=0.0,   maxKg=59.0),
    WeightClass(name="66 kg",  minKg=59.01, maxKg=66.0),
    WeightClass(name="74 kg",  minKg=66.01, maxKg=74.0),
    WeightClass(name="83 kg",  minKg=74.01, maxKg=83.0),
    WeightClass(name="93 kg",  minKg=83.01, maxKg=93.0),
    WeightClass(name="105 kg", minKg=93.01, maxKg=105.0),
    WeightClass(name="120 kg", minKg=105.01, maxKg=120.0),
    WeightClass(name="120+ kg",minKg=120.01, maxKg=None),
]

@router.get("/v1/meta/weight-classes", response_model=List[WeightClass])
def list_weight_classes():
    return WEIGHT_CLASSES
