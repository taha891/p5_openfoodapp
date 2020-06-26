import requests
from pprint import pprint
import json
from request import ApiRequest


class Product(ApiRequest):
    ''' This class search the date in a category'''
    def __init__(self, name, nutriscore, url, stores):
        #ApiRequest.__init__(self, category)
        self.name = name
        self.nutriscore = nutriscore
        self.url = url
        self.stores = stores
        # utiliser @property pour faire de la methode un attribut
        # Comment je peux mettre ces info dans la classe category sans enlever le reste 
        # et appeler la categorie pour la requete url


    def add_product(self):
        # self.liste_prod = []
        for product in self.products:
            self.name = product.get("product_name", "no information")
            self.unique_scans_n = product.get("unique_scans_n", "not available")
            self.nutriscore = product.get("nutriscore_grade", "e")
            self.url_prod = product.get("url", "no information")
            self.stores = product.get("stores", "no information")
            print(self.unique_scans_n, self.name, self.nutriscore, self.url_prod, self.stores)
            # self.liste_prod.extend([self.name, self.nutriscore, self.url, self.stores])
            # print(self.liste_prod)
            #return(self.unique_scans_n, self.name, self.nutriscore)
            
    
    def save_product(self):
        ''' This method save the data of the product '''
        
        print(self.liste_prod)
        pass
        #return self.object.show_product(self)




