import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 3068),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "n_rocks, expected_output",
    [
        (2022, 3161),
        (5000, 7879),
        (10000, 15755),
        (20000, 31505),
    ],
)
def test_second_task(n_rocks, expected_output):
    assert second_task(n_rocks) == expected_output


if __name__ == "__main__":
    test_first_task(""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 3068)
