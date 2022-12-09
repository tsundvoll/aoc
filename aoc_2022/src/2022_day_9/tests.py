import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""",
            13,
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
            """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""",
            1,
        ),
        (
            """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""",
            36,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
