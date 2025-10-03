from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class WeightClass:
    name: str
    min_kg: float
    max_kg: float


DEFAULT_CLASSES: List[WeightClass] = [
    WeightClass("59 kg", 0.0, 59.0),
    WeightClass("66 kg", 59.01, 66.0),
    WeightClass("74 kg", 66.01, 74.0),
    WeightClass("83 kg", 74.01, 83.0),
    WeightClass("93 kg", 83.01, 93.0),
    WeightClass("105 kg", 93.01, 105.0),
    WeightClass("120 kg", 105.01, 120.0),
    WeightClass("120+ kg", 120.01, None),
]


def classify(
    body_weight_kg: Optional[float], classes: List[WeightClass] = DEFAULT_CLASSES
) -> Optional[str]:
    if body_weight_kg is None:
        return None
    for cls in classes:
        if body_weight_kg >= cls.min_kg and (
            cls.max_kg is None or body_weight_kg <= cls.max_kg
        ):
            return cls.name
    return None


WEIGHT_CLASSES = DEFAULT_CLASSES

__all__ = [
    "DEFAULT_CLASSES",
    "WEIGHT_CLASSES",
]
