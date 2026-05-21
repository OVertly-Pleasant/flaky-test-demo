import random
import datetime

def test_always_passes():
    assert 1 + 1 == 2

def test_always_fails():
    assert 1 == 2

def test_flaky():
    # Signal 1 & 2: Pure mathematical randomness
    assert random.random() > 0.5

def test_another_flaky():
    assert random.random() > 0.3

def test_time_of_day():
    """
    Signal 8: Time-of-day failure.
    We use minutes instead of hours so no need to wait 12 hours to test it.
    """
    current_minute = datetime.datetime.utcnow().minute
    # Passes from :00 to :29, Fails from :30 to :59
    assert current_minute < 30

def test_burst_clustering():
    """
    Signal 6: Burst clustering. 
    It passes 80% of the time, but when it fails simulate a "database timeout"
    by making it sleep for a second which tests your duration_ms field!.
    """
    import time
    if random.random() > 0.8:
        time.sleep(1) # Simulates a slow run
        assert False  # Then fails
    assert True