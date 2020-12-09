from solution import *
import pytest

data = [x for x in open('test.txt').read().splitlines()]


def test_part_1():
    assert acc_before_loop(data) == 5


def test_part_2():
    changed_data = data.copy()
    for i, line in enumerate(data):
        tmp = changed_data[i]
        op, arg = line.split()
        if op == "nop":
            changed_data[i] = "".join(("jmp ", arg))
        elif op == "jmp":
            changed_data[i] = "".join(("nop ", arg))

        try:
            result = acc_after_termination(changed_data)
            break
        except KeyError as e:
            print(e)
            changed_data[i] = tmp

    assert result == 8