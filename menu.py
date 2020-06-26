from category import Category

class Menu:
    ''' This class take all the menu in the program'''

    def __init__(self):
        pass

    def welcome_menu(self):
        ''' First menu with 2 options : find substitute or see my favorite'''
        choice_accepted = [1, 2]
        try:
            choix = int(input("Que voulez-vous faire? \n Trouver un susbtitut pour un aliment: Tapez 1 \n Retrouver mes aliments substitués : Tapez 2 \n"))
        except TypeError:
            print("La valeur entrée n'est pas un chiffre")

        while choix != 1 & choix != 2:
            choix = int(input("entre une nouvelle valeur"))
    
    def find_substitute(self):
        ''' This is the menu if the user want to find a new substitute'''
        pass


    def my_substitute(self):
        '''The user sees the subsitute he already find and save in his favorite'''
        pass
