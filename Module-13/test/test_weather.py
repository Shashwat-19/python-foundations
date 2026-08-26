# from main import get_weather
from main import add, divide
import pytest
# def test_get_weather():
#     assert get_weather(25) == "hot"
#     assert get_weather(15) == "cold"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 3) == 2
    assert add(0, 0) == 0
    assert add(-2, -2) == -4

def test_divide():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
    assert divide(10, 2) == 5