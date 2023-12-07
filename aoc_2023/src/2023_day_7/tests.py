import pytest

from solution import first_task, second_task

EXAMPLE_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EXAMPLE_INPUT, 6440),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EXAMPLE_INPUT, 5905),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
