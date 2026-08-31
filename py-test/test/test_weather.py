from weather import get_weather
def test_get_weather():
    assert get_weather(25) == "It's hot outside!"
    assert get_weather(15) == "It's cold outside!"
    assert get_weather(20) == "It's cold outside!"