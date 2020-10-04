import sys
from model.menu import Menu
from data.functions import init_database, Application


def main():
    ''' function of the program'''
    program_loop = 1
    while program_loop:
        app = Application()
        debut = int(input("1 : Initialise database  "
                          "2 :Use current database  "))
        if debut == 1:
            init_database()
            app.create_db()
        elif debut == 2:
            print("This is your dabatase  ")
        else:
            print("please press 1 or 2  ")

        # Main menu the user can choose what he wants to do
        menu = Menu()
        choice = menu.welcome_menu()

        if choice == 1:
            app.find_substitute()
        elif choice == 2:
            app.favorite_list()
        elif choice == 0:
            program_loop = 0
            sys.exit()
        else:
            print("Please Enter a correct Value : 0, 1 or 2")

        quit_program = input("Do you want to quit the program ?"
                             "Yes : 1     No : 2      ")
        if quit_program == 1:
            program_loop = 0
            sys.exit()


if __name__ == "__main__":
    # execute only if run as a script
    main()
