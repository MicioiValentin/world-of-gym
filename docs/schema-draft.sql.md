- schema-draft.sql.md

# Users (table: users)
- id (uuid, pk)
- username (text, unique)
- level (int not null default 1)
- xp (int not null defualt 0)
- total_xp (bigint not null default 0)
- last_workout_at (timestamptz)
- body_weight_kg (numeric(5,2)) -- nullable
- weight_class (text)           -- cached string for fast leaderboard; computed in app logic on updates
- created_at (timestamptz not null default now())
- updated_at (timestamptz not null default now())

# Leaderboard query

- SELECT * FROM users WHERE (weight_class = $1) ORDER BY total_xp DESC LIMIT 10;
