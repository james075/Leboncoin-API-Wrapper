from DataClasses.Payload.Payload import *
from DataClasses.Response.Response import *

import requests

# area = Area(lat=43.703284, lng=1.80605, radius=20000)
# loc = Location(area=area, region=set_region("aquitaine"))

payload = Payload(
    limit=35,
    limit_alu=0,
    filters=Filters(
        category=Category(id=get_category("google home")),
        enums=Enums(ad_type=["offer"]),
        location=Locale(department=set_dept("tarn")),
        keywords=Keywords(text="google home"),
        ranges=Ranges()
    )
).to_json

reponse = Response(**requests.post(
    url="https://api.leboncoin.fr/finder/search",
    data=payload,
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': '*/*',
        'DNT': '1',
    }  # Fake User-Agent
).json())


for ads in reponse.ads:
    offre = Ads(**ads)
    print(f"Titre: {offre.subject}")
    print(f"Prix: {offre.price[0]}€")
    print(f"Ville: {Location(**offre.location).city_label}")
    print("")
