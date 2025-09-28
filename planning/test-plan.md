## Weight Class Tests
15) Classification: 74.0 kg ? "74 kg"; 74.01 kg ? "83 kg".
16) Lower/upper bound inclusivity per config (min inclusive, max inclusive; last class is open-ended).
17) Unclassified: no bodyWeightKg ? excluded from weightClass-filtered leaderboard; included in global.
18) Leaderboard filter: `?weightClass=83 kg` returns only users in that class.
19) Update profile: PATCH /v1/users/me { bodyWeightKg: 73.9 } ? user.weightClass updates accordingly.
