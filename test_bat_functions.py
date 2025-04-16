# test_bat_functions.py

import pytest
from bat_functions import calculate_bat_power, signal_strength

def test_calculate_bat_power():

    """ Tests that bat power is correctly calculated with the given level"""
    assert calculate_bat_power(1) == 1 * 42
    assert calculate_bat_power(2) == 2 * 42
    assert calculate_bat_power(3) == 3 * 42

@pytest.mark.parametrize("distance, expected", [
    (5,50),
    (7.8,22),
    (3,70),
    (12,0)
])

def test_signal_strength(distance, expected):

    """ Tests that signal power is correctly calculated and above zero"""
    assert signal_strength(distance) == expected
