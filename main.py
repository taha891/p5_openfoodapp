import mysql.connector
import requests
from product import Product
from category import Category
from request import ApiRequest
from menu import Menu
from bdd import Bdd
from database import Database

''' créer virtualenv'''

if __name__ == "__main__":
    
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
    for x in range(5):
        var = ApiRequest(categories[x])  # instance de categorie dans API
        liste = var.request()
     
        ''' Store the product in the Product object'''
       # instancier mes produits depuis la liste
        for i in range(len(liste)):
            product = Product(x, liste[i])
            products.append(product)

    print(products[0].name)       

    ''' Save data in the local database with mysql connector'''
    my_db = Database()
    my_db.create_table()  
    my_database = Bdd()
    #my_database = Database((products, category)) # Ajouter les autres methodes : association et substitut
    for f in range(307):
        my_database.add_product(products[f].name, products[f].nutriscore, products[f].url, products[f].stores)

    for c in range(5):
        my_database.add_category(str(categories[c]))
    
    my_database.add_association()
        # Comment éviter les doublons pour les catégories ? Distinct marche avec tout select, insert ?

    ''' Interaction client'''

    ''' First menu '''
    # menu = Menu()
    # menu.welcome_menu()

    
