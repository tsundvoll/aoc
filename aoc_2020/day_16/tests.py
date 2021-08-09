from solution import *
import pytest
import time

data = [x for x in open('test.txt').read().splitlines()]
data_2 = [x for x in open('test_2.txt').read().splitlines()]


def test_part_1():
    invalid_values = invalid_values_on_nearby_tickets(data)
    assert invalid_values == [4,55,12]
    assert sum(invalid_values) == 71


def test_part_2():
    field_values = find_field_values(data_2)
    assert field_values["class"] == 12
    assert field_values["row"] == 11
    assert field_values["seat"] == 13


if __name__ == "__main__":
    tic = time.perf_counter()
    # test_part_1()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran tests in {toc - tic:0.4f} seconds")
