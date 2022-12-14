import pytest
from solution_refactored import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""",
            31,
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
            """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""",
            29,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
