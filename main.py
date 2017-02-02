from applicants_status import applicants_status
from build import BuildTable
from applicants_school import applicants_school
from applicant_interview_details import *

import os
from create_table import CreateTable
from applicant_generator import ApplicantGenerator
from mentor_details import MentorDetails
from applicant_details import ApplicantDetails


def clear_sreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    chosen_menu = 'q'
    clear_sreen()
    while chosen_menu != 0:
        print("\n- - - School system - Main Menu - - -\n-------------------------------------")
        print("1. I am an administrator")
        print("2. I am a mentor")
        print("3. I am an applicant")
        print("0. Exit")
        print("-------------------------------")
        chosen_menu = int(input("Please choose a menu number: "))

        if chosen_menu == 1:
            # Create the necessary instances
            create_and_upload_table = CreateTable()
            generate_applicants = ApplicantGenerator()

            clear_sreen()
            chosen_administrator_menu = 'q'
            while chosen_administrator_menu != 0:
                print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
                print("1. Create tables")
                print("2. Generate data")
                print("3. Generate applicants")
                print("4. Generate interview date to applicants")
                print("0. Exit")
                print("-------------------------------------")
                chosen_administrator_menu = int(input("Please choose an Administrator menu number: "))

                if chosen_administrator_menu == 1:
                    try:
                        create_and_upload_table.create_table()
                        print("Tables created succcessfully")
                    except:
                        print("I can't create tables")

                elif chosen_administrator_menu == 2:
                    try:
                        create_and_upload_table.generate_example_data()
                        print("Data successfully generated and inserted")
                    except:
                        print("I can't Generate example data")

                elif chosen_administrator_menu == 3:
                    try:
                        generate_applicants.generate_applicant("example_data/applicant.txt")
                        print("Applicants data successfully generated and inserted")
                    except:
                        print("I can't Generate applicants")

                elif chosen_administrator_menu == 4:
                    # try:
                    generate_applicants.generate_nearest_school()
                    generate_applicants.generate_interview_for_applicants()

                    print("Interview dates successfully generated to applicants")
                    # except:
                    #    print("Something went wrong. I can't generate interview dates to applicants")

                elif chosen_administrator_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 2:
            mentor_details = MentorDetails()
            clear_sreen()
            chosen_mentor_menu = 'q'
            while chosen_mentor_menu != 0:
                print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
                print("1. Interviews")
                print("0. Exit")
                print("-------------------------------------")
                chosen_mentor_menu = int(input("Please choose a Mentor menu number: "))
                if chosen_mentor_menu == 1:
                    try:
                        mentor_details.mentor_date_time()
                    except:
                        print("There is no mentor with that id")

                elif chosen_mentor_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 3:
            # Create instances
            applicant_detail = ApplicantDetails()

            clear_sreen()
            chosen_applicant_menu = 'q'
            while chosen_applicant_menu != 0:
                print("\n- - - School system - Applicant Menu - - -\n-------------------------------------")
                print("1. Interview details")
                print("2. Status details")
                print("3. School details")
                print("0. Exit")
                print("-------------------------------------")
                chosen_applicant_menu = int(input("Please choose an Applicant menu number: "))

                if chosen_applicant_menu == 1:
                    applicant_detail.interview_details()

                elif chosen_applicant_menu == 2:
                    try:
                        applicant_detail.status_details()
                        # print("Your application status is", status)
                    except:
                        print("There is no application code like that in the database. Please try again")

                elif chosen_applicant_menu == 3:
                    try:
                        applicant_detail.school_details()
                    except:
                        print("There is no application code like that in the database. Please try again")
                elif chosen_applicant_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 0:
            print("\n------------------------------------------------------------")
            print("| Thanks for choosing Codeorgo Software! See you next time!|")
            print("------------------------------------------------------------")
        else:
            print("Wrong menu number was given")


main()
