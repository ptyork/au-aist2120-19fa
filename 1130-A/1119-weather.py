import json
import requests as req
from pprint import pprint as pp

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

print(apikeys.keys())
key = apikeys["OpenWeather"]

resp = req.get(
    "http://api.openweathermap.org/data/2.5/weather",
    params={
        "appid": key,
        "zip": "30904",
        "units": "imperial"
    }
)
#print(resp.text)
weather = json.loads(resp.text)
#pp(weather)

temp = weather['main']['temp']
print(f"Temp: {temp}")

desc = weather['weather'][0]['description']
print(f"Conditions: {desc.title()}")


resp = req.get(
    "http://api.openweathermap.org/data/2.5/forecast",
    params={
        "appid": key,
        "zip": "30904",
        "units": "imperial"
    }
)
forecast = json.loads(resp.text)
#pp(forecast)

cnt = 1
for fc in forecast['list']:
    time = fc['dt_txt']
    temp = fc['main']['temp']
    print(f"{cnt} -- {time}: {temp}")
    cnt += 1
