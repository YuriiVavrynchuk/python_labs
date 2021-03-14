from .MedicalProfession import *


class Surgeon(MedicalProfession):

    def __init__(self, name, department, duration, avg_salary, max_age, organ):
        MedicalProfession.__init__(self, name, department, duration, avg_salary, max_age)
        self.__organ = organ

    def print_out(self):
        print(f"All information about medic: Name: {self._name}.\n"
              f"Department: {self._department.name}"
              f"Duration: {self._duration}.\n"
              f"Organ: {self.__organ.name}.\n"
              f"Average salary: {self._avg_salary}.\n"
              f"Max age: {self._max_age}.\n")

    def get_organ(self):
        return self.__organ

    def set_organ(self, organ):
        self.__organ = organ
