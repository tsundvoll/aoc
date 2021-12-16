import pytest
from day_13.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""",
            17
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
#             """example_input""",
#             None
#         ),
#     ]
# )
# def test_second_task(input, expected_output):
#     ex = list(map(lambda l: l.strip(), input.splitlines()))
#     assert second_task(ex) == expected_output
