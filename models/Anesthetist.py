from .MedicalProfession import *


class Anesthetist(MedicalProfession):

    def __init__(self, name, department, duration, avg_salary, max_age, remedy):
        MedicalProfession.__init__(self, name, department, duration, avg_salary, max_age)
        self.__remedy = remedy

    def print_out(self):
        print(f"All information about medic: Name: {self._name}.\n"
              f"Department: {self._department.name}.\n"
              f"Duration: {self._duration}.\n"
              f"Remedy: {self.__remedy.name}.\n"
              f"Average salary: {self._avg_salary}.\n"
              f"Max age: {self._max_age}.\n")

    def get_remedy(self):
        return self.__remedy

    def set_remedy(self, remedy):
        self.__remedy = remedy
