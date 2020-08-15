from Payload.Payload import Payload
import requests
import json

# area = Area(lat=43.703284, lng=1.80605, radius=20000)
# loc = Location(area=area, region=set_region("aquitaine"))


def callAPI(payload):
    return requests.post(
        url="https://api.leboncoin.fr/finder/search",
        data=payload,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
            'Accept': '*/*',
            'DNT': '1',
        }
    )

# payload = {"limit":0,"limit_alu":0,"filters":{"category":{},"enums":{"ad_type":["offer"]},"location":{"locations":[{"locationType":"region","label":"Midi-Pyrénées","region_id":"16"}]},"keywords":{"text":"google home","parrot_used":4},"ranges":{"price":{"max":100}}}}
# payload = json.dumps(payload)
# print(callAPI(payload).json())

pl = Payload()
pl.setLimit(30)
pl.maxPrice(200)
pl.setDepartement("tarn")
pl.searchFor("google home", True)
print(pl.build())
print(callAPI(pl.build()).json())