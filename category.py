class Category:
    ''' This class create, use and check the category of a product'''

    def __init__(self, category):
        self.category = category #self.name = category
        
        # Ok le constructeur ?
        # Liste ou dictionnaire pour les catégories ?

    def __str__(self):
        return "The category chosen is {}".format(self.category)

    
    def client_category(self):
        ''' return the choice of the client and give the products of it'''
        pass

    def create_list(self, category):
        '''This method should create a list of the products in the chosen category'''
        pass