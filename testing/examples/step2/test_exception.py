import pytest

def test_invalid_values():
    from fibonacci import fibonacci

    with pytest.raises(ValueError, match='n must be >= 0, got -1'):
        fibonacci(-1)
