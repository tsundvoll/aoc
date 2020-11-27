from solution import *
import pytest

@pytest.mark.skip("Not implemented yet")
def test_data_structure():
    width = 5
    height = 10
    center = (3,4)

    my_map = PrintableMap(width, height)
    my_map.place_wire(3, 4)
    my_map.plot()

    assert False


@pytest.mark.skip("Already checked")
def test_part_1():
    first_wire = ["R8", "U5", "L5", "D3"]
    second_wire = ["U7", "R6", "D4", "L4"]
    assert find_closest_cross_location(first_wire, second_wire) == 6

    first_wire = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    second_wire = ["U62","R66","U55","R34","D71","R55","D58","R83"]
    assert find_closest_cross_location(first_wire, second_wire) == 159


    first_wire = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
    second_wire = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
    assert find_closest_cross_location(first_wire, second_wire) == 135


def test_part_2():
    # first_wire = ["R5", "U5", "L10", "D10", "R10"]
    # second_wire = ["U7", "R6", "D4", "L4"]
    # assert find_fewest_steps_to_intersection(first_wire, second_wire) == 30

    first_wire = ["R8", "U5", "L5", "D3"]
    second_wire = ["U7", "R6", "D4", "L4"]
    assert find_fewest_steps_to_intersection(first_wire, second_wire) == 30

    first_wire = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
    second_wire = ["U62","R66","U55","R34","D71","R55","D58","R83"]
    assert find_fewest_steps_to_intersection(first_wire, second_wire) == 610


    first_wire = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
    second_wire = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
    assert find_fewest_steps_to_intersection(first_wire, second_wire) == 410
