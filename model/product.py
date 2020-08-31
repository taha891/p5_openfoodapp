import requests
from model.request import ApiRequest


class Product:
    ''' This class search the date in a category'''
    def __init__(self, id_category, liste):
        self.category = id_category # + 1 to have the first category = 1
        self.code = liste[0]
        self.name = liste[1]
        self.nutriscore = liste[2]
        self.url = liste[3]
        self.stores = liste[4]
