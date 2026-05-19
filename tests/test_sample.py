import random

def test_always_passes():
    assert 1 + 1 == 2

def test_always_fails():
    assert 1 == 2

def test_flaky():
    # randomly passes or fails
    assert random.random() > 0.5

def test_another_flaky():
    assert random.random() > 0.3