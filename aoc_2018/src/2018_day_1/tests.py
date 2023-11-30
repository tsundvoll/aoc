import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """+1
        -2
        +3
        +1""",
            3,
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
            """+1
        -2
        +3
        +1""",
            2,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
