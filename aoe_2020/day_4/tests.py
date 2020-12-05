from solution import *
import pytest
test_data = [x for x in open('test_input.txt').read().splitlines()]
valid = [x for x in open('valid.txt').read().splitlines()]
invalid = [x for x in open('invalid.txt').read().splitlines()]


def test_part_1():
    pd = parse_data(test_data)
    assert count_valid_passports(pd, 1) == 2


def test_part_2():
    pd_valid = parse_data(valid)
    pd_invalid = parse_data(invalid)

    assert count_valid_passports(pd_valid, 2) == 4
    assert count_valid_passports(pd_invalid, 2) == 0
