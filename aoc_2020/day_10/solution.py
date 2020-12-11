import networkx as nx
from networkx import Graph
import numpy as np

import matplotlib.pyplot as plt

input_data = [int(x) for x in open('input.txt').read().splitlines()]


def count_differences(data):
    s_data = sorted(data)
    rating = 0
    res = {1:0, 2:0, 3:0}
    for n in s_data:
        diff = n - rating
        rating = n
        res[diff] += 1
    res[3] += 1
    return res


def count_arrangements(data):
    G = nx.DiGraph()
    s_data = sorted(data)
    s_data.append(s_data[-1]+3)

    rating = 0
    for i in range(len(s_data)):
        alts = s_data[i:i+3]
        for a in alts:
            diff = a - rating
            if diff in [1,2,3]:
                G.add_edge(rating, a)
                # print(rating, "to", a)
        rating = s_data[i]


    l = []
    for node in G:
        print(node)
        l.append(len(list(G.successors(node))))

    new_array = []
    i = 0
    while (i < len(l)):
        el = l[i]
        if el == 2:
            if l[i+1] == 1:
                new_array.append(2)
            elif l[i+1] == 2:
                new_array.append(3)
            i += 2
        elif el == 3:
            if l[i+1] == 1 and l[i+2] == 1:
                new_array.append(3)
            elif l[i+1] == 2 and l[i+2] == 1:
                new_array.append(4)
            elif l[i+1] == 1 and l[i+2] == 2:
                new_array.append(5)
            elif l[i+1] == 2 and l[i+2] == 2:
                new_array.append(6)

            elif l[i+1] == 3 and l[i+2] == 1:
                new_array.append(3)
            elif l[i+1] == 1 and l[i+2] == 3:
                new_array.append(7)
            elif l[i+1] == 3 and l[i+2] == 2:
                new_array.append(7)
            elif l[i+1] == 2 and l[i+2] == 3:
                new_array.append(8)
            elif l[i+1] == 3 and l[i+2] == 3:
                new_array.append(9)
            i += 3
        else:
            i += 1

    # print(l)
    # print(new_array)
    # G.successors()

    # count = 0
    # for path in nx.all_simple_paths(G, 0, s_data[-1]):
    #     count += 1
    # return count
    return np.prod(new_array)
    



def solution_part_1():
    res = count_differences(input_data)
    return res[1] * res[3]


def solution_part_2():
    return count_arrangements(input_data)


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())

