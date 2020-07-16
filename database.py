import mysql.connector
import requests
from bdd import Bdd

openfood_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="banane35",
    database="openfooddb"
)

print(openfood_db)

mycursor = openfood_db.cursor()
class Database():

    def __init__(self):
        pass
    
    mycursor = openfood_db.cursor()

    

    ''' Create table for the products'''
    #mycursor.execute("CREATE TABLE products (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(255), nutriscore VARCHAR(1), url VARCHAR(250), stores LONGTEXT, PRIMARY KEY (id))")
    mycursor.execute("DELETE FROM products")

    openfood_db.commit()

    ''' Create table for the category'''
    #mycursor.execute("CREATE TABLE category(id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(255), PRIMARY KEY (id))")
    #mycursor.execute("DELETE FROM category")
    openfood_db.commit()

    def reset(self):
        '''Reset and clean all'''
    mycursor.execute("DROP TABLE IF EXISTS products, category")
    mycursor.execute("CREATE TABLE products (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(255), nutriscore VARCHAR(1), url VARCHAR(250), stores LONGTEXT, PRIMARY KEY (id))")
    mycursor.execute("CREATE TABLE category(id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(255), PRIMARY KEY (id))")
    openfood_db.commit()
