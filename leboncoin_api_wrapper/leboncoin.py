from typing import List

from dataclasses import dataclass

import json
import os
#  from pathlib import Path

import requests
from cloudscraper import create_scraper


@dataclass
class Advertisement:
    """
    This class represent an ad with the following attributes
    """
    list_id: str
    first_publication_date: str
    index_date: str
    status: str
    category_id: str
    category_name: str
    subject: str
    body: str
    ad_type: str
    url: str
    price: List[int]
    price_calendar: str
    images: dict
    attributes: List[dict]
    location: dict
    owner: dict
    options: dict
    has_phone: bool

    # noinspection PyTypeChecker
    def __post_init__(self):
        self.price = self.price[0]


class Results:
    def __init__(self, data):
        self._ = data

    def ads(self):
        """
        :return: A list of ads
        """
        return [Advertisement(**ad) for ad in self._["ads"]]

    def shippable_ads(self):
        """
        :return: Return a list of shippable product
        """
        return [Advertisement(**ad) for ad in self._["ads_shippable"]]

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

        current_path = os.path.dirname(os.path.realpath(__file__))
        with open(current_path + "/Ressources/regions.json", "r") as json_file:
            self.region_data = json.load(json_file)
        with open(current_path + "/Ressources/departements.json", "r") as json_file:
            self.dept_data = json.load(json_file)

    def setLimit(self, limit):
        self._payload["limit"] = int(limit)

    def maxPrice(self, price):
        self._payload["filters"]["ranges"]["price"]["max"] = int(price)

    def minPrice(self, price):
        self._payload["filters"]["ranges"]["price"]["min"] = int(price)

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
        res = anti_captcha.get(url).json()
        if res:
            assert isinstance(res, List), f"Unexpected answer received from API: {res!r}"
            return str(res[0]["cat_id"])
        else:
            # No category returned
            return None

    def searchFor(self, query, autoCatgory=True):
        self._payload["filters"]["keywords"]["text"] = query
        if autoCatgory:
            category = self._get_category(query)
            if category:
                self._payload["filters"]["category"]["id"] = str(category)

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
        r.raise_for_status()
        return Results(data=r.json())
