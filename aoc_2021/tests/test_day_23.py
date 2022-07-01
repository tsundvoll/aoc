from day_23.solution import first_task, second_task
import pytest


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """B C B D
A D C A""",
            12521
        ),
    ]
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


# @pytest.mark.parametrize(
#     "input, expected_output",
#     [
#         (
#             """B C B D
# D C B A 
# D B A C
# A D C A""",
#             44169
#         ),
#     ]
# )
# def test_second_task(input, expected_output):
#     ex = list(map(lambda l: l.strip(), input.splitlines()))
#     assert second_task(ex) == expected_output
