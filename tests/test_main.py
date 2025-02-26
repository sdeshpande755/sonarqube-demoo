import sys
import os

# Add the 'app' directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Now import functions from main.py
from main import add, subtract, multiply, division  

import unittest

class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(division(10, 5), 2)

if __name__ == '__main__':
    unittest.main()