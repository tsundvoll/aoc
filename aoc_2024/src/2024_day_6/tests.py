import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""",
            41,
        ),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    answer = first_task(ex)
    assert answer == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""example_input""", None),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output


if __name__ == "__main__":
    test_first_task(
        """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""",
        41,
    )
