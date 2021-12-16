import pytest
from day_3.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""",
            198
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
            """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""",
            230
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
