# XP & Leveling Rules (Spec)

## Per-set XP
Given (reps, weightKg, level):
- base = reps * sqrt(weightKg)
- scaling = 1 / (1 + 0.08 * max(level - 1, 0))
- xp = round(base * scaling)
- Clamp weightKg < 0 to 0; reps must be >= 1.

Examples:
- reps=10, weight=50kg, level=1:
  sqrt(50)≈7.0711 → base≈70.7107 → scaling=1 → **xp=71**
- reps=10, weight=50kg, level=6:
  scaling=1/(1+0.08*5)=1/1.4≈0.7143
  70.7107*0.7143≈50.5 → **xp=51**
- reps=8, weight=60kg, level=1:
  sqrt(60)≈7.7460 → base≈61.9677 → **xp=62**
- reps=8, weight=60kg, level=10:
  scaling=1/(1+0.08*9)=1/1.72≈0.5814
  61.9677*0.5814≈36.0 → **xp=36**

## Level curve (XP needed to reach next level)
xpToNext(level) = 100 + floor(30 * level^1.35)

Approx values:
- L1: 130, L2: 176, L3: 232, L4: 294, L5: 363,
- L6: 437, L7: 515, L8: 597, L9: 682, L10: 771  (approx; compute programmatically later)

## Cooldown
- After a user logs **>= 120 minutes** in a local calendar day, further sets award **0 XP** until the next day.

## Decay (consistency mechanic)
- Applies **only if level > 5**.
- If a user skips **two consecutive weekdays (Mon–Fri)**, apply decay on next app open:
  - newXP = floor(currentXP * 0.85) within the current level.
  - If after applying decay you’d go below 0, drop a level and recompute carryover (never below level 1).

## Anti-abuse sanity checks
- Ignore sets where reps > 100 or weightKg > 500 by default (validation error).
- Ignore sets with obviously impossible cadence (server-side future check).
- Server is the source of truth: XP is computed server-side, not by the client.

## Weight Classes
Weight classes are for fair comparison on leaderboards. XP/Level math is independent of body weight and is not scaled by it.
