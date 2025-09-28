import pytest
from wog.progression import set_xp, xp_to_next, apply_xp, apply_decay

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

def test_decay_thresholds():
    assert apply_decay(5, 100)[1] == 100
    assert apply_decay(6, 100)[1] == 85

def test_guards():
    with pytest.raises(ValueError): set_xp(0, 10, 1)
    with pytest.raises(ValueError): set_xp(5, 10, 0)
    with pytest.raises(ValueError): xp_to_next(0)
    with pytest.raises(ValueError): apply_xp(0, 0, 0)
    with pytest.raises(ValueError): apply_xp(1, -1, 0)
    with pytest.raises(ValueError): apply_xp(1, 0, -1)
    with pytest.raises(ValueError): apply_decay(0, 0)
    with pytest.raises(ValueError): apply_decay(1, -5)
