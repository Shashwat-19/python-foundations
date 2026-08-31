def get_weather(temp):
    temp = float(temp)
    if temp > 20:
        return "It's hot outside!"
    else:
        return "It's cold outside!"

