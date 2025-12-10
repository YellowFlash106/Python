import requests

def get_weather(latitude, longitude):
    res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}current=temperature_2m,wind_speed_10m")
    data = res.json()
    return data['current']['tempreture_2m']

# get tmp for diff cities
paris_temp = get_weather(43.22, 3.22)
london_temp = get_weather(45.2, -0.22)
tokyo_temp = get_weather(33.32, 133.32)


print(f"Paris: {paris_temp} C")
print(f"London: {london_temp} C")
print(f"Tokyo: {tokyo_temp} C")