import mysql.connector
import requests
from product import Product
from category import Category
from request import ApiRequest


if __name__ == "__main__":

    ''' Get the data from the API'''

    category = ["legumineuses", "infusions", "boissons-aux-fruits",
                "cremes", "plats-prepares-en-conserve"]
    ''' Instantiation of 5 categories of products '''
    i = 0
    for i in range(5):
        a = Category(category[i])
        print(a)
        i += 1

    ''' Request from the API to get the product'''
    var = ApiRequest(category[0])
    print(var)
    #print(var.request())

    print(var.liste_prod)
    #x = var.request())
    # On récupère les infos nécéssaires : self.name, self.nutriscore, self.url_prod, self.stores

    prod_list = list(var.request)
    #print(prod_list)
    
    # prod = Product(var.products)
    # prod.add_product()
    # print(prod)

    ''' Store the product in the Product object'''


    # first_cat = Product("legumineuses")  # Dataselector(i)
    # first_cat.request("legumineuses")
    # first_cat.add_product()
    # first_cat.save_product()

    # second_cat = Product("infusions")
    # second_cat.request("infusions")
    # second_cat.add_product()
    
    # Comment éviter la redondance pour l'instanciation des 5 catégories



    ''' Save data in the local database with mysql connector'''

    



# Interaction with user
    ''' This menu give the choice to the user '''


    

    
