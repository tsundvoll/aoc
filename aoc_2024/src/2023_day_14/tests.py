import pytest
from solution import first_task, second_task, tilt_column_once


@pytest.mark.skip
@pytest.mark.parametrize(
    "input_column, expected_column, is_expected_equal",
    [
        ([".", ".", ".", "O"], [".", ".", "O", "."], True),
        (["O", ".", ".", "O"], ["O", ".", "O", "."], True),
        ([".", ".", "#", "O"], [".", ".", "#", "O"], False),
    ],
)
def test_tilt_column_once(input_column, expected_column, is_expected_equal):
    tilted_column, is_different = tilt_column_once(input_column)

    assert tuple(tilted_column) == tuple(expected_column)
    assert is_different == is_expected_equal


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""",
            136,
        ),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""",
            64,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
