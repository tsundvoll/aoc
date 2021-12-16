import math
import os
import time
from collections import defaultdict

import networkx as nx
import numpy as np
import pyperclip
from matplotlib import pyplot as plt
from networkx.generators import small
from utility import parse


def first_task(input):
    count = 0
    G = nx.Graph()
    large_caves = {}
    large_caves_to = {}
    for i, word in enumerate(input):
        a, b = word.split('-')
        for x in {a, b}:
            y = {a, b} - {x}
            if x.isupper():
                if x in large_caves:
                    n_x = len(large_caves[x])
                    X = x + '_' + str(n_x)
                    large_caves[x].append(X)
                    large_caves_to[x].append(list(y)[0])
                else:
                    X = x + '_0'
                    large_caves[x] = [X]
                    large_caves_to[x] = list(y)
                continue
        if a.islower() and b.islower():
            G.add_edge(a, b)

    for X in large_caves:
        L = large_caves[X]
        T = large_caves_to[X]
        for l in L:
            for t in T:
                G.add_edge(l, t)

    ps = nx.all_simple_paths(G, 'start', 'end')
    paths = set()
    for p in ps:
        path = []
        for n in p:
            N, *d = n.split('_')
            path.append(N)
        paths.add(tuple(path))
        count += 1

    return len(paths)


def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos)
    plt.show()


root = 'start'
goal = 'end'
small_caves = None
visited = defaultdict(lambda: 0)
def DFS(G, u, current_path = []):
    global visited

    path_count = 0
    if u.isupper():
        pass
    elif u != root and u.islower():
        n_twice = 0
        for sm in small_caves:
            if current_path.count(sm) > 1:
                n_twice += 1
        if n_twice > 1:
            return path_count

        if visited[u] == 1:
            for sm in small_caves:
                if current_path.count(sm) > 1:
                    return path_count
        elif visited[u] > 1:
            return path_count
    elif visited[u] != 0:
        return path_count

    visited[u] += 1

    current_path.append(u)

    if u == goal:
        visited[u] = 0
        n_twice = 0
        for sm in small_caves:
            if current_path.count(sm) > 1:
                n_twice += 1

        current_path.pop()
        return path_count + 1

    for n in G.neighbors(u):
        path_count += DFS(G, n, current_path)

    current_path.pop()

    visited[u] = 0

    return path_count


def second_task(input):
    global small_caves
    G = nx.Graph()
    for word in input:
        a, b = word.split('-')
        G.add_edge(a, b)

    small_caves = [
        n
        for n in list(G.nodes)
        if n != goal and n != root and n.islower()
    ]
    print(small_caves)

    count = DFS(G, 'start')

    return count


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

    # t_start = time.time()
    # first_answer = first_task(input_data)
    # t_end = time.time()
    # first_time = round(t_end - t_start, 2)
    # if first_answer is not None:
    #     pyperclip.copy(str(first_answer))
    #     pyperclip.paste()

    # print('#############################')
    # print('The answer to the 1st task is')
    # print(first_answer, f'in {first_time} seconds')

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
