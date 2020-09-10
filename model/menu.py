

class Menu:
    '''This class take all the menu in the program'''

    def __init__(self):
        self.choix = 0
   
    def welcome_menu(self):
        print("          ***Main menu***        ")
        choice = int(input("""
                        1 : Find a substitute
                        2 : See my favorite substitute
                        0 : Quit
        """))
        return choice
