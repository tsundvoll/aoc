import itertools
from copy import deepcopy

import pytest
from solution import Number, first_task, second_task

LIST_OF_NUMBERS = []
for n in range(10):
    number = Number(value=n)
    LIST_OF_NUMBERS.append(number)

for i in range(len(LIST_OF_NUMBERS) - 1):
    LIST_OF_NUMBERS[i].next = LIST_OF_NUMBERS[i + 1]
    LIST_OF_NUMBERS[i + 1].prev = LIST_OF_NUMBERS[i]

LIST_OF_NUMBERS[0].prev = LIST_OF_NUMBERS[-1]
LIST_OF_NUMBERS[-1].next = LIST_OF_NUMBERS[0]


def test_numbers():
    list_of_numbers = deepcopy(LIST_OF_NUMBERS)

    zero = list_of_numbers[0]

    assert zero.get_next_number(1) == 1
    assert zero.get_next_number(2) == 2
    assert zero.get_next_number(10) == 0
    assert zero.get_next_number(11) == 1

    number_list = list(itertools.islice(zero.yield_numbers(), 10))
    assert number_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_move_forward():
    list_of_numbers = deepcopy(LIST_OF_NUMBERS)
    zero = list_of_numbers[0]
    three = list_of_numbers[3]
    three.move_forward(3)
    number_list = list(itertools.islice(zero.yield_numbers(), 10))
    print(number_list)
    assert number_list == [0, 1, 2, 4, 5, 6, 3, 7, 8, 9]


def test_move_backward():
    list_of_numbers = deepcopy(LIST_OF_NUMBERS)
    zero = list_of_numbers[0]
    three = list_of_numbers[3]
    three.move_backward(2)
    number_list = list(itertools.islice(zero.yield_numbers(), 10))
    print(number_list)
    assert number_list == [0, 3, 1, 2, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """1
2
-3
3
-2
0
4
""",
            3,
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
            """1
2
-3
3
-2
0
4
""",
            1623178306,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output


if __name__ == "__main__":
    test_first_task(
        """1
2
-3
3
-2
0
4
""",
        3,
    )
