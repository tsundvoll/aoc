import pytest
from day_5.solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""",
            5
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
            """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""",
            12
        ),
    ]
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output


# def second_task(input):
#     count = 0
#     scores = {')': 1, ']': 2, '}': 3, '>': 4}
#     S = []
#     for word in input:
#         stack = []
#         open_c = {'(': 0, '[': 0, '{': 0, '<': 0}
#         for i in range(len(word)):
#             c = word[i]

#             if c in open_c.keys():
#                 closing_match = {'(': ')', '[': ']', '{': '}', '<': '>'}[c]
#                 stack.append(closing_match)
#             else:
#                 next_closing_c = stack.pop()

#                 if c != next_closing_c:
#                     # print(f'At {i}, found {c}, expected {next_closing_c}')
#                     count += {
#                         ')': 3, ']': 57, '}': 1197, '>': 25137
#                     }[c]

#         print(stack)
#         # if len(stack) > 0:
#         #     # r = stack[::-1]
#         #     print(r)
#         #     s = 0
#         #     for c in r:
#         #         s = s * 5 + scores[c]

#             # S.append(s)
#         print()

#     # return int(S[len(S)//2])
