import mysql.connector
from config import HOST, USER, PASSWD, DATABASE


class Bdd:

    def __init__(self):
        self.openfood_db = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWD,
            database=DATABASE
        )

        self.mycursor = self.openfood_db.cursor()

    def add_product(self, a, b, c, d, e):
        ''' Method to insert the table products in the database'''
        sql = """INSERT INTO products (code_bar, name, nutriscore,
              url, stores) VALUES (%s, %s, %s, %s, %s)"""
        val = (a, b, c, d, e)
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()

    def add_category(self, name):
        ''' Method to insert the table category in the database'''
        sql = "INSERT INTO category (name) VALUES (%s)"
        val = (name, )
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()

    def add_association(self, cat, prod):
        ''' Method to insert FK from product and category tables'''
        sql = """INSERT INTO association (id_category, id_product)
         VALUES (%s, %s)"""
        val = (cat, prod)
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()

    def get_caterory(self):
        ''' Method to get the category of products '''
        self.mycursor.execute("SELECT * from category ORDER BY name DESC")
        return self.mycursor.fetchall()

    def get_products(self, category):
        ''' Method to get the products from database '''
        sql = """ SELECT association.code_asso, association.id_product,
            association.id_category, products.name, products.nutriscore
            FROM association
            inner join products
            on association.id_product = products.code_bar
            where id_category = %s"""
        val = (category, )
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def product_selected(self, code_asso):
        ''' Get the product selected from user to find substitute'''
        sql = """ SELECT association.code_asso, association.id_product,
            association.id_category, products.name, products.nutriscore
            FROM association
            inner join products
            on association.id_product = products.code_bar
            where code_asso = %s"""
        val = (code_asso, )
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def find_substitute(self, category, nutriscore):
        ''' Method to find substitute of a product selected '''
        sql = """ SELECT association.code_asso, association.id_product,
        association.id_category, products.name, products.nutriscore
        FROM association
        inner join products
        on association.id_product = products.code_bar
        where id_category = %s AND nutriscore < %s LIMIT 1"""
        val = (category, nutriscore)
        self.mycursor.execute(sql, val)
        return self.mycursor.fetchall()

    def save_product(self, product_selected, substitute):
        ''' Method to save substitute in the favorite list '''
        sql = """INSERT into substitute (id_product, substitute)
             VALUES (%s, %s)"""
        val = (product_selected, substitute)
        self.mycursor.execute(sql, val)
        self.openfood_db.commit()

    def see_myfavorite(self):
        ''' Method do display the favorite list of user substitute '''
        self.mycursor.execute(""" SELECT substitute.id_substitute,
        products.name, products.nutriscore, products.stores,
        substitute.substitute
        FROM substitute
        INNER JOIN products
        ON substitute.substitute = products.code_bar""")
        return self.mycursor.fetchall()
