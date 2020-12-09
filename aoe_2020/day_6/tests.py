from solution import *
import pytest

data = [x for x in open('test.txt').read().splitlines()]


def test_part_1():
    assert sum_of_answers(data) == 11


def test_part_2():
    assert sum_of_all_yes_answers(data) == 6
