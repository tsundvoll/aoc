from day_21.solution import first_task, second_task
import pytest


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """4
8""",
            739785
        ),
    ]
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """4
8""",
            444356092776315
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
