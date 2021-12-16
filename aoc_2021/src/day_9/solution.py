import itertools
import math
import os
import time

import networkx as nx
import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    m = []
    for i, word in enumerate(input):
        ns = np.array(list(map(int, word)))
        m.append(ns)

    m = np.array(m)
    low_points = []
    for row in range(len(m)):
        for col in range(len(m[0])):
            n = m[row][col]
            left_i = col - 1
            if left_i < 0:
                left = 11
            else:
                left = m[row][left_i]

            right_i = col + 1
            if right_i >= len(m[0]):
                right = 11
            else:
                right = m[row][right_i]

            up_i = row - 1
            if up_i < 0:
                up = 11
            else:
                up = m[up_i][col]

            down_i = row + 1
            if down_i >= len(m):
                down = 11
            else:
                down = m[down_i][col]

            if left > n and right > n and up > n and down > n:
                low_points.append(n + 1)

    risk = sum(low_points)

    return risk

def second_task(input):
    m = []
    for i, word in enumerate(input):
        ns = np.array(list(map(int, word)))
        m.append(ns)
    
    m = np.array(m)

    low_points = []

    G=nx.Graph()
    low_point_nodes = []

    for row in range(len(m)):
        for col in range(len(m[0])):
            n = m[row][col]
            left_i = col - 1
            if left_i < 0:
                left = 9
            else:
                left = m[row][left_i]
            
            if left > n and left != 9:
                G.add_edge(
                    str((row, left_i)),
                    str((row, col))
                )

            right_i = col + 1
            if right_i >= len(m[0]):
                right = 9
            else:
                right = m[row][right_i]
            if right > n and right != 9:
                G.add_edge(
                    str((row, right_i)),
                    str((row, col))
                )

            up_i = row - 1
            if up_i < 0:
                up = 9
            else:
                up = m[up_i][col]
            if up > n and up != 9:
                G.add_edge(
                    str((up_i, col)),
                    str((row, col))
                )

            down_i = row + 1
            if down_i >= len(m):
                down = 9
            else:
                down = m[down_i][col]
            if down > n and down != 9:
                G.add_edge(
                    str((down_i, col)),
                    str((row, col))
                )

            if left > n and right > n and up > n and down > n:
                low_point_nodes.append(str((row, col)))
                low_points.append(n + 1)

    basins = [
        len(nx.node_connected_component(G, node))
        for node in low_point_nodes
    ]

    basins.sort()
    return math.prod(basins[-3:])


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()
