#!/usr/bin/env python

from leap import is_leap_year

import unittest

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertTrue(is_leap_year("2020"))

    def test2(self):
        self.assertTrue(is_leap_year("2024"))

    def test3(self):
        self.assertFalse(is_leap_year("1981"))

    def test4(self):
        self.assertRaises(ValueError, is_leap_year, "fasdgfawdg")

if __name__ == '__main__':
    unittest.main(verbosity=2)
