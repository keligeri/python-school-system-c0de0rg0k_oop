import os


class UserInterface:
    """This class contain the necessary print methods"""

    def clear_sreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def choose_menu_number(self):
        chosen_menu = input("Please choose a menu number: ")
        return chosen_menu

    def choose_administrator_menu_number(self):
        chosen_administrator_menu = input("Please choose an Administrator menu number: ")
        return chosen_administrator_menu

    def choose_mentor_menu_number(self):
        chosen_mentor_menu = input("Please choose an Administrator menu number: ")
        return chosen_mentor_menu

    def choose_applicant_menu_number(self):
        chosen_applicant_menu = input("Please choose an Administrator menu number: ")
        return chosen_applicant_menu

    def print_main_menu(self):
        print("\n- - - School system - Main Menu - - -\n-------------------------------------")
        print("1. I am an administrator")
        print("2. I am a mentor")
        print("3. I am an applicant")
        print("0. Exit")
        print("-------------------------------")

    def print_administrator_menu(self):
        print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
        print("1. Create tables")
        print("2. Generate data")
        print("3. Generate applicants")
        print("4. Generate interview date to applicants")
        print("0. Exit")
        print("-------------------------------------")

    def print_mentor_menu(self):
        print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
        print("1. Interviews")
        print("0. Exit")
        print("-------------------------------------")

    def print_applicant_menu(self):
        print("\n- - - School system - Applicant Menu - - -\n-------------------------------------")
        print("1. Interview details")
        print("2. Status details")
        print("3. School details")
        print("0. Exit")
        print("-------------------------------------")

    def print_say_hello(self):
        print("\n------------------------------------------------------------")
        print("| Thanks for choosing Codeorgo Software! See you next time!|")
        print("------------------------------------------------------------")
