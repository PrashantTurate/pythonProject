# Fixture - Concept in python
# Similar to pre condition, post condition.
# Pre Condition - token, booking Id - Fixture


import pytest

@pytest.fixture()
def is_married():
    return True


def test_confirmation(is_married):
    assert is_married == True