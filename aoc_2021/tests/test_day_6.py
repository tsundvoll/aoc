import pytest
from day_6.solution import first_task, second_task

# @pytest.mark.parametrize(
#     "input, expected_output",
#     [
#         (
#             """3,4,3,1,2""",
#             5934
#         ),
#     ]
# )
# def test_first_task(input, expected_output):
#     ex = list(map(lambda l: l.strip(), input.splitlines()))[0]
#     assert first_task(ex) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """3,4,3,1,2""",
            26984457539
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))[0]
    assert second_task(ex) == expected_output
