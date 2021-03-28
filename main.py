from models import *
from managers import *


def main():
    a = Midwife("Popka", Department.East, 8, 1000, 60, MidwifeStyle.StyleB0231)
    b = Surgeon("Dupka", Department.East, 7, 1200, 55, Organ.Brain)
    c = Anesthetist("Kaka", Department.West, 8, 800, 70, Remedy.CO3COOH)
    first_group = [a, b, c]
    first_group_manager = MedicalManager(first_group)
    first_group_manager.sort_by_max_age(Order.Ascending)
    first_group_manager.print_out()
    first_group_manager.find_by_duration(8)
    first_group_manager.find_by_department(Department.East)


if __name__ == '__main__':
    main()
