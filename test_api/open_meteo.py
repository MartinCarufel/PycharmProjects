import requests
import json

url = "https://api.open-meteo.com/v1/"
command = "forecast?latitude=45.5699&longitude=-73.692&models=gem_seamless&current=temperature_2m,relative_humidity_2m&timezone=America%2FNew_York"
r = requests.get(url+command)
# r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5699&longitude=-73.692&models=gem_seamless&current=temperature_2m,relative_humidity_2m&timezone=America%2FNew_York")

print(r.json()["current"]["temperature_2m"]) 