from solution import *
import pytest

data = parse([x for x in open('test.txt').read().splitlines()])
data_4d = parse_4d([x for x in open('test.txt').read().splitlines()])


def test_part_1():
    assert run_cycles(data, 6) == 112


def test_part_2():
    assert run_cycles_hyperspace(data_4d, 6) == 848


if __name__ == "__main__":
    tic = time.perf_counter()
    test_part_1()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran tests in {toc - tic:0.4f} seconds")
