import mysql.connector
from config import HOST, USER, PASSWD
from model.product import Product
from model.category import Category
from model.request import ApiRequest
from model.menu import Menu
from data.bdd import Bdd
from data.database import Database


def init_database():
    ''' Method to create and reset the database '''
    openfood_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
    )

    mycursor = openfood_db.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS openfooddb")
    openfood_db.commit()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS openfooddb")
    openfood_db.commit()

class Application:
    ''' this class includes main function of the app (user interaction)'''
    def __init__(self):
        pass

    def create_db(self):
        ''' create the dabatase and insert values into it for user '''
        category = ["legumineuses", "infusions", "cremes",
                        "cereales-et-pommes-de-terre", "boissons-aux-fruits"]

        #Instantiation of 5 categories of products
        categories = []
        i = 0
        for i in range(5):
            a = Category(category[i])
            categories.append(a)
            i += 1

        #Request from the API to get the product
        products = []
        #Iterate into the 5 category and get 100 products
        for x in range(5):
            var = ApiRequest(categories[x])
            category_list = var.request()

            for i in range(len(category_list)):
                #Store the product in the Product object
                product = Product(x, category_list[i]) # x is the category through iteration
                products.append(product)
        # Create databse object add product to the database the first time
        my_db = Database()
        my_db.create_table()
        my_database = Bdd()

        ''' Create database locally to insert API request'''
        for c in range(5):
            my_database.add_category(category[c])
        try:
            for f in range(500):
                my_database.add_product(products[f].code,
                                        products[f].name,
                                        products[f].nutriscore,
                                        products[f].url,
                                        products[f].stores)
                if products[f].code != "":
                    my_database.add_association(
                        category[products[f].category],
                        products[f].code)
        except IndexError:
            pass

    def find_substitute(self):
        ''' Get the category from the database'''
        my_database = Bdd()
        tuple_cat = my_database.get_caterory()
        list_cat = list(tuple_cat)

        ''' Show categories in the database the user select category'''
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

        for product in products_cat:
            print(str(product[0]) + ": " + product[3])

        user_product = int(input("please choose a product in the list: "))

        ''' Return the product selected especially its nutriscore'''
        my_product = my_database.product_selected(user_product)
        print("You want a substitute for " + my_product[0][3] +
            " and its nutriscore is: " + str(my_product[0][4]))

        ''' Find substitute in same category with better nutriscore'''
        substitute = my_database.find_substitute(
            dict_cat[user_category], my_product[0][4])
        print("Your substitute is " + substitute[0][3] +
            " and nutriscore is " + str(substitute[0][4]))

        ''' Save the product in the favorite list'''
        save_product = int(input("Do you want to save the substitute"
                                " in your list ? Yes: 1     No: 2 "))
        if save_product == 1:
            my_database.save_product(my_product[0][1], substitute[0][1])
        elif save_product == 2:
            print("Try to find another substitute ")
        else:
            print("Please enter 1 or 2 ")

    def favorite_list(self):
        ''' See my favorite list function'''
        my_database = Bdd()
        favorite_list = my_database.see_myfavorite()
        print(favorite_list)

    
