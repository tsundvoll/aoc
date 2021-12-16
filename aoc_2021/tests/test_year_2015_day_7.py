import pytest
from year_2015_day_7.solution import first_task, second_task


@pytest.mark.skip
@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """123 -> x
            456 -> y
            x AND y -> d
            x OR y -> e
            x LSHIFT 2 -> f
            y RSHIFT 2 -> g
            NOT x -> h
            NOT y -> i""",
            {
                'd': 72,
                'e': 507,
                'f': 492,
                'g': 114,
                'h': 65412,
                'i': 65079,
                'x': 123,
                'y': 456,
            }
        ),
    ]
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.skip
@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """example_input""",
            0
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = input.splitlines()
    assert second_task(ex) == expected_output
