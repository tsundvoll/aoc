import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""bvwbjplbgvbhsrlpgdmjqwftvncz""", 5),
        ("""nppdvjthqldpwncqszvftbrmjlhg""", 6),
        ("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""", 10),
        ("""zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""", 11),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("""mjqjpqmgbljsphdztnvjfqwrcgsmlb""", 19),
        ("""bvwbjplbgvbhsrlpgdmjqwftvncz""", 23),
        ("""nppdvjthqldpwncqszvftbrmjlhg""", 23),
        ("""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""", 29),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
