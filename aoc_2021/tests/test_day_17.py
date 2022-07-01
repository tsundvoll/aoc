from day_17.solution import first_task, second_task
import pytest


# @pytest.mark.parametrize(
#     "input, expected_output",
#     [
#         (
#             """target area: x=20..30, y=-10..-5""",
#             45
#         ),
#     ]
# )
# def test_first_task(input, expected_output):
#     ex = list(map(lambda l: l.strip(), input.splitlines()))
#     assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """target area: x=20..30, y=-10..-5""",
            112
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
