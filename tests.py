import unittest
from managers import *
from models import *


class TestMedicalManager(unittest.TestCase):

    def setUp(self):
        self.a = Midwife("Popka", Department.East, 8, 1000, 60, MidwifeStyle.StyleB0231)
        self.b = Surgeon("Dupka", Department.East, 7, 1200, 55, Organ.Brain)
        self.c = Anesthetist("Kaka", Department.West, 8, 800, 70, Remedy.CO3COOH)
        result = [self.a, self.b, self.c]
        self.medicalManager = MedicalManager(result)
        self.maxDiff = None

    def test_sort_by_max_age(self):
        self.assertEqual(self.medicalManager.sort_by_max_age(Order.Ascending),
                         [self.b, self.a, self.c])

    def test_find_by_duration(self):
        self.assertEqual(self.medicalManager.find_by_duration(8), [self.a, self.c])

    def test_find_by_department(self):
        self.assertEqual(self.medicalManager.find_by_department(Department.East),
                         [self.a, self.b])


if __name__ == "__main__":
    unittest.main()
