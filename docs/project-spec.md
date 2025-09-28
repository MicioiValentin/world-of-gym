#world of gym - MVP Spec
- Log sets manually (exercise, reps, kg)
- XP per set with diminishing returns by level
- Level-ups; Daily 120 min cooldown (no XP after)
- Decay if skipping 2 weekdays (abole level 5)
- Local leaderboard (later :Global)
Non-goals (MVP): sensors, BLE, payments.
Open questions: achievements list, titles taxonomy.
## Weight Classes (MVP+)
- Users can set "bodyWeightKg".
- Server computes "weightClass" from configurable ranges (see docs/weight-classes.md).
- Leaderboard supports an optional 'weightClass' filter.
