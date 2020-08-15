from pydantic import BaseModel
from typing import List, Optional


class Attribute(BaseModel):
    key: str
    value: str
    values: List[str]
    value_label: str
    generic: bool
    key_label: str = ""


class Geometry(BaseModel):
    type: str
    coordinates: List[float]


class Feature(BaseModel):
    type: str
    geometry: Geometry

class Location(BaseModel):
    country_id: str
    region_id: str
    region_name: str
    department_id: str
    department_name: str
    city_label: str
    city: str
    zipcode: str
    lat: str
    lng: str
    source: str
    provider: str
    id_shape: bool = False
    feature: Feature
    properties: str = "None"


class Owner(BaseModel):
    store_id: str
    user_id: str
    type: str
    name: str
    no_salesmen: bool

class Options(BaseModel):
    has_option: bool
    booster: bool
    photosup: bool
    urgent: bool
    gallery: bool
    sub_toplist: bool
    
class Image(BaseModel):
    thumb_url: str
    small_url: str
    nb_images: int
    urls: List[str]
    urls_thumb: List[str]
    urls_large: List[str]

class Ad(BaseModel):
    list_id: int
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
    price_calendar: Optional[str] = None
    images: Image
    attributes: List[Attribute]
    location: Location
    owner: Owner
    options: Options
    has_phone: bool

class Response(BaseModel):
    total: int
    total_all: int
    total_private: int
    total_active: int
    total_inactive: int
    total_shippable: int
    max_pages: int
    referrer_id: str
    pivot: str
    ads: List[Ad]
    applied_condition: str