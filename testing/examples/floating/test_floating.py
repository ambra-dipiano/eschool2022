import pytest

def test_addition_naive():
    # this will fail due to floating points
    assert 0.1 + 0.2 == 0.3

@pytest.mark.xfail
def test_addition_naive():
    # this will fail expectedly so we mark it
    assert 0.1 + 0.2 == 0.3

def test_addition_correct():
    assert 0.1 + 0.2 == pytest.approx(0.3)
