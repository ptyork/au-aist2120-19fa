import json
import requests as req
from pprint import pprint as pp

with open("\\apikeys.json") as fi:
    apikeys = json.loads(fi.read())

print(apikeys.keys())

owapi = apikeys["OpenWeather"]

resp = req.get(
    "http://api.openweathermap.org/data/2.5/weather",
    params={
        "zip": "30904",
        "appid": owapi,
        "units": "imperial"
    }
)
#print(resp.text)
weather = json.loads(resp.text)
#pp(weather)

# print(f"{'Temp':20}{weather['main']['temp']}")
desc = weather['weather'][0]['description']
print(f"{'Weather':20}{desc.title()}")

resp = req.get(
    "http://api.openweathermap.org/data/2.5/forecast",
    params={
        "zip": "30904",
        "appid": owapi,
        "units": "imperial"
    }
)
forecast = json.loads(resp.text)
# pp(forecast)

for fc in forecast['list']:
    print(f"{fc['dt_txt']:20}{fc['main']['temp']}")
