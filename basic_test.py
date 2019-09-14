import unittest
from get_column_stats import calculate_std
from get_column_stats import calculate_mean
import random
import os
import numpy as np

class TestMean(unittest.TestCase):

    def setUp(self):
        self.n = 100
        self.empty = []
        self.V = np.random.randint(0, 100, size=self.n)
        self.test_file= 'data_file.txt'
        self.mean = np.mean(self.V)
        self.std = np.std(self.V)

    def test_mean(self):
        self.assertEqual(calculate_mean(self.V), self.mean)

    def test_std(self):
        self.assertAlmostEqual(calculate_std(self.mean, self.V), self.std, 8)
    
    def test_empty_mean(self):
        with self.assertRaises(SystemExit) as cm:
            calculate_mean(self.empty)
        self.assertEqual(cm.exception.code, 1)

    def test_empty_std(self):
        with self.assertRaises(SystemExit) as cm:
            calculate_std(self.mean, self.empty)
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()
