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

    category = ["legumineuses", "infusions", "cremes", "cereales-et-pommes-de-terre", "boissons-aux-fruits"]

    ''' Instantiation of 5 categories of products '''
    categories = []
    i = 0
    for i in range(5):
        a = Category(category[i])
        categories.append(a)
        i += 1
    # print(categories)

    ''' Request from the API to get the product'''
    # print(categories[0].category)
    products = []
    for x in range(5):
        var = ApiRequest(categories[x])
        liste = var.request()
        # print(liste)

        for i in range(len(liste)):
            ''' Store the product in the Product object'''
            product = Product(x, liste[i])
            products.append(product)

    # # ''' Create database locally to insert API request'''
    # my_db = Database()
    # # #my_db.create_db() # enlever pour que ça marche
    # my_db.create_table()
    my_database = Bdd()

    ''' Save data in the local database with mysql connector'''
    # for c in range(5):
    #     my_database.add_category(category[c])
    #     print(type(categories[c]))
    # try:
    #     for f in range(500): # au dela de 315 list out of index

    #         my_database.add_product(products[f].code, products[f].name, products[f].nutriscore, products[f].url, products[f].stores)
    #         if products[f].code != "":
    #             my_database.add_association(category[products[f].category], products[f].code)
    #         print(category[products[f].category])
    # except IndexError:
    #     print("list index out of range")
    ''' Get the category from the database'''
    tuple_cat = my_database.get_caterory()
    list_cat = list(tuple_cat)
    ''' Show the categories in the database and select category'''
    dict_cat = {}
    i = 1
    for item in list_cat:
        dict_cat[i] = item[0]
        print(i, " - ", item[0])
        i += 1

    user_category = int((input("Please choose a category: ")))
    print((f"You choose {dict_cat[user_category]} category"))

    ''' Display all the products of the category'''
    products_cat = my_database.get_products(dict_cat[user_category])
    #print(products_cat)

    for product in products_cat:
        print(str(product[0]) + ": " + product[3])

    # code_bar = [a_tuple[0] for a_tuple in products_cat]
    # product_name = [a_tuple[3] for a_tuple in products_cat]
    # print(code_bar + product_name)
    # product_dict = {}
    # for item in products_cat:
    #     product_dict[i] = item[0]
    #     print(item[0], " - ", item[3])
    #     i += 1
    # print(product_dict)

    user_product = int(input("please choose a product in the list: "))
    # variable = choix du produit
    ''' Return the product selected and specifically its nutriscore'''
    my_product = my_database.product_selected(user_product)
    print(my_product)
    ''' Find the substitute in the same category with better nutriscore'''
    substitute = my_database.find_substitute(dict_cat[user_category], my_product[0][4])
    print(substitute)

    # Inserer produit a substitute

    ''' Interaction client
    First menu '''
    # menu = Menu()
    # menu.welcome_menu()
