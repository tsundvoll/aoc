import pytest

from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""", 4361),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""", 467835),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
