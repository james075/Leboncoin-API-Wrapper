from cloudscraper import create_scraper
from dataclasses import *
import json
from typing_extensions import TypedDict


def get_category(query):
    url = f"https://api.leboncoin.fr/api/parrot/v1/complete?q={query.replace(' ', '%20')}"
    requests = create_scraper(browser="chrome")
    return str(requests.get(url).json()[0]["cat_id"])


def set_region(region_name):
    with open("Ressources/regions.json") as file:
        data_regions = json.load(file)

    for region in data_regions:
        if region["channel"] == region_name:
            return region["id"]
    else:
        return " "


def set_dept(dept_name):
    with open("Ressources/departements.json") as file:
        data_departements = json.load(file)

    for dept in data_departements:
        if dept["channel"] == dept_name:
            return dept["id"]
    else:
        return " "


@dataclass
class Category:
    """Data Class to build the payload"""
    id: str

    @property
    def to_json(self):
        return json.dumps(asdict(self))


@dataclass
class Enums:
    ad_type: list

    @property
    def to_json(self):
        return json.dumps(asdict(self))


@dataclass
class Keywords:
    text: str

    @property
    def to_json(self):
        return json.dumps(asdict(self), indent=4)


@dataclass
class Area:
    lat: float
    lng: float
    radius: int

    @property
    def to_json(self):
        return json.dumps(asdict(self))


@dataclass
class Locale(TypedDict):
    area: Area
    region: str
    department: str


@dataclass
class Ranges:
    pass

    @property
    def to_json(self):
        return json.dumps({})


@dataclass
class Filters:
    category: Category
    enums: Enums
    location: Locale
    keywords: Keywords
    ranges: Ranges

    @property
    def to_json(self):
        return json.dumps(asdict(self), indent=4)


@dataclass
class Payload:
    limit: int
    limit_alu: int
    filters: Filters

    @property
    def to_json(self):
        return json.dumps(asdict(self), indent=4)

    @property
    def to_dict(self):
        return asdict(self)
