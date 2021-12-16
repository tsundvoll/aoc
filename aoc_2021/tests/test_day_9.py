import pytest
from day_9.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """2199943210
3987894921
9856789892
8767896789
9899965678""",
            15
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
            """2199943210
3987894921
9856789892
8767896789
9899965678""",
            1134
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
