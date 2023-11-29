import pytest
from solution import first_task, second_task


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""",
            6032,
        ),
    ],
)
def test_first_task(input, expected_output):
    ex = list(map(lambda l: l, input.splitlines()))
    assert first_task(ex, max_line_length=16) == expected_output


@pytest.mark.parametrize(
    "input, expected_output",
    [
        (
            """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""",
            5031,
        ),
    ],
)
def test_second_task(input, expected_output):
    ex = list(map(lambda l: l, input.splitlines()))
    assert second_task(ex, max_line_length=16) == expected_output


if __name__ == "__main__":
    #     test_first_task(
    #         """        ...#
    #         .#..
    #         #...
    #         ....
    # ...#.......#
    # ........#...
    # ..#....#....
    # ..........#.
    #         ...#....
    #         .....#..
    #         .#......
    #         ......#.

    # 10R5L5R10L4R5L5
    # """,
    #         6032,
    #     )
    test_second_task(
        """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""",
        5031,
    )
