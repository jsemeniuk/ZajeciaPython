from unittest import TestCase
from bmi import bmi, NotHigherthan0


class TestBmi(TestCase):
    def test_bmi(self):
        self.assertEqual(bmi(58, 1.57), 23.5)
        self.assertEqual(bmi(30, 1.57), 12.2)
        self.assertEqual(bmi(100, 1.57), 40.6)

    def test_badargument(self):
        with self.assertRaises(NotHigherthan0):
            bmi(0, 0)
        with self.assertRaises(NotHigherthan0):
            bmi(0, 1.57)
        with self.assertRaises(NotHigherthan0):
            bmi(58, 0)
