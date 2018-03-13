from sample.basic import BMI
from unittest import TestCase


class TestBMI(TestCase):
    def setUp(self):
        self.bmi = BMI()

    def test_calc_bmi(self):
        bmi = self.bmi.calc_bmi(56.0, 1.78)
        self.assertEqual(bmi, 17.67)

    def test_calc_right_weight(self):
        right_weight = self.bmi.right_weight(1.78)
        self.assertEqual(right_weight, 69.7)




