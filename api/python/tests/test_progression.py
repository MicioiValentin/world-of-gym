from wog.progression import set_xp, xp_to_next, apply_xp

def test_set_xp_examples():
    assert set_xp(10, 50, 1) == 71
    assert set_xp(10, 50, 6) == 51
    assert set_xp(8, 60, 10) == 36
    assert set_xp(10, -5, 1) == 0

def test_xp_to_next_monotonic():
    vals = [xp_to_next(i) for i in range(1, 11)]
    assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))

def test_apply_xp_exact_threshold():
    lvl, xp = 1, 0
    lvl, xp = apply_xp(lvl, xp, 130)
    assert (lvl, xp) == (2, 0)
