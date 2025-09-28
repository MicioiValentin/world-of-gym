from fastapi import APIRouter
from ..schemas import User, UpdateProfileRequest
from wog.weight_classes import classify

router = APIRouter(tags=["users"])

_ME = User(id="u_1", username="valentin", level=1, xp=0, bodyWeightKg=None, weightClass=None)

@router.get("/users/me", response_model=User)
def get_me():
    return _ME

@router.patch("/users/me", response_model=User)
def patch_me(req: UpdateProfileRequest):
    global _ME
    if req.bodyWeightKg is not None:
        _ME.bodyWeightKg = req.bodyWeightKg
        _ME.weightClass = classify(req.bodyWeightKg)
    return _ME
