import unittest
from unittest import TestCase
import random
import sys
import os

sys.path.append(os.path.abspath("../../src")) # noqa
import my_utils


class Test(TestCase):
    def test_get_column_happy(self):
        result = my_utils.get_column('../test_data.csv',
                                     query_column=0,
                                     query_value="China",
                                     result_column=3, )

        self.assertIsNotNone(result)

    def test_get_country_names_happy(self):
        names = my_utils.get_country_names('../test_data.csv')
        # assert that all names are unique
        self.assertEquals(len(set(names)) / len(names), 1)


class TestMath(TestCase):

    def setUp(self):
        self.long_list = [random.random() for i in range(10000)]


    def test_mean(self):
        self.assertAlmostEqual(my_utils.mean(self.long_list), 0.5, places=2)

    def test_median(self):
        self.assertAlmostEqual(my_utils.mean(self.long_list), 0.5, places=2)

    def test_std(self):
        self.assertAlmostEqual(my_utils.std(self.long_list), 12**(-1/2), places=2)


if __name__ == "__main__":
    unittest.main()
