#!/usr/bin/env python

# Tests for leap.py.

import pytest

from leap import is_leap_year


def test_is_leap1():
    assert is_leap_year("2020") == True


def test_is_leap2():
    assert is_leap_year("2021") == False

def test_is_leap3():
    with pytest.raises(ValueError):
        is_leap_year("fasdkjgfas")
        
    
