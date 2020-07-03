# Leboncoin API Wrapper
![Coverage Badge](coverage.svg)
[![Build Status](https://img.shields.io/github/forks/Shinyhero36/LeboncoinApiWraper.svg)](https://github.com/Shinyhero36/LeboncoinApiWraper)
[![Build Status](https://img.shields.io/github/stars/Shinyhero36/LeboncoinApiWraper.svg)](https://github.com/Shinyhero36/LeboncoinApiWraper)

Allow easy acces to leboncoin api using python

## Installation
```bash
pip install requirements.txt
```

## Usage
```python
from DataClasses.Payload.Payload import *
from DataClasses.Response.Response import *
import requests


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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)