import pytest
from year_2015_day_6.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """turn on 0,0 through 999,999""",
            1000000
        ),
        (
            """turn on 0,0 through 3,3
            turn off 0,0 through 2,2
            toggle 0,0 through 4,4""",
            18
        ),
    ]
)
def test_first_task(input, expected_output):
    ex = input.splitlines()
    assert first_task(ex) == expected_output

def test_second_task():
    ex = ("""turn on 0,0 through 0,0""").splitlines()
    assert second_task(ex) == 1
    ex = ("""toggle 0,0 through 999,999""").splitlines()
    assert second_task(ex) == 2000000

    ex = ("""turn on 0,0 through 3,3
    turn off 0,0 through 2,2
    toggle 0,0 through 4,4""").splitlines()
    assert second_task(ex) == 57
