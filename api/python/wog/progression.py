import math
from decimal import Decimal, ROUND_HALF_UP

def _round_half_up(x: float) -> int:
    return int(Decimal(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def xp_to_next(level: int) -> int:
    if level < 1:
        raise ValueError("level must be >= 1")
    return 100 + math.floor(30 * (level ** 1.35))

def set_xp(reps: int, weight_kg: float, level: int) -> int:
    if reps < 1:
        raise ValueError("reps must be >= 1")
    if level < 1:
        raise ValueError("level must be >= 1")
    w = max(weight_kg, 0.0)
    base = reps * math.sqrt(w)
    scaling = 1.0 / (1.0 + 0.08 * max(level - 1, 0))
    return _round_half_up(base * scaling)

def apply_xp(level: int, xp: int, gained: int):
    if level < 1:
        raise ValueError("level must be >= 1")
    if xp < 0 or gained < 0:
        raise ValueError("xp and gained must be >= 0")
    new_level = level
    cur_xp = xp + gained
    while cur_xp >= xp_to_next(new_level):
        cur_xp -= xp_to_next(new_level)
        new_level += 1
    return new_level, cur_xp

def apply_decay(level: int, xp: int):
    if level < 1:
        raise ValueError("level must be >= 1")
    if xp < 0:
        raise ValueError("xp must be >= 0")
    if level <= 5:
        return level, xp
    reduced = math.floor(xp * 0.85)
    return level, max(reduced, 0)
