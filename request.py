import mysql.connector
import requests
from pprint import pprint

class ApiRequest:

    def __init__(self, category):
        self.category = category.category
        self.url = f"https://fr.openfoodfacts.org/categorie/{self.category}.json"
        self.result = requests.get(self.url)
        self.liste_prod = []
        

    def request(self):
        payload = {"search_terms": self.category,
                   "search_tag": "categorie",
                   "sort_by": "unique_scans_n",
                   "page_size": 100,
                   "json": 1}

        self.request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
        self.json_object = self.request.json()
        #pprint(self.json_object)
        self.products = self.json_object["products"]
        
        for product in self.products:
            self.name = product.get("product_name", "no information")
            self.unique_scans_n = product.get("unique_scans_n", "not available") # Peut être enlver
            self.nutriscore = product.get("nutriscore_grade", "e")
            self.url_prod = product.get("url", "no information")
            self.stores = product.get("stores", "no information")
            self.liste_prod.append([self.name, self.nutriscore, self.url, self.stores])
        return self.liste_prod