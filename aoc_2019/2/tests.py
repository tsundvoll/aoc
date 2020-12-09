from solution import *
import pytest

"""
    1202 program alarm
    Intcode
    prog = [1, 0, 0, 3, 99]

    99 - finished
    1 - adds two numbers
    2 - multiplies two number


"""


def test_part_1():
    program_01 = [1, 0, 0, 0, 99]
    req_result = [2, 0, 0, 0, 99]
    program = Intcode(program_01)
    assert program.run() == req_result


    program_01 = [2,3,0,3,99]
    req_result = [2,3,0,6,99]
    program = Intcode(program_01)
    assert program.run() == req_result


    program_01 = [2,4,4,5,99,0]
    req_result = [2,4,4,5,99,9801]
    program = Intcode(program_01)
    assert program.run() == req_result


    program_01 = [1,1,1,4,99,5,6,0,99]
    req_result = [30,1,1,4,2,5,6,0,99]
    program = Intcode(program_01)
    assert program.run() == req_result


@pytest.mark.skip("Not implemented yet")
def test_part_2():
    raise NotImplementedError