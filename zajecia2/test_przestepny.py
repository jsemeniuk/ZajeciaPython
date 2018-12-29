from unittest import TestCase
from przestepne import przestepny, NotValidYear


class TestPrzestepny(TestCase):
    def test_przestepny(self):
        self.assertEqual(przestepny(1581), False)
        self.assertEqual(przestepny(2019), False)
        self.assertEqual(przestepny(2020), True)

    def test_badargument(self):
        with self.assertRaises(NotValidYear):
            przestepny("tysiac")
        with self.assertRaises(NotValidYear):
            przestepny(0)
        with self.assertRaises(NotValidYear):
            przestepny(10000)
