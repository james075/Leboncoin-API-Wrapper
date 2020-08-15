import json
from cloudscraper import create_scraper


class Payload:
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
        
        with open("Ressources/regions.json", "r") as json_file:
            self.region_data = json.load(json_file)
        with open("Ressources/departements.json", "r") as json_file:
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

    def _get_category(self, query):
        url = f"https://api.leboncoin.fr/api/parrot/v1/complete?q={query.replace(' ', '%20')}"
        requests = create_scraper(browser="chrome")
        return str(requests.get(url).json()[0]["cat_id"])
    
    def searchFor(self, query, autoCatgory=True):
        self._payload["filters"]["keywords"]["text"] = query
        if autoCatgory:
            self._payload["filters"]["category"]["id"] = str(self._get_category(query))
    
    def setCategory(self, query):
        self._payload["filters"]["category"]["id"] = self._get_category(query)
        
    def build(self):
        return json.dumps(self._payload)
