import mysql.connector
import requests
from bdd import Bdd

class Database():

    def __init__(self):
        self.openfood_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="banane35",
            database="openfooddb"
        )

        print(self.openfood_db)

        self.mycursor = self.openfood_db.cursor()
        
   

    ''' Create table for the products and categories'''
    def create_table(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS products ("
            "id_product INT UNSIGNED NOT NULL AUTO_INCREMENT,"
            "name VARCHAR(255),"
            "nutriscore VARCHAR(1),"
            "url VARCHAR(250)," 
            "stores LONGTEXT,"
            "PRIMARY KEY (id_product))")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS category ("
        "id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,"
        "name VARCHAR(255),"
        "PRIMARY KEY (id_category))")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS association ("
        "code_asso INT UNSIGNED NOT NULL AUTO_INCREMENT,"
        "id_product INT UNSIGNED NOT NULL,"
        "id_category SMALLINT UNSIGNED NOT NULL,"
        "PRIMARY KEY(code_asso)," 
        "INDEX (id_product),"
        "INDEX (id_category),"
        "CONSTRAINT fk_product_category"
        "   FOREIGN KEY(id_product) REFERENCES products(id_product),"
        "   FOREIGN KEY(id_category) REFERENCES category(id_category))")
        #mycursor.execute("DELETE FROM products")
        self.openfood_db.commit()
        # ALTER TABLE association ADD FOREIGN KEY (id_product) REFERENCES products(id_product)

    # def create_db(self):
    #     self.mycursor.execute("CREATE DATABASE openfooddb")
    #     self.openfood_db.commit()
    
    # def reset(self):
    #     '''Reset and clean all'''
    #     self.req = """
    # DROP DATABASE IF EXISTS opendooddb;
    # CREATE DATABASE openfooddb;
    # USE openfooddb;   
    # CREATE TABLE IF NOT EXISTS products (
    #     id_product INT UNSIGNED NOT NULL AUTO_INCREMENT,
    #     name VARCHAR(255),
    #     nutriscore VARCHAR(1),
    #     url VARCHAR(250), stores LONGTEXT, PRIMARY KEY (id));
    # CREATE TABLE IF NOT EXISTS category(
    #     id_category SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    #     name VARCHAR(255), 
    #     PRIMARY KEY (id));
    # CREATE TABLE association (
    #     code_asso INT UNSIGNED NOT NULL AUTO_INCREMENT, 
    #     id_product INT NOT NULL,
    #     id_category SMALLINT NOT NULL,
    
    #     PRIMARY KEY(code_asso),
    #     INDEX (id_product)
    #     INDEX (id_category)

    #     FOREIGN KEY(id_product)
    #         REFERENCES products(id_product)

    #     FOREIGN KEY(id_category)
    #         REFERENCES products(id_category)"""
    
    #     self.mycursor.execute(self.req, multi=True)
    #     self.openfood_db.commit()


    def association(self):
        ''' 
        Pour chaque produit obtenir id produit et id category
        
        
        '''
        pass

    def substitute():
        ''' this function givea substitute for a product
        
        SELECT FROM products WHERE 
        category = category choisi 
        nutriscore < nutriscore product

        CREATE TABLE substitute(idsubstitut INT UNSIGNED NOT NULL AUTO_INCREMENT,  id_product INT, PRIMARY KEY (id))")
        '''
        pass
