from solution import *
import pytest

def test_part_1():
    assert calc_fuel_module(mass=12) == 2
    assert calc_fuel_module(mass=14) == 2
    assert calc_fuel_module(mass=1969) == 654
    assert calc_fuel_module(mass=100756) == 33583


def test_part_2():
    assert calc_fuel_extended(mass=14) == 2
    assert calc_fuel_extended(mass=1969) == 966
    assert calc_fuel_extended(mass=100756) == 50346
