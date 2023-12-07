import pytest

from solution import first_task, second_task

EXAMPLE_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

MINI_EXAMPLE_INPUT = """seeds: 0 11

seed-to-soil map:
4 2 7
2 9 2

humidity-to-location map:
3 0 6
0 6 3
"""


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EXAMPLE_INPUT, 35),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


# All seeds transformation:
# [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 43, 36, 37, 38, 39, 40, 41, 42, 90, 91, 92, 93, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 61, 62, 63, 64, 65, 66, 20, 21, 44, 45, 85, 86, 87, 88, 89, 94, 95, 96, 56, 57, 58, 59, 97, 98, 99, 73, 0, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 60, 68, 69, 70, 71, 72, 67, 19]


# 46
@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            EXAMPLE_INPUT,
            46,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
