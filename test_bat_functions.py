# test_bat_functions.py

import pytest
from bat_functions import calculate_bat_power, signal_strength, get_bat_vehicle


""" Exercise 1 : Basic Tests and Parametrization """

def test_calculate_bat_power():
 """ Tests that bat power is correctly calculated with the given level"""

 assert calculate_bat_power(1) == 1 * 42
 assert calculate_bat_power(2) == 2 * 42
 assert calculate_bat_power(3) == 3 * 42

@pytest.mark.parametrize("distance, expected",
[
    (5,50),
    (7.8,22),
    (3,70),
    (12,0)
]
)

def test_signal_strength(distance:float, expected:float):

 """ Tests that signal power is correctly calculated and above zero"""

 assert signal_strength(distance) == expected



""" Exercise 2 : Fixtures """

@pytest.fixture
def bat_vehicles():
 
 """Fixture that sets up a reusable dictonary of bat_vehicles"""

 return { 
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50},
 }


def test_get_bat_vehicles(bat_vehicles): 
 
 """Tests that get_bat_vehicles function returns the correct specs for each one of batmans vehicles"""

 for v in bat_vehicles :
   assert get_bat_vehicle(v) == bat_vehicles[v]
  
def test_unknown_bat_vehicles():
 
 """Tests that when an unknown vehicle is input-ed an error is thrown"""
 
 with pytest.raises(ValueError, match=f"Unknown vehicle: Batship"): 
  get_bat_vehicle('Batship')