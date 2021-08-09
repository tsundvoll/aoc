from solution import *
import pytest
import time

test_data = parse([x for x in open('test.txt').read().splitlines()])


def test_part_1():
    lines_answers = calc_lines(test_data)
    assert lines_answers == [71,51,26,437,12240,13632]


def test_part_2():
    lines_answers = calc_lines_advanced(test_data)
    assert lines_answers == [231,51,46,1445,669060,23340]



if __name__ == "__main__":
    tic = time.perf_counter()
    test_part_1()
    toc = time.perf_counter()
    print(f"Ran first tests in {toc - tic:0.4f} seconds")
    

    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran second tests in {toc - tic:0.4f} seconds")