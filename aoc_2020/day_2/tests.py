from solution import *
import pytest


def test_part_1():
    data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    assert valid_passwords(data) == 2


def test_part_2():
    data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    assert valid_passwords_2(data) == 2
