import pytest
import time

# this marker must be defined in the project.toml
# it will be skipped if run without the correct marker expression
# $ pytest -m "not slow" will skip it
# $ pytest -m "slow" will run it
@pytest.mark.slow
def test_slow():
    time.sleep(2)
    assert 1 + 1 == 2

def test_fast():
    assert 1 + 1== 2
