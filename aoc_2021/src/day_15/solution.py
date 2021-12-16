import math
import os
import time

import networkx as nx
import numpy as np
import pyperclip
from networkx.algorithms.assortativity import neighbor_degree
from networkx.algorithms.assortativity.pairs import node_attribute_xy
from networkx.readwrite.edgelist import read_weighted_edgelist
from utility import parse


def first_task(input):
    count = 0
    risk_map = []
    for i, word in enumerate(input):
        line = []
        for c in word:
            line.append(int(c))
        risk_map.append(line)
    
    size = len(line)

    G = nx.DiGraph()
    for row in range(size):
        for col in range(size):
            node = f'{row}, {col}'
            if row == 0 and col == 0:
                node = 'start'
            elif row == size - 1 and col == size - 1:
                node = 'end'

            neighbors = [
                f'{row}, {col - 1}' if col - 1 > 0 else None,
                f'{row}, {col + 1}' if col + 1 < size else None,
                f'{row - 1}, {col}' if row - 1 > 0 else None,
                f'{row + 1}, {col}' if row + 1 < size else None,
            ]

            for n in neighbors:
                if n is None:
                    continue
                
                r, c = map(int, (n.split(', ')))

                n_weight = int(risk_map[r][c])

                if r == size - 1 and c == size - 1:
                    n = 'end'

                G.add_weighted_edges_from([(node, n, n_weight)])

    shortest_path = nx.shortest_path(G, source='start', target='end', weight='weight')

    print(shortest_path)
    for i in range(len(shortest_path) - 1):
        f = shortest_path[i]
        t = shortest_path[i+1]
        count += G[f][t]["weight"]

    return count


def second_task(input):
    count = 0
    risk_map = []
    for i, word in enumerate(input):
        line = []
        for c in word:
            line.append(int(c))
        risk_map.append(np.array(line))
    
    risk_map = np.array(risk_map)

    risk_cell = risk_map.copy()
    for _ in range(4):
        risk_cell = risk_cell + 1
        risk_cell[np.nonzero(risk_cell > 9)] = 1
        risk_map = np.concatenate((risk_map, risk_cell), axis=1)
    
    risk_cell = risk_map.copy()
    for _ in range(4):
        risk_cell = risk_cell + 1
        risk_cell[np.nonzero(risk_cell > 9)] = 1
        risk_map = np.concatenate((risk_map, risk_cell), axis=0)

    size = len(line)*5

    G = nx.DiGraph()
    for row in range(size):
        for col in range(size):
            node = f'{row}, {col}'
            if row == 0 and col == 0:
                node = 'start'
            elif row == size - 1 and col == size - 1:
                node = 'end'

            neighbors = [
                f'{row}, {col - 1}' if col - 1 > 0 else None,
                f'{row}, {col + 1}' if col + 1 < size else None,
                f'{row - 1}, {col}' if row - 1 > 0 else None,
                f'{row + 1}, {col}' if row + 1 < size else None,
            ]

            for n in neighbors:
                if n is None:
                    continue
                
                r, c = map(int, (n.split(', ')))

                n_weight = int(risk_map[r][c])

                if r == size - 1 and c == size - 1:
                    n = 'end'

                G.add_weighted_edges_from([(node, n, n_weight)])

    shortest_path = nx.shortest_path(G, source='start', target='end', weight='weight')

    for i in range(len(shortest_path) - 1):
        f = shortest_path[i]
        t = shortest_path[i+1]
        count += G[f][t]["weight"]

    return count


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

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()
