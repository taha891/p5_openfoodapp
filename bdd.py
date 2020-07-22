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

    
    def add_product(self, a, b, c, d):
        ''' Function for the table products'''
        sql = "INSERT INTO products (name, nutriscore, url, stores) VALUES (%s, %s, %s, %s)"
        val = (a, b, c, d)
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()
        print(self.mycursor.rowcount, "record inserted.")
        # return category
    def add_category(self, name):
        
        sql = "INSERT INTO category (name) VALUES (%s)"
        val = (name, )
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()
        print(self.mycursor.rowcount, "record inserted.")

    def add_association(self):
        self.mycursor.execute("ALTER TABLE association" 
        "ADD CONSTRAINT fk_product_category"
        "FOREIGN KEY (id_product) REFERENCES products(id_product)"
        "FOREIGN KEY (id_category) REFERENCES category(id_category)")
        self.openfood_db.commit()
        print(self.mycursor.rowcount, "record inserted.")
    # Plusieurs commit pour les créations de table ?


    
    ''' Requête qui affiche tous les produits d'une catégorie choisi 

    SELECT
    '''


    ''' Requête qui cherche le substitut '''
