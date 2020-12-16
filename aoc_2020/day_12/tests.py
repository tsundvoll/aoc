from solution import *
import pytest

data = parse([x for x in open('test.txt').read().splitlines()])


def test_part_1():
    # actions
    # values
    print(data)
    east, north = travel(data)

    assert east == 17
    assert north == -8
    assert abs(east) + abs(north) == 25


def test_part_2():
    east, north = travel_waypoint(data)
    assert abs(east) + abs(north) == 286
