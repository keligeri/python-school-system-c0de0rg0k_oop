import os


class UserInterface:
    """This class contain the necessary print methods, and inputs method for the main"""

    def clear_sreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def choose_menu_number(self):
        chosen_menu = input("Please choose a menu number: ")
        return chosen_menu

    def choose_submenu_number(self, role):
        chosen_submenu = input("Please choose an {0} menu number: ".format(role))
        return chosen_submenu

    def show_main_menu(self):
        print("\n- - - School system - Main Menu - - -\n-------------------------------------")
        print("1. I am an administrator")
        print("2. I am a mentor")
        print("3. I am an applicant")
        print("0. Exit")
        print("-------------------------------")

    def show_administrator_menu(self):
        print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
        print("1. Create tables")
        print("2. Generate data")
        print("3. Generate applicants")
        print("4. Generate interview date to applicants")
        print("0. Exit")
        print("-------------------------------------")

    def show_mentor_menu(self):
        print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
        print("1. Interviews")
        print("0. Exit")
        print("-------------------------------------")

    def show_applicant_menu(self):
        print("\n- - - School system - Applicant Menu - - -\n-------------------------------------")
        print("1. Interview details")
        print("2. Status details")
        print("3. School details")
        print("0. Exit")
        print("-------------------------------------")

    def show_say_hello(self):
        print("\n------------------------------------------------------------")
        print("| Thanks for choosing Codeorgo Software! See you next time!|")
        print("------------------------------------------------------------")

    def show_generetad_data(self, data_type, inserted_needed=True):
        if inserted_needed is True:
            print("{0} successfully generated and inserted!".format(data_type))
        else:
            print("{0} successfully generated!".format(data_type))

    def show_cant_generate_data(self, data_type):
        print("Something went wrong. I can't generate {0} :(".format(data_type))

    def show_cant_found(self, identification):
        print("There is no {0} like that in the database. Please try again".format(identification))

    def show_wrong_number(self):
        print("Wrong menu number was given")
