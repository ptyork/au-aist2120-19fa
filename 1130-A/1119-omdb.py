import json
import requests as req
from pprint import pprint as pp

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OMDB"]

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "t": "the fly",
        "y": 1958
    }
)
movie = json.loads(resp.text)
pp(movie)


resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "s": "the fly",
        "page": 2
    }
)
movies = json.loads(resp.text)
#pp(movies)


resp = req.get(movie["Poster"])
#print(resp.content)

fn = movie["Title"]
fn = fn.strip().replace(' ', '_').replace(':', '')
fn += '.jpg'
with open(fn,'wb') as fi:
    fi.write(resp.content)

