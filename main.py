import mysql.connector
import requests
from product import Product
from category import Category
from request import ApiRequest

''' créer virtualenv'''

if __name__ == "__main__":

    ''' Get the data from the API'''

    category = ["legumineuses", "infusions", "boissons-aux-fruits",
                "cremes", "plats-prepares-en-conserve"]

    ''' Instantiation of 5 categories of products '''
    categories = []
    i = 0
    for i in range(5):
        a = Category(category[i])
        categories.append(a)
        i += 1
    
# Ajouter l'instance dans une liste ( append)
    ''' Request from the API to get the product'''
    #print(categories[0].category)
    for x in range(5):
        var = ApiRequest(categories[x]) # instance de categorie dans API 
        liste = var.request()
        print(liste)

   # instancier mes produits depuis la liste
    ''' Utilisation de la liste'''
    # indice de 0 à 3 : 0 name, 1 nutriscore, 2 url, 3 magasin
    # faire un split à 3 pour reinitialiser le i

    '''produit : prend en paramètre unpacking ( prendre en paramètre une liste ou dictionnaire)'''
   


    #x = var.request())
    # On récupère les infos nécéssaires : self.name, self.nutriscore, self.url_prod, self.stores
    
   

    ''' Store the product in the Product object'''
    prod_cat = Product(liste)
    print(prod_cat)



    ''' Save data in the local database with mysql connector'''

    
# Interaction with user
    ''' This menu give the choice to the user '''


    

    
