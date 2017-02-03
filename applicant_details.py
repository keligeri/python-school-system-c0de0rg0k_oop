from models import *


class ApplicantDetails:
    """ This class can print out the applications interview-, status- and school-details,
        based on the application code """

    def __init__(self):
        self.applicant_code = ""

    def interview_details(self):
        self.__input_applicant_code()
        self.__check_applicant_code()
        self.__print_interview_details()

    def status_details(self):
        self.__input_applicant_code()
        self.__check_applicant_code()
        self.__print_status_details()

    def school_details(self):
        self.__input_applicant_code()
        self.__check_applicant_code()
        self.__print_school_details()

    def __input_applicant_code(self):
        self.applicant_code = int(input("Please tell me your application code: "))

    def __check_applicant_code(self):
        applications = Applicant.select().where(Applicant.applicant_code == self.applicant_code)
        if len(applications) == 0:
            raise ValueError

    def __print_interview_details(self):
        query = Interview.select().join(Applicant).where(Applicant.applicant_code == self.applicant_code)
        if len(query) == 0:
            print("Wrong code! Please, try again!")
        for i in query:
            print(i.applicant_code.first_name, i.applicant_code.last_name, "\n",
                  "Your school is Codecool", i.applicant_code.applied_school.city, "\n",
                  "Your interview date:", i.slot_id.start_time, "\n",
                  "Your mentor is", i.slot_id.mentor.first_name, i.slot_id.mentor.last_name)

    def __print_status_details(self):
        applicant = Applicant.select().where(Applicant.applicant_code == self.applicant_code).get()
        print("Your application status is ", applicant.status)

    def __print_school_details(self):
        applicant = Applicant.select().where(Applicant.applicant_code == self.applicant_code).get()
        print("Your applied school is", applicant.applied_school.city)
