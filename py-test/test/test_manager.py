import pytest
from manager import UserManager

@pytest.fixture # runs before every single test function
def user_manager():
    """Creates a fresh instance of UserManager for each test."""
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_user("user1", "user1@example.com") is True
    assert user_manager.get_user("user1") == {"email": "user1@example.com"}

def test_add_duplicate(user_manager):
    user_manager.add_user("user1", "user1@example.com")
    with pytest.raises(ValueError):
        user_manager.add_user("user1", "user1_new@example.com")

