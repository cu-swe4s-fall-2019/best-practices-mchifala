import unittest
from get_column_stats import calculate_std
from get_column_stats import calculate_mean
import random
import os
import numpy as np


class TestMean(unittest.TestCase):

    def make_file(self):
        self.n = 100
        self.empty = []
        self.V = np.random.randint(0, 100, size=self.n)
        self.test_file = 'data_file.txt'
        self.mean = np.mean(self.V)
        self.std = np.std(self.V)

    def setUp(self):
        self.make_file()

    def test_mean(self):
        for i in range(100):
            self.make_file()
            self.assertEqual(calculate_mean(self.V), round(self.mean, 1))

    def test_std(self):
        for i in range(100):
            self.make_file()
            self.assertAlmostEqual(calculate_std(self.mean, self.V),
                                   self.std, 2)

    def test_mean_empty_excp(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, calculate_mean, self.empty)

    def test_std_empty_excp(self):
        self.assertRaises(ZeroDivisionError and
                          SystemExit, calculate_std, self.mean, self.empty)


if __name__ == '__main__':
    unittest.main()

"""
 def test_mean_empty_exit(self):
        with self.assertRaises(SystemExit) as cm:
            calculate_mean(self.empty)
        self.assertEqual(cm.exception.code, 1)

    def test_std_empty_exit(self):
        with self.assertRaises(SystemExit) as cm:
            calculate_std(self.mean, self.empty)
        self.assertEqual(cm.exception.code, 1)
"""
