from solution import *
import time

import pytest

data = [x for x in open('test.txt').read().splitlines()]


def test_part_1():
    earliest_departure = int(data[0])
    busses = data[1]

    bus_id, dep_time = find_first_bus(data)
    wait_time = dep_time - earliest_departure
    
    assert bus_id == 59
    assert dep_time == 944
    assert wait_time == 5
    assert bus_id*wait_time == 295


test_1 = ["17","x","13","19"]
test_2 = ["67","7","59","61"]
test_3 = ["67","x","7","59","61"]
test_4 = ["67","7","x","59","61"]
test_4 = ["67","7","x","59","61"]
test_5 = ["1789","37","47","1889"]


def test_part_2():
    # busses = data[1].split(",")
    # assert find_first_subsequent_timestamp(busses) == 1068781
    # print("Test 0 Done")

    # assert find_first_subsequent_timestamp(test_1) == 3417
    # print("Test 1 Done")

    # assert find_first_subsequent_timestamp(test_2) == 754018
    # print("Test 2 Done")

    # assert find_first_subsequent_timestamp(test_3) == 779210
    # print("Test 3 Done")

    # assert find_first_subsequent_timestamp(test_4) == 1261476
    # print("Test 4 Done")

    assert find_first_subsequent_timestamp(test_5) == 1202161486
    print("Test 5 Done")


if __name__ == "__main__":
    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran tests in {toc - tic:0.4f} seconds")
