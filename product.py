import requests
from pprint import pprint
import json
from request import ApiRequest


class Product:
    ''' This class search the date in a category'''
    def __init__(self, *liste_prod):
        
        self.liste_prod = liste_prod
        # utiliser @property pour faire de la methode un attribut
        # Faire un split tous les 4 élements

    def add_product(self):
        # self.name = name
        # self.nutriscore = nutriscore
        # self.url = url
        # self.stores = stores
        # self.name = liste_prod[0]
        print(self.name)
        #return(self.unique_scans_n, self.name, self.nutriscore)
            
    
    def save_product(self):
        ''' This method save the data of the product '''
        print(self.liste_prod)
        pass
