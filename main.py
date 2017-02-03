from create_table import CreateTable
from applicant_generator import ApplicantGenerator
from mentor_details import MentorDetails
from applicant_details import ApplicantDetails
from ui import UserInterface


def main():

    chosen_menu = 'q'
    ui = UserInterface()
    ui.clear_sreen()

    while chosen_menu != '0':
        ui.print_main_menu()
        chosen_menu = ui.choose_menu_number()

        if chosen_menu == "1":
            # Create the necessary instances
            create_and_upload_table = CreateTable()
            generate_applicants = ApplicantGenerator("example_data/applicant.txt")
            ui.clear_sreen()
            chosen_administrator_menu = 'q'

            while chosen_administrator_menu != "0":
                ui.print_administrator_menu()
                chosen_administrator_menu = ui.choose_administrator_menu_number()

                if chosen_administrator_menu == "1":
                    try:
                        create_and_upload_table.create_table()
                        print("Tables created successfully")
                    except:
                        print("I can't create tables")

                elif chosen_administrator_menu == "2":
                    try:
                        create_and_upload_table.generate_example_data()
                        print("Data successfully generated and inserted")
                    except:
                        print("I can't Generate example data")

                elif chosen_administrator_menu == "3":
                    try:
                        generate_applicants.generate_applicant()
                        print("Applicants data successfully generated and inserted")
                    except:
                           print("I can't Generate applicants")

                elif chosen_administrator_menu == "4":
                    try:
                        generate_applicants.generate_nearest_school()
                        generate_applicants.generate_interview_for_applicants()

                        print("Interview dates successfully generated to applicants")
                    except:
                        print("Something went wrong. I can't generate interview dates to applicants")

                elif chosen_administrator_menu == "0":
                    ui.clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == "2":
            mentor_details = MentorDetails()
            ui.clear_sreen()
            chosen_mentor_menu = 'q'

            while chosen_mentor_menu != "0":
                ui.print_mentor_menu()
                chosen_mentor_menu = ui.choose_mentor_menu_number()

                if chosen_mentor_menu == '1':
                    try:
                        mentor_details.mentor_date_time()
                    except:
                        print("There is no mentor with that id")

                elif chosen_mentor_menu == '0':
                    ui.clear_sreen()
                    break
                else:
                    print("Wrong menu number was given")

        elif chosen_menu == '3':
            # Create instances
            applicant_detail = ApplicantDetails()
            ui.clear_sreen()
            chosen_applicant_menu = 'q'

            while chosen_applicant_menu != '0':
                ui.print_applicant_menu()
                chosen_applicant_menu = ui.choose_applicant_menu_number()

                if chosen_applicant_menu == '1':
                    try:
                        applicant_detail.interview_details()
                    except:
                        print("There is no application code like that in the database. Please try again")

                elif chosen_applicant_menu == '2':
                    try:
                        applicant_detail.status_details()
                    except:
                        print("There is no application code like that in the database. Please try again")

                elif chosen_applicant_menu == '3':
                    try:
                        applicant_detail.school_details()
                    except:
                        print("There is no application code like that in the database. Please try again")

                elif chosen_applicant_menu == '0':
                    ui.clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == '0':
            ui.print_say_hello()
        else:
            print("Wrong menu number was given")


if __name__ == '__main__':
    main()
