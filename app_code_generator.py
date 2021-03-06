from random import randint
from models import *


class AppCodeGenerator:
    """ This class generate the application code. First, generate the application_code,
        then compare the earlier password, if the current app code equal with the earlier, generate a new one """

    def __init__(self):
        self.__earlier_app_code = []
        self.__query_the_earliest_app_code()
        self.__is_valid_pass = False

        self.application_code = ""
        self.__generate_code()

    def __query_the_earliest_app_code(self):
        applications = Applicant.select()
        for application in applications:
            self.__earlier_app_code.append(application.applicant_code)

    def __generate_code(self):
        counter = 0
        while counter != 6:
            self.application_code += str(randint(0, 9))
            counter += 1
        self.__check_earlier_app_code()

    def __check_earlier_app_code(self):
        # if the current password in the earlier,call the code generator again,
        # what check the earlier app code again
        while self.__is_valid_pass is False:
            if self.application_code not in self.__earlier_app_code:
                self.__is_valid_pass = True
            else:
                self.__generate_code()
