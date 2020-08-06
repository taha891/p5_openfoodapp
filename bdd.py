import mysql.connector
import requests
from product import Product



class Bdd():

    def __init__(self):
        self.openfood_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="banane35",
            database="openfooddb"
        )

        print(self.openfood_db)

        self.mycursor = self.openfood_db.cursor()

    
    def add_product(self, a, b, c, d, e):
        ''' Method to insert the table products in the database''' # ajouter categorie en paramenetre, insert produit + cat dans la table d'association
        sql = "INSERT INTO products (code_bar, name, nutriscore, url, stores) VALUES (%s, %s, %s, %s, %s)"
        val = (a, b, c, d, e) # e qui est la catégorie ne s'affiche pas
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()
        print(self.mycursor.rowcount, "record inserted.")
        
    def add_category(self, name):
        ''' Method to insert the table category in the database'''
        sql = "INSERT INTO category (name) VALUES (%s)"
        val = (name, )
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()
        print(self.mycursor.rowcount, "record inserted.")

    def add_association(self, cat, prod):
        
        sql = "INSERT INTO association (id_category, id_product) VALUES (%s, %s)"
        val = (cat, prod)
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()
        #print(self.mycursor.rowcount, "record inserted.")
    
    ''' Requête qui affiche tous les produits d'une catégorie choisi 

    SELECT
    '''


    # def substitute(user_category, user_product):
    # ''' this function givea substitute for a product
        
    # SELECT FROM products FROM products WHERE 
    # category = category choisi 
    # nutriscore < nutriscore product
    # CREATE TABLE substitute(idsubstitut INT UNSIGNED NOT NULL AUTO_INCREMENT,  id_product INT, PRIMARY KEY (id))")'''
