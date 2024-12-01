import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """3   4
4   3
2   5
1   3
3   9
3   3""",
            11,
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
            """3   4
4   3
2   5
1   3
3   9
3   3""",
            31,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
