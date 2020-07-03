from dataclasses import *
from typing import List
from typing_extensions import TypedDict


@dataclass
class Price:
    price: list


@dataclass()
class Images:
    thumb_url: str
    small_url: str
    nb_images: int
    url: list
    url_thumb: list
    url_large: list


@dataclass
class Attributes:
    key: str
    value: str
    values: list
    value_label: str
    generic: bool = ""


@dataclass
class Geometry:
    type: str
    coordinates: list


@dataclass
class Feature:
    type: str
    geometry: Geometry
    properties: bool


@dataclass
class Location:
    country_id: str
    region_id: str
    region_name: str
    department_id: str
    department_name: str
    city_label: str
    city: str
    zipcode: str
    lat: float
    lng: float
    source: str
    provider: str
    is_shape: bool
    feature: Feature


@dataclass
class Owner:
    store_id: str
    user_id: str
    type: str
    name: str
    no_salesmen: bool


@dataclass
class Options:
    has_option: bool
    booster: bool
    photosup: bool
    urgent: bool
    gallery: bool
    sub_toplist: bool


@dataclass
class Ads:
    list_id: int
    first_publication_date: str
    expiration_date: str
    index_date: str
    status: str
    category_id: str
    category_name: str
    subject: str
    body: str
    ad_type: str
    url: str
    price: Price
    price_calendar: bool
    images: Images
    attributes: List[Attributes]
    location: Location
    owner: Owner
    options: Options
    has_phone: bool


@dataclass
class AdsShippable(Ads):
    pass


@dataclass
class Response:
    total: int
    total_all: int
    total_pro: int
    total_private: int
    total_active: int
    total_inactive: int
    total_shippable: int
    max_pages: int
    referrer_id: str
    pivot: int
    applied_condition: str
    ads_shippable: List[AdsShippable]
    ads: List[Ads] = field(default_factory={})
