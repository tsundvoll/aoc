from solution import *
import pytest
import time
import re



data = [x for x in open('test.txt').read().splitlines()]
data_2 = [x for x in open('test_2.txt').read().splitlines()]


def test_part_1():
    assert read_program(data) == 165
    
        

def test_part_2():
    assert read_program_floating(data_2) == 208


if __name__ == "__main__":
    tic = time.perf_counter()
    # test_part_1()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran tests in {toc - tic:0.4f} seconds")
