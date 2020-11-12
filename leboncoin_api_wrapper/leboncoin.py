import json
from cloudscraper import create_scraper
import requests


class Results:
    def __init__(self, data):
        self._ = data

    def pprint(self):
        print(json.dumps(self._, indent=4))

    def print(self):
        print(self._)


# noinspection PyTypeChecker,PyPep8Naming
class Leboncoin:
    def __init__(self):
        self._payload = {
            "limit": 35,
            "limit_alu": 3,
            "filters": {
                "enums": {
                    "ad_type": ["offer"]
                },
                "ranges": {
                    "price": {
                        "min": 0,
                    }
                },
                "location": {

                },
                "keywords": {

                },
                "category": {

                }
            }
        }

        with open("./Leboncoin/Ressources/regions.json", "r") as json_file:
            self.region_data = json.load(json_file)
        with open("./Leboncoin/Ressources/departements.json", "r") as json_file:
            self.dept_data = json.load(json_file)

    def setLimit(self, limit):
        self._payload["limit"] = int(limit)

    def maxPrice(self, price):
        self._payload["filters"]["ranges"]["price"]["max"] = int(price)

    def setRegion(self, region_name):
        for region in self.region_data:
            if region["channel"] == region_name:
                self._payload["filters"]["location"]["locations"] = [{
                    "locationType": "region",
                    "region_id": region["id"],
                    "label": region["name"]
                }]

    def setDepartement(self, dept_name):
        for dept in self.dept_data:
            if dept["channel"].lower() == dept_name:
                self._payload["filters"]["location"]["locations"] = [{
                    "country_id": "FR",
                    "department_id": str(dept["id"]),
                    "locationType": "department",
                    "region_id": dept["region_id"]
                }]

    @staticmethod
    def _get_category(query):
        url = f"https://api.leboncoin.fr/api/parrot/v1/complete?q={query.replace(' ', '%20')}"
        anti_captcha = create_scraper(browser="chrome")
        return str(anti_captcha.get(url).json()[0]["cat_id"])

    def searchFor(self, query, autoCatgory=True):
        self._payload["filters"]["keywords"]["text"] = query
        if autoCatgory:
            self._payload["filters"]["category"]["id"] = str(self._get_category(query))

    def setCategory(self, query):
        self._payload["filters"]["category"]["id"] = self._get_category(query)

    def execute(self):
        r = requests.post(
            url="https://api.leboncoin.fr/finder/search",
            data=json.dumps(self._payload),
            headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
                'Accept': '*/*',
                'DNT': '1',
            }
        )
        if r.status_code != 200:
            raise Exception
        return Results(data=r.json())
