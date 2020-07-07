import mysql.connector
import requests
from product import Product
from category import Category
from request import ApiRequest
from menu import Menu
from bdd import Database

''' créer virtualenv'''

if __name__ == "__main__":
    ''' First menu '''
    # menu = Menu()
    # menu.welcome_menu()

    ''' Get the data from the API'''

    category = ["legumineuses", "infusions", "boissons-aux-fruits",
                "cremes", "plats-prepares-en-conserve"] # verif category

    ''' Instantiation of 5 categories of products '''
    categories = []
    i = 0
    for i in range(5):
        a = Category(category[i])
        categories.append(a)
        i += 1
    
# Ajouter l'instance dans une liste ( append)
    ''' Request from the API to get the product'''
    #print(categories[0].category)
    products = []
    for x in range(4):
        var = ApiRequest(categories[x])  # instance de categorie dans API
        liste = var.request()
        #print(liste)
        ''' Store the product in the Product object'''
       # instancier mes produits depuis la liste
        for i in range(len(liste)):
            product = Product(x, liste[i])
            products.append(product)
            #print(products[i])
            


    ''' Save data in the local database with mysql connector'''
    # my_database = Database()
    # for product in products:
    #     my_database.product_db(product)
    #     f = my_database.product_db(product)
    #     print(f)
    
# Interaction with user
    ''' This menu give the choice to the user '''


    

    
