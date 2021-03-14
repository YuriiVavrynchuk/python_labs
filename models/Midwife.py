from .MedicalProfession import *


class Midwife(MedicalProfession):

    def __init__(self, name, department, duration, avg_salary, max_age, style):
        MedicalProfession.__init__(self, name, department, duration, avg_salary, max_age)
        self.__style = style

    def print_out(self):
        print(f"All information about medic: Name {self._name}.\n"
              f"Department: {self._department.name}.\n"
              f"Duration: {self._duration}.\n"
              f"Style: {self.__style.name}.\n"
              f"Average salary: {self._avg_salary}.\n"
              f"Max age: {self._max_age}.\n")

    def get_style(self):
        return self.__style

    def set_style(self, style):
        self.__style = style
