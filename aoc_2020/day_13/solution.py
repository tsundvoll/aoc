from functools import reduce
from itertools import groupby, takewhile, repeat, count, dropwhile, filterfalse
from math import gcd
from mod import Mod
from operator import add, mod, eq
import numpy as np
import time

data = [x for x in open('input.txt').read().splitlines()]


def find_first_bus(input_data):
    earliest_departure = int(input_data[0])
    busses = input_data[1].split(",")

    first_departure = earliest_departure
    while True:
        for bus in busses:
            if bus == "x":
                continue
            else:
                if first_departure%int(bus) == 0:
                    return int(bus), first_departure
        first_departure += 1
    return 0,0


def all_equal(iterable):    
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def do_check(bus_ids, offsets, c):
    for b, o in zip(bus_ids, offsets):
        if (c+o)%b !=0:
            return False
    return True


def find_first_subsequent_timestamp(busses):
    list_of_bus_ids = []
    list_of_offsets = []

    for i, bus in enumerate(busses):
        if bus != "x":
            bus_id = int(bus)
            list_of_bus_ids.append(bus_id)   
            list_of_offsets.append(i)

    list_of_offsets = [x for _,x in sorted(zip(list_of_bus_ids, list_of_offsets), reverse=True)]
    list_of_bus_ids = [x for _,x in sorted(zip(list_of_bus_ids, list_of_bus_ids), reverse=True)]

    c = 0
    step = 1
    include = 1
    event = 0
    while True:
        if do_check(list_of_bus_ids[:include], list_of_offsets[:include], c):
            # print("Found aligning busses at {}".format(c))
            if include >= len(list_of_bus_ids):
                return c

            if event == 0:
                event = 1
                event_start = c
            elif event == 1:
                event = 0
                step = c - event_start
                # print("New step will be {}".format(step))
                include += 1
        c += step


def find_first_subsequent_timestamp_old(busses):
    offsets = []
    bus_ids = []
    largest_bus_id = 0
    largest_i = 0
    denominators = []
    modulos = []
    for i, bus in enumerate(busses):
        
        if bus != "x":
            bus_id = int(bus)
            denominators.append(bus_id)
            if bus_id > largest_bus_id:
                largest_bus_id = bus_id
                largest_i = i
            offsets.append(i)
            bus_ids.append(bus_id)
            modulos.append(Mod(i, bus_id))

    c = count(-largest_i, largest_bus_id)

    a = offsets
    b = bus_ids

    res = filter(
        lambda n: all(list(
            map(
                eq,
                map(
                    mod,
                    map(
                        add,
                        repeat(n),
                        a
                    ),
                    b
                ),
                repeat(0)
            )
        )),
        c
    )
    r = next(res)
    return r


def solution_part_1():
    earliest_departure = int(data[0])
    busses = data[1]

    bus_id, dep_time = find_first_bus(data)
    wait_time = dep_time - earliest_departure

    return bus_id*wait_time


def solution_part_2():
    busses = data[1].split(",")
    return find_first_subsequent_timestamp(busses)


if __name__ == "__main__":
    print("Part 1")
    tic = time.perf_counter()
    print("- answer:", solution_part_1())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")


    print("Part 2")
    tic = time.perf_counter()
    print("- answer:", solution_part_2())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")
