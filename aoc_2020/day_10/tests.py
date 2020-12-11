from solution import *
import pytest

data_1 = [int(x) for x in open('test_1.txt').read().splitlines()]
data_2 = [int(x) for x in open('test_2.txt').read().splitlines()]


def test_part_1():
    res = count_differences(data_1)
    assert res[1] == 7
    assert res[3] == 5

    res = count_differences(data_2)
    assert res[1] == 22
    assert res[3] == 10


def test_part_2():
    assert count_arrangements(data_1) == 8
    assert count_arrangements(data_2) == 19208
