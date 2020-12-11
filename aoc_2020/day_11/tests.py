from solution import *
import pytest
import numpy as np




data_0 = parse_data([x for x in open('test.txt').read().splitlines()])
data_1 = parse_data([x for x in open('test_1.txt').read().splitlines()])
data_2 = parse_data([x for x in open('test_2.txt').read().splitlines()])
data_3 = parse_data([x for x in open('test_3.txt').read().splitlines()])
data_4 = parse_data([x for x in open('test_4.txt').read().splitlines()])
data_5 = parse_data([x for x in open('test_5.txt').read().splitlines()])

data_21 = parse_data([x for x in open('test_21.txt').read().splitlines()])
data_22 = parse_data([x for x in open('test_22.txt').read().splitlines()])
data_23 = parse_data([x for x in open('test_23.txt').read().splitlines()])
data_24 = parse_data([x for x in open('test_24.txt').read().splitlines()])
data_25 = parse_data([x for x in open('test_25.txt').read().splitlines()])
data_26 = parse_data([x for x in open('test_26.txt').read().splitlines()])

data_sparse = parse_data([x for x in open('test_sparse.txt').read().splitlines()])


@pytest.mark.skip("Done")
def test_part_1():
    data = data_0
    print_seats(data, "Initial")
    seats_1 = apply_rules_1(data)
    print_seats(data_1, "True 1")
    print_seats(seats_1, "Sim 1")
    assert (data_1 == seats_1).all()

    seats_2 = apply_rules_1(seats_1)
    print_seats(data_2, "True 2")
    print_seats(seats_2, "Sim 2")
    assert (data_2 == seats_2).all()

    seats_3 = apply_rules_1(seats_2)
    print_seats(data_3, "True 3")
    print_seats(seats_3, "Sim 3")
    assert (data_3 == seats_3).all()

    seats_4 = apply_rules_1(seats_3)
    print_seats(data_4, "True 4")
    print_seats(seats_4, "Sim 4")
    assert (data_4 == seats_4).all()

    seats_5 = apply_rules_1(seats_4)
    print_seats(data_5, "True 5")
    print_seats(seats_5, "Sim 5")
    assert (data_5 == seats_5).all()

    new_seats = simulate_1(data_0)

    occupied = len(new_seats[new_seats == 1])
    assert occupied == 37


def test_part_2():


    data = data_0
    print_seats(data, "Initial")
    seats_21 = apply_rules_2(data)
    print_seats(data_21, "True 21")
    print_seats(seats_21, "Sim 21")
    assert (data_21 == seats_21).all()

    seats_22 = apply_rules_2(seats_21)
    print_seats(data_22, "True 22")
    print_seats(seats_22, "Sim 22")
    assert (data_22 == seats_22).all()

    seats_23 = apply_rules_2(seats_22)
    print_seats(data_23, "True 23")
    print_seats(seats_23, "Sim 23")
    assert (data_23 == seats_23).all()

    seats_24 = apply_rules_2(seats_23)
    print_seats(data_24, "True 24")
    print_seats(seats_24, "Sim 24")
    assert (data_24 == seats_24).all()

    seats_25 = apply_rules_2(seats_24)
    print_seats(data_25, "True 25")
    print_seats(seats_25, "Sim 25")
    assert (data_25 == seats_25).all()



    new_seats = simulate_2(data_0)
    print_seats(new_seats, "new_seats", is_chars=False)


    occupied = len(new_seats[new_seats == 1])
    assert occupied == 26
