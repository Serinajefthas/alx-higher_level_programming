#!/usr/bin/python3
"""Defines a class TestMaxInteger for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    def test_max_integer(self):
        """Test max integer"""
        self.assertEqual(max_integer([5, -2, 100, 3]), 100)

    def test_empty_list(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_float_numbers(self):
        """Test for float values"""
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_negative_integers(self):
        """Test for negative integers"""
        test_list1 = [-91, -31, -4, -2]
        self.assertEqual(max_integer(test_list1), -2)

    def test_zero_number(self):
        """Test zero values"""
        self.assertEqual(max_integer([0, 0]), 0)

    def test_string_numbers(self):
        """Test for passing a string of numbers in list"""
        test_list = ["1234"]
        self.assertEqual(max_integer(test_list), "1234")

if __name__ == '__main__':
    unittest.main()
