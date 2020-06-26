import mysql.connector
import requests
from product import Product

openfood_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="banane35",
    database = "openfooddb"
)

print(openfood_db)

mycursor = openfood_db.cursor()

mycursor.execute("DROP TABLE products")
openfood_db.commit()

mycursor.execute("CREATE TABLE products(id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, name VARCHAR(45), nutriscore VARCHAR(1), url VARCHAR(100), store VARCHAR(45), PRIMARY KEY (id))")
# Comment prendre info depuis l'objet product
sql = "INSERT INTO products (name, nutriscore, url, store) VALUES (%s, %s, %s, %s)"
val = (Product, Product.nutriscore, Product.url, Product.store) # Comment aller chercher les valeurs de la lsite
mycursor.execute(sql, val)

openfood_db.commit()
print(mycursor.rowcount, "record inserted.")

for x in mycursor:
    print(x)


''' Requete qui enregistre les produits dans la base de données

INSERT '''



''' Requête qui affiche tous les produits d'une catégorie choisi 

SELECT
'''


''' Requête qui cherche le substitut ''''