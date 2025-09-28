# Weight Classes (Config)

Purpose: server computes `weightClass` from `bodyWeightKg` using these ranges.
Policy: lower bound inclusive; upper bound inclusive (except last open-ended class).

## Default classes (unisex for MVP)
- 59 kg:   0.0  – 59.0
- 66 kg:  59.01 – 66.0
- 74 kg:  66.01 – 74.0
- 83 kg:  74.01 – 83.0
- 93 kg:  83.01 – 93.0
- 105 kg: 93.01 – 105.0
- 120 kg: 105.01 – 120.0
- 120+ kg: >120.0

Notes
- If `bodyWeightKg` is missing, user is **Unclassified**.
- Later we can split by sex/age if you want (e.g., Male/Female/Open masters/juniors).
