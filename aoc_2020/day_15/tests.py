from solution import *
import pytest

starting_numbers = [0,3,6]


def test_part_1():
    # assert play_game_until(starting_numbers, 1) == 0
    # assert play_game_until(starting_numbers, 2) == 3
    # assert play_game_until(starting_numbers, 3) == 6
    # assert play_game_until(starting_numbers, 4) == 0
    assert play_game_until(starting_numbers, 5) == 3
    assert play_game_until(starting_numbers, 6) == 3
    assert play_game_until(starting_numbers, 7) == 1
    assert play_game_until(starting_numbers, 8) == 0
    assert play_game_until(starting_numbers, 9) == 4
    assert play_game_until(starting_numbers, 10) == 0

    assert play_game_until(starting_numbers, 2020) == 436


    assert play_game_until([1,3,2], 2020) == 1
    assert play_game_until([2,1,3], 2020) == 10
    assert play_game_until([1,2,3], 2020) == 27
    assert play_game_until([2,3,1], 2020) == 78
    assert play_game_until([3,2,1], 2020) == 438
    assert play_game_until([3,1,2], 2020) == 1836




@pytest.mark.skip("Not implemented yet")
def test_part_2():
    raise NotImplementedError