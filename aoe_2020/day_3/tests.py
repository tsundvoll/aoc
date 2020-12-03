from solution import *
import pytest

test_data =[
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]


def test_part_1():
    parsed_data = parse_data(test_data)

    assert not check_pos(parsed_data, 0, 0)
    assert not check_pos(parsed_data, 3, 1)
    assert check_pos(parsed_data, 6, 2)
    assert check_pos(parsed_data, 21, 7)

    right = 3
    down = 1
    assert count_trees(parsed_data, right, down) == 7


@pytest.mark.skip("Not implemented yet")
def test_part_2():
    raise NotImplementedError
