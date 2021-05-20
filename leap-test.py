#!/usr/bin/env python

# Tests for leap.py.

from leap import is_leap_year


def test_is_leap1():
    assert is_leap_year("2020") == True


