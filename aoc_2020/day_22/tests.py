from solution import *
import pytest


def test_part_1():
    data = [x for x in open('test.txt').read().splitlines()]
    assert game_result(data) == 306


def test_part_2():
    data = [x for x in open('test_2.txt').read().splitlines()]
    assert recursive_combat_result(data) == 291


if __name__ == "__main__":
    test_part_1()
    test_part_2()