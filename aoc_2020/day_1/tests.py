from .solution import *
import pytest


"""
Expense report
"""

def test_part_1():
    expenses = [1721,979,366,299,675,1456]
    assert expenses_2020(expenses) == 514579


def test_part_2():
    expenses = [1721,979,366,299,675,1456]
    assert expenses_three_2020(expenses) == 241861950