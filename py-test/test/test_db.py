import pytest
from db import Database

@pytest.fixture
def db():
    """Creates a fresh instance of Database for each test."""
    database = Database()
    yield database # provides the fixture value to the test function
    database.data.clear() #cleanup step after the test function runs

def test_add_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == {"name": "Alice"}

def test_add_duplicate_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User ID already exists."):
        db.add_user(1, "Bob")

def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None