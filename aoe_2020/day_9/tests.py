from solution import *
import pytest


data = [int(x) for x in open('test.txt').read().splitlines()]


def test_part_1():
    preamble = [1,2,3,4,5]

    assert is_two_sum(preamble, 6) == True
    assert is_two_sum(preamble, 9) == True
    assert is_two_sum(preamble, 10) == False

    assert first_invalid(data=data, preamble_length=5) == 127


def test_part_2():
    result = find_contiguous_set(data=data, preamble_length=5)

    assert result == [15,25,47,40]

    s_result = sorted(result)

    assert s_result[0] + s_result[-1] == 62