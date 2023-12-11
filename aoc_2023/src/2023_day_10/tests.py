import pytest

from solution import first_task, second_task

EX_1 = """.....
.S-7.
.|.|.
.L-J.
.....
"""

EX_1_ADVANCED = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

EX_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

EX_2_ADVANCED = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EX_1, 4),
        (EX_1_ADVANCED, 4),
        (EX_2, 8),
        (EX_2_ADVANCED, 8),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert first_task(ex) == expected_output


EX_3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

EX_4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

EX_5 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (EX_3, 4),
        (EX_4, 8),
        (EX_5, 10),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l.strip(), input.splitlines()))
    assert second_task(ex) == expected_output
