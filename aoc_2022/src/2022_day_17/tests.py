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
    "input, expected_output",
    [
        (""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 1514285714288),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output


if __name__ == "__main__":
    test_first_task(""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 3068)
