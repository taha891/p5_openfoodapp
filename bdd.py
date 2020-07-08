import mysql.connector
import requests
from product import Product

# fonction en prarametre product()
# 1 fonction par table
# 1 

openfood_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="banane35",
    database="openfooddb"
)

print(openfood_db)

mycursor = openfood_db.cursor()
class Database:

    def __init__(self, product):
        self.product = product
        self.category = 0
        self.name = 0
        self.nutriscore = 0
        self.url = 0
        self.stores = 0

    ''' Function for the table products'''
    def product_db(self, name, nutriscore, url, stores):
        # mycursor.execute("DROP TABLE products")
        # openfood_db.commit()
        ''' Create table for the products'''

        #mycursor.execute("CREATE TABLE products(id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(45), nutriscore VARCHAR(1), url VARCHAR(100), store VARCHAR(45), PRIMARY KEY (id))")
        # Comment prendre info depuis l'objet product
        sql = "INSERT INTO products (name, nutriscore, url, store) VALUES (%s, %s, %s, %s)"
        val = (self.name, self.nutriscore, self.url, self.stores) # Comment aller chercher les valeurs de la lsite
        mycursor.execute(sql, val)
        openfood_db.commit()
        print(mycursor.rowcount, "record inserted.")

    def category_db(self):
        ''' Create table for the category'''
        mycursor.execute("CREATE TABLE category(id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(45), PRIMARY KEY (id))")


        openfood_db.commit()
        print(mycursor.rowcount, "record inserted.")
    # Plusieurs commit pour les créations de table ?

    for x in mycursor:
        print(x)


    ''' Requete qui enregistre les produits dans la base de données

    INSERT '''



    ''' Requête qui affiche tous les produits d'une catégorie choisi 

    SELECT
    '''


    ''' Requête qui cherche le substitut '''
