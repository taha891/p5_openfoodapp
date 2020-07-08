import requests
from pprint import pprint
import json
from request import ApiRequest


class Product:
    ''' This class search the date in a category'''
    def __init__(self, id_category, liste):
        self.category = id_category
        self.name = liste[0]
        self.nutriscore = liste[1]
        self.url = liste[2]
        self.stores = liste[3]
        #print(self.name)
        # utiliser @property pour faire de la methode un attribut
        # Faire un split tous les 4 élements

    def add_product(self):
        return(self.name)
        return(self.nutriscore)
        return(self.url)
        return(self.stores)    
    
    def save_product(self):
        ''' This method save the data of the product '''
        pass
