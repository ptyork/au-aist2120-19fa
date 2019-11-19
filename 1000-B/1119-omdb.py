import json
import requests as req
from pprint import pprint as pp

with open("\\apikeys.json") as fi:
    apikeys = json.loads(fi.read())

# print(apikeys.keys())

omdbapi = apikeys["OMDB"]

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "t": "the fly",
        "apikey": omdbapi
    }
)
#print(resp.text)
movie = json.loads(resp.text)
pp(movie)


resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "s": "the fly",
        "apikey": omdbapi,
        "page": 2
    }
)
#print(resp.text)
movies = json.loads(resp.text)
pp(movies)

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "t": "Avatar The Last Airbender",
        "type": "series",
        "apikey": omdbapi
    }
)
#print(resp.text)
show = json.loads(resp.text)
pp(show)

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "t": "Avatar The Last Airbender",
        "type": "series",
        "season": 1,
        "apikey": omdbapi
    }
)
#print(resp.text)
s1 = json.loads(resp.text)
pp(s1)


resp = req.get(show["Poster"])
#print(resp.content)
title = show["Title"]
title = title.replace(':', '')
title = title.replace(' ', '_')
title += '.jpg'
with open(title,"wb") as fi:
    fi.write(resp.content)
