from create_table import CreateTable
from applicant_generator import ApplicantGenerator
from mentor_details import MentorDetails
from applicant_details import ApplicantDetails
from ui import UserInterface

class Main:

    ui = UserInterface()

    @classmethod
    def main(cls):
        chosen_menu = 'q'
        cls.ui.clear_sreen()

        while chosen_menu != '0':
            cls.ui.show_main_menu()
            chosen_menu = cls.ui.choose_menu_number()
            if chosen_menu == '1':
                cls.menu_1()
            elif chosen_menu == '2':
                cls.menu_2()
            elif chosen_menu == '3':
                cls.menu_3()
            elif chosen_menu == '0':
                cls.ui.show_say_hello()
            else:
                cls.show_wrong_number()

    @classmethod
    def menu_1(cls):
        # Create the necessary instances
        create_and_upload_table = CreateTable()
        generate_applicants = ApplicantGenerator("example_data/applicant.txt")
        cls.ui.clear_sreen()
        chosen_administrator_menu = 'q'

        while chosen_administrator_menu != "0":
            cls.ui.show_administrator_menu()
            chosen_administrator_menu = cls.ui.choose_submenu_number("Administrator")

            if chosen_administrator_menu == "1":
                try:
                    create_and_upload_table.create_table()
                    cls.ui.show_generetad_data("Tables", False)
                except:
                    cls.ui.show_cant_generate_data("tables")

            elif chosen_administrator_menu == "2":
                try:
                    create_and_upload_table.generate_example_data()
                    cls.ui.show_generetad_data("Example data")
                except:
                    cls.ui.show_cant_generate_data("example data")

            elif chosen_administrator_menu == "3":
                try:
                    generate_applicants.generate_applicant()
                    cls.ui.show_generetad_data("Applicants data")
                except:
                    cls.ui.show_cant_generate_data("applicants data")

            elif chosen_administrator_menu == "4":
                try:
                    generate_applicants.generate_nearest_school()
                    generate_applicants.generate_interview_for_applicants()
                    cls.ui.show_generetad_data("Interview dates")
                except:
                    cls.ui.show_cant_generate_data("interviews date")

            elif chosen_administrator_menu == "0":
                cls.ui.clear_sreen()
                break

            else:
                cls.ui.show_wrong_number()

    @classmethod
    def menu_2(cls):
        mentor_details = MentorDetails()
        cls.ui.clear_sreen()
        chosen_mentor_menu = 'q'

        while chosen_mentor_menu != "0":
            cls.ui.show_mentor_menu()
            chosen_mentor_menu = cls.ui.choose_submenu_number("Mentor")

            if chosen_mentor_menu == '1':
                try:
                    mentor_details.mentor_date_time()
                except:
                    cls.ui.show_cant_found("mentor id")

            elif chosen_mentor_menu == '0':
                cls.ui.clear_sreen()
                break
            else:
                cls.ui.show_wrong_number()

    @classmethod
    def menu_3(cls):
        # Create instances
        applicant_detail = ApplicantDetails()
        cls.ui.clear_sreen()
        chosen_applicant_menu = 'q'

        while chosen_applicant_menu != '0':
            cls.ui.show_applicant_menu()
            chosen_applicant_menu = cls.ui.choose_submenu_number("Applicant")

            if chosen_applicant_menu == '1':
                try:
                    applicant_detail.interview_details()
                except:
                    cls.ui.show_cant_found("applicant code")

            elif chosen_applicant_menu == '2':
                try:
                    applicant_detail.status_details()
                except:
                    cls.ui.show_cant_found("applicant code")

            elif chosen_applicant_menu == '3':
                try:
                    applicant_detail.school_details()
                except:
                    cls.ui.show_cant_found("applicant code")

            elif chosen_applicant_menu == '0':
                cls.ui.clear_sreen()
                break

            else:
                cls.ui.show_wrong_number()


if __name__ == '__main__':
    Main.main()
