

class Product:
    ''' This class search the date in a category'''
    def __init__(self, id_category, liste):
        ''' Return an object of a product get by the API'''
        self.category = id_category
        self.code = liste[0]
        self.name = liste[1]
        self.nutriscore = liste[2]
        self.url = liste[3]
        self.stores = liste[4]
