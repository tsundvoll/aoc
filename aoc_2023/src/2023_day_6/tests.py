import pytest

from solution import first_task, second_task

EXAMPLE_INPUT = """Time:      7  15   30
Distance:  9  40  200
"""


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EXAMPLE_INPUT, 288),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EXAMPLE_INPUT, 71503),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
