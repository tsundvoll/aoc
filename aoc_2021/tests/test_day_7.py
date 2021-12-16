import pytest
from day_7.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """16,1,2,0,4,2,7,1,2,14""",
            37
        ),
    ]
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))[0]
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """16,1,2,0,4,2,7,1,2,14""",
            168
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))[0]
    assert second_task(ex) == expected_output
