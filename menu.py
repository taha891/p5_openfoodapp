from category import Category

class Menu:
    ''' This class take all the menu in the program'''

    def __init__(self):
        self.choix = 0

    def welcome_menu(self):
        ''' First menu with 2 options : find substitute or see my favorite'''
        choice_accepted = [1, 2]
        try:
            self.choix = int(input("What do you want to do? \n Find a susbtitute for a product: Press 1 \n See your favorite substitute : Tapez 2 \n"))
        # Comment mettre à la ligne sans couper la chaine de caractere
        except TypeError:
            print("La valeur entrée n'est pas un chiffre")

        while self.choix != 1 & self.choix != 2: # is not in choice accepted
            self.choix = int(input("entre une nouvelle valeur"))
        
        if self.choix == 1:
            self.find_substitute()
        elif self.choix == 2:
            self.my_substitute()
        else: print("please choose 1 or 2")
    
    def find_substitute(self):
        ''' This is the menu if the user want to find a new substitute'''
        # Enter a category
        user_category = int(input("Please choose a category"))
        check_answer = 1
        while check_answer:
            
            if user_category is not int and user_category not in range(6): # range(len(categories))
                print("This category is not correct")
                user_category = int(input("Please choose a category"))
            else:
                print(f" the category you choose is {user_category}") # return pour enregistrer la valeur
                #Afficher les produits de la catégorie SELECT * FROM products WHERE id_category = user_category
                check_answer = 0

            
        user_product = (input("Please choose a product"))
        ''' select a product in the list
        get the id of product

        SQL : SELECT * FROM products WHERE nutriscore < nutriscore substitut

        save product


        '''
        


    def my_substitute(self):
        '''The user sees the subsitute he already find and save in his favorite'''
        print("list of substitute")
        pass
#def find_substitute():
    ''' This is the menu if the user want to find a new substitute'''

