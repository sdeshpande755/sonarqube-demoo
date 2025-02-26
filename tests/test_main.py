# tests/test_main.py

import sys
import os
import unittest

# Add the 'app' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Import functions from main.py
from main import add, subtract, multiply, divide

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)  # Extra test for coverage

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 3), -3)  # Extra test for coverage

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 3), -3)  # Extra test for coverage

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(9, 3), 3)  # Extra test for coverage

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)  # Edge case for division by zero

if __name__ == '__main__':
    unittest.main()