import pytest

@pytest.fixture(scope='function')
def some_data():
    return [1, 2, 3]

def test_mutatable(some_data):
    # will fail because the first test mutated the array
    # if scope of fixture is "function" then it will not fail
    some_data[0] == 5
    assert some_data[0] == 5

def test_using_fixture(some_data):
    assert len(some_data) == 3

def test_also_using_fixture(some_data):
    # will not fail with fixture "session"
    # if scope of fixture is "function" then it will fail
    assert some_data[0] == 1
