import requests

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={longitude}&current=temperature_2m"

res = requests.get(url)
data = res.json()
print(data)