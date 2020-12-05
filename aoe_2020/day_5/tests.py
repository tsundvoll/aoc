from solution import *
import pytest

"""
binary space partitioning

128 rows
8 columns

First 7: Row between 0 - 127
F (0-63), B (64-127)

Last 3: Column between 0-7
L (0-3), R (4-7)

"""


def test_part_1():
    seat = "FBFBBFFRLR"
    row = get_row(seat)
    column = get_col(seat)
    seat_id = get_seat_id(row, column)

    assert row == 44
    assert column == 5
    assert seat_id == 357

    seat = "BFFFBBFRRR"
    row = get_row(seat)
    column = get_col(seat)
    seat_id = get_seat_id(row, column)

    assert row == 70
    assert column == 7
    assert seat_id == 567

    seat = "FFFBBBFRRR"
    row = get_row(seat)
    column = get_col(seat)
    seat_id = get_seat_id(row, column)

    assert row == 14
    assert column == 7
    assert seat_id == 119

    seat = "BBFFBBFRLL"
    row = get_row(seat)
    column = get_col(seat)
    seat_id = get_seat_id(row, column)

    assert row == 102
    assert column == 4
    assert seat_id == 820



@pytest.mark.skip("Not implemented yet")
def test_part_2():
    raise NotImplementedError
