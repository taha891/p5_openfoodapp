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

    category = ["legumineuses", "infusions",
                "boissons-aux-fruits", "cereales-et-pommes-de-terre", "cremes"]
    

    ''' Instantiation of 5 categories of products '''
    categories = []
    i = 0
    for i in range(5):
        a = Category(category[i])
        categories.append(a)
        i += 1
    #print(categories)
    
    ''' Request from the API to get the product'''
    #print(categories[0].category)
    products = []
    for x in range(5):
        var = ApiRequest(categories[x])
        liste = var.request()
        print(liste)

        for i in range(len(liste)):
        #''' Store the product in the Product object'''
            product = Product(x, liste[i])
            products.append(product)

    ''' Create database locally to insert API request'''
    my_db = Database()
    #my_db.create_db() # enlever pour que ça marche
    my_db.create_table() 
    my_database = Bdd()

    ''' Save data in the local database with mysql connector'''
    for c in range(5):
        my_database.add_category(category[c])
        #print(type(categories[c]))
    for f in range(315): # au dela de 315 list out of index
        
        my_database.add_product(products[f].code, products[f].name, products[f].nutriscore, products[f].url, products[f].stores)    
        if products[f].code != "":
            my_database.add_association(category[products[f].category], products[f].code)
        print(category[products[f].category])

    # def find_cat(x):
    #     user_category = int(input("Please choose a category: "))
    #     category_name = x[user_category]
    #     print(category_name)
    # 
    # find_cat(category)

    
        # Comment éviter les doublons pour les catégories ? Distinct marche avec tout select, i:ppnsert ?

    ''' Interaction client'''

    ''' First menu '''
    # menu = Menu()
    # menu.welcome_menu()
