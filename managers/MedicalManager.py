class MedicalManager:

    def __init__(self, medicalprofessions=list):
        self.__medicalProfessions = medicalprofessions

    def find_by_duration(self, duration):
        result = list()
        for i in self.__medicalProfessions:
            if i.get_duration() == duration:
                result.append(i)
        return result

    def find_by_department(self, department):
        result = list()
        for i in self.__medicalProfessions:
            if i.get_department() == department:
                result.append(i)
        return result

    def sort_by_max_age(self, order):
        result = list()
        self.__medicalProfessions.sort(key=lambda i: i.get_max_age(),
                                       reverse=bool(order.value))
        result = self.__medicalProfessions
        return result

    def print_out(self):
        for i in self.__medicalProfessions:
            i.print_out()
            print("----------------------------------------------------------")
