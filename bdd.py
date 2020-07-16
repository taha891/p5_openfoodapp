import mysql.connector
import requests
from product import Product

openfood_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="banane35",
    database="openfooddb"
)

print(openfood_db)

mycursor = openfood_db.cursor()

class Bdd():

    def __init__(self):
        pass

    ''' Function for the table products'''
    def add_product(self, a, b, c, d):
        # mycursor.execute("DROP TABLE products")
        # openfood_db.commit()
        sql = "INSERT INTO products (name, nutriscore, url, stores) VALUES (%s, %s, %s, %s)"
        val = (a, b, c, d)
        mycursor.execute(sql, val)
        openfood_db.commit()
        print(mycursor.rowcount, "record inserted.")

    def add_category(self, name):
        
        sql = "INSERT INTO category (name) VALUES (%s)"
        val = (name, )
        mycursor.execute(sql, val)
        openfood_db.commit()
        print(mycursor.rowcount, "record inserted.")
    # Plusieurs commit pour les créations de table ?


    
    ''' Requête qui affiche tous les produits d'une catégorie choisi 

    SELECT
    '''


    ''' Requête qui cherche le substitut '''
