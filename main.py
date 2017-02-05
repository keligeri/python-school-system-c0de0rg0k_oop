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
        ui.show_main_menu()
        chosen_menu = ui.choose_menu_number()

        if chosen_menu == "1":
            # Create the necessary instances
            create_and_upload_table = CreateTable()
            generate_applicants = ApplicantGenerator("example_data/applicant.txt")
            ui.clear_sreen()
            chosen_administrator_menu = 'q'

            while chosen_administrator_menu != "0":
                ui.show_administrator_menu()
                chosen_administrator_menu = ui.choose_submenu_number("Administrator")

                if chosen_administrator_menu == "1":
                    try:
                        create_and_upload_table.create_table()
                        ui.show_generetad_data("Tables", False)
                    except:
                        ui.show_cant_generate_data("tables")

                elif chosen_administrator_menu == "2":
                    try:
                        create_and_upload_table.generate_example_data()
                        ui.show_generetad_data("Example data")
                    except:
                        ui.show_cant_generate_data("example data")

                elif chosen_administrator_menu == "3":
                    try:
                        generate_applicants.generate_applicant()
                        ui.show_generetad_data("Applicants data")
                    except:
                        ui.show_cant_generate_data("applicants data")

                elif chosen_administrator_menu == "4":
                    try:
                        generate_applicants.generate_nearest_school()
                        generate_applicants.generate_interview_for_applicants()
                        ui.show_generetad_data("Interview dates")
                    except:
                        ui.show_cant_generate_data("interviews date")

                elif chosen_administrator_menu == "0":
                    ui.clear_sreen()
                    break

                else:
                    ui.show_wrong_number()

        elif chosen_menu == "2":
            mentor_details = MentorDetails()
            ui.clear_sreen()
            chosen_mentor_menu = 'q'

            while chosen_mentor_menu != "0":
                ui.show_mentor_menu()
                chosen_mentor_menu = ui.choose_submenu_number("Mentor")

                if chosen_mentor_menu == '1':
                    try:
                        mentor_details.mentor_date_time()
                    except:
                        ui.show_cant_found("mentor id")

                elif chosen_mentor_menu == '0':
                    ui.clear_sreen()
                    break
                else:
                    ui.show_wrong_number()

        elif chosen_menu == '3':
            # Create instances
            applicant_detail = ApplicantDetails()
            ui.clear_sreen()
            chosen_applicant_menu = 'q'

            while chosen_applicant_menu != '0':
                ui.show_applicant_menu()
                chosen_applicant_menu = ui.choose_submenu_number("Applicant")

                if chosen_applicant_menu == '1':
                    try:
                        applicant_detail.interview_details()
                    except:
                        ui.show_cant_found("applicant code")

                elif chosen_applicant_menu == '2':
                    try:
                        applicant_detail.status_details()
                    except:
                        ui.show_cant_found("applicant code")

                elif chosen_applicant_menu == '3':
                    try:
                        applicant_detail.school_details()
                    except:
                        ui.show_cant_found("applicant code")

                elif chosen_applicant_menu == '0':
                    ui.clear_sreen()
                    break

                else:
                    ui.show_wrong_number()

        elif chosen_menu == '0':
            ui.show_say_hello()
        else:
            ui.show_wrong_number()

if __name__ == '__main__':
    main()
