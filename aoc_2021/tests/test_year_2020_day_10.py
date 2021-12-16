import pytest
from year_2020_day_10.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """example_input""",
            0
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
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
