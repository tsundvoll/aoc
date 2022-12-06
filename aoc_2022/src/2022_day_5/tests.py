import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""",
            "CMZ",
        ),
    ],
)
def test_first_task(input, expected_output):
    ex = list(input.splitlines())
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""",
            "MCD",
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(input.splitlines())
    assert second_task(ex) == expected_output
