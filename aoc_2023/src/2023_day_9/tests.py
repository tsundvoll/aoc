import pytest

from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""",
            114,
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
            """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""",
            2,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
