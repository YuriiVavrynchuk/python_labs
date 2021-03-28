from abc import ABC
from abc import abstractmethod


class MedicalProfession(ABC):

    def __init__(self,name, department, duration, avg_salary, max_age):
        self._name = name
        self._department = department
        self._duration = duration
        self._avg_salary = avg_salary
        self._max_age = max_age

    @abstractmethod
    def print_out(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_avg_salary(self):
        return self._avg_salary

    def set_avg_salary(self, avg_salary):
        self._avg_salary = avg_salary

    def get_max_age(self):
        return self._max_age

    def set_max_age(self, max_age):
        self._max_age = max_age
