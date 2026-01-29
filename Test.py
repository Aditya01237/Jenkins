#!/usr/bin/python3
# Unit test for Prog1.py

import unittest
from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_addition(self):
        data = [10, 20]
        result = summation(data)
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()
