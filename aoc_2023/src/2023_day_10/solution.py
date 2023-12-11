import math
import os
import time

import networkx as nx
import numpy as np
import pyperclip
from tqdm import tqdm

"""
.....
.F-7.
.|.|.
.L-J.
.....
"""


def first_task(input_data: list):
    count = 0

    G = nx.Graph()
    S = None
    for row in range(len(input_data)):
        row_value = input_data[row]
        for col in range(len(row_value)):
            tile = input_data[row][col]
            tile_id = (row, col)
            above_id = (row - 1, col)
            below_id = (row + 1, col)
            left_id = (row, col - 1)
            right_id = (row, col + 1)

            def add_above(G: nx.Graph, tile_id, above_id):
                if above_id[0] >= 0:
                    above_value = input_data[above_id[0]][above_id[1]]
                    if above_value in ["-", "L", "J"]:
                        return
                    G.add_edge(tile_id, above_id)

            def add_below(G: nx.Graph, tile_id, below_id):
                if below_id[0] < len(input_data):
                    below_value = input_data[below_id[0]][below_id[1]]
                    if below_value in ["-", "F", "7"]:
                        return
                    G.add_edge(tile_id, below_id)

            def add_left(G: nx.Graph, tile_id, left_id):
                if left_id[1] >= 0:
                    below_value = input_data[left_id[0]][left_id[1]]
                    if below_value in ["|", "J", "7"]:
                        return
                    G.add_edge(tile_id, left_id)

            def add_right(G: nx.Graph, tile_id, right_id):
                if right_id[1] < len(input_data[0]):
                    below_value = input_data[right_id[0]][right_id[1]]
                    if below_value in ["|", "L", "F"]:
                        return
                    G.add_edge(tile_id, right_id)

            if tile == "|":
                add_above(G, tile_id, above_id)
                add_below(G, tile_id, below_id)
            elif tile == "-":
                add_left(G, tile_id, left_id)
                add_right(G, tile_id, right_id)
            elif tile == "L":
                add_above(G, tile_id, above_id)
                add_right(G, tile_id, right_id)
            elif tile == "J":
                add_above(G, tile_id, above_id)
                add_left(G, tile_id, left_id)
            elif tile == "7":
                add_left(G, tile_id, left_id)
                add_below(G, tile_id, below_id)
            elif tile == "F":
                add_right(G, tile_id, right_id)
                add_below(G, tile_id, below_id)
            elif tile == "S":
                S = (row, col)
                print(f"{S=}")
            else:
                if tile != ".":
                    raise ValueError

    height = len(input_data)
    width = len(input_data[0])

    display = np.zeros((height, width), dtype=str)
    display[True] = "."

    start_neighbors = list(G.neighbors(S))

    assert len(start_neighbors) == 2
    display[S] = "S"
    next_node = start_neighbors[0]
    prev_node = S
    while next_node != S:
        display[next_node] = str(count)
        tmp = next_node
        neighbors_of_next = list(G.neighbors(next_node))
        next_candidates = [n for n in neighbors_of_next if n != prev_node]
        if len(next_candidates) > 1:
            best_candidate = None
            shortest_path = math.inf
            for next_candidate in next_candidates:
                G_copy = G.copy()
                G_copy.remove_node(next_node)
                try:
                    path_length = len(nx.shortest_path(G_copy, S, next_candidate))
                except nx.exception.NetworkXNoPath:
                    continue
                if path_length < shortest_path:
                    best_candidate = next_candidate
                    shortest_path = path_length
            next_node = best_candidate
        else:
            next_node = next_candidates[0]
        prev_node = tmp
        count += 1

    return (count + 1) / 2


"""
-L|F7
7S-7|
L|7||
-L-J|
L|-JF

.....
.S-7.
.|.|.
.L-J.
.....

..F7.
.FJ|.
SJ.L7
|F--J
LJ...

7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ

..45.
.236.
01.78
14567
23...


"""


def second_task(input_data: list):
    count = 0

    G = nx.Graph()
    S = None
    for row in range(len(input_data)):
        row_value = input_data[row]
        for col in range(len(row_value)):
            tile = input_data[row][col]
            tile_id = (row, col)
            above_id = (row - 1, col)
            below_id = (row + 1, col)
            left_id = (row, col - 1)
            right_id = (row, col + 1)

            def add_above(G: nx.Graph, tile_id, above_id):
                if above_id[0] >= 0:
                    above_value = input_data[above_id[0]][above_id[1]]
                    if above_value in ["-", "L", "J"]:
                        return
                    G.add_edge(tile_id, above_id)

            def add_below(G: nx.Graph, tile_id, below_id):
                if below_id[0] < len(input_data):
                    below_value = input_data[below_id[0]][below_id[1]]
                    if below_value in ["-", "F", "7"]:
                        return
                    G.add_edge(tile_id, below_id)

            def add_left(G: nx.Graph, tile_id, left_id):
                if left_id[1] >= 0:
                    below_value = input_data[left_id[0]][left_id[1]]
                    if below_value in ["|", "J", "7"]:
                        return
                    G.add_edge(tile_id, left_id)

            def add_right(G: nx.Graph, tile_id, right_id):
                if right_id[1] < len(input_data[0]):
                    below_value = input_data[right_id[0]][right_id[1]]
                    if below_value in ["|", "L", "F"]:
                        return
                    G.add_edge(tile_id, right_id)

            if tile == "|":
                add_above(G, tile_id, above_id)
                add_below(G, tile_id, below_id)
            elif tile == "-":
                add_left(G, tile_id, left_id)
                add_right(G, tile_id, right_id)
            elif tile == "L":
                add_above(G, tile_id, above_id)
                add_right(G, tile_id, right_id)
            elif tile == "J":
                add_above(G, tile_id, above_id)
                add_left(G, tile_id, left_id)
            elif tile == "7":
                add_left(G, tile_id, left_id)
                add_below(G, tile_id, below_id)
            elif tile == "F":
                add_right(G, tile_id, right_id)
                add_below(G, tile_id, below_id)
            elif tile == "S":
                S = (row, col)
            else:
                if tile != ".":
                    raise ValueError

    height = len(input_data)
    width = len(input_data[0])

    display = np.zeros((height, width), dtype=str)
    display[True] = "."

    start_neighbors = list(G.neighbors(S))

    assert len(start_neighbors) == 2
    display[S] = "S"
    next_node = start_neighbors[0]
    prev_node = S

    nodes_in_loop = [S]

    while next_node != S:
        nodes_in_loop.append(next_node)
        display[next_node] = str(count)
        tmp = next_node
        display[next_node] = str(count)
        neighbors_of_next = list(G.neighbors(next_node))
        next_candidates = [n for n in neighbors_of_next if n != prev_node]
        if len(next_candidates) > 1:
            best_candidate = None
            shortest_path = math.inf
            for next_candidate in next_candidates:
                G_copy = G.copy()
                G_copy.remove_node(next_node)
                try:
                    path_length = len(nx.shortest_path(G_copy, S, next_candidate))
                except nx.exception.NetworkXNoPath:
                    continue
                if path_length < shortest_path:
                    best_candidate = next_candidate
                    shortest_path = path_length
            next_node = best_candidate
        else:
            next_node = next_candidates[0]
        prev_node = tmp
        count += 1

    start_node = nodes_in_loop[0]
    first_node = nodes_in_loop[1]
    node_char = input_data[first_node[0]][first_node[1]]

    def get_direction(first_node, second_node):
        start_dir_vertical = second_node[0] - first_node[0]
        start_dir_horizontal = second_node[1] - first_node[1]

        if start_dir_vertical == 1:
            direction = "down"
        elif start_dir_vertical == -1:
            direction = "up"
        elif start_dir_horizontal == 1:
            direction = "right"
        elif start_dir_horizontal == -1:
            direction = "left"
        else:
            return RuntimeError
        return direction

    def get_left(node):
        return (node[0], node[1] - 1)

    def get_right(node):
        return (node[0], node[1] + 1)

    def get_above(node):
        return (node[0] - 1, node[1])

    def get_below(node):
        return (node[0] + 1, node[1])

    left_side_nodes = []
    right_side_nodes = []

    def add_to_left_side(node):
        if not node in nodes_in_loop:
            print(f"Adding {node} to the left")
            left_side_nodes.append(node)

    def add_to_right_side(node):
        if not node in nodes_in_loop:
            print(f"Adding {node} to the right")
            right_side_nodes.append(node)

    start_dir = get_direction(start_node, nodes_in_loop[1])
    end_dir = get_direction(nodes_in_loop[-1], start_node)

    left = get_left(start_node)
    right = get_right(start_node)
    above = get_above(start_node)
    below = get_below(start_node)

    if end_dir == "up" and start_dir == "left":  # 7, up
        add_to_right_side(right)
        add_to_right_side(above)
    elif end_dir == "up" and start_dir == "up":  # |, up
        add_to_left_side(left)
        add_to_right_side(right)
    elif end_dir == "up" and start_dir == "right":  # F, up
        add_to_left_side(left)
        add_to_left_side(above)

    elif end_dir == "right" and start_dir == "up":  # J, right
        add_to_right_side(below)
        add_to_right_side(right)
    elif end_dir == "right" and start_dir == "right":  # -, right
        add_to_left_side(above)
        add_to_right_side(below)
    elif end_dir == "right" and start_dir == "down":  # 7, right
        add_to_left_side(above)
        add_to_left_side(right)

    elif end_dir == "down" and start_dir == "right":  # L, down
        add_to_right_side(below)
        add_to_right_side(left)
    elif end_dir == "down" and start_dir == "down":  # |, down
        add_to_left_side(right)
        add_to_right_side(left)
    elif end_dir == "down" and start_dir == "left":  # J, down
        add_to_left_side(below)
        add_to_left_side(right)

    elif end_dir == "left" and start_dir == "down":  # F, left
        add_to_right_side(left)
        add_to_right_side(above)
    elif end_dir == "left" and start_dir == "left":  # -, left
        add_to_left_side(below)
        add_to_right_side(above)
    elif end_dir == "left" and start_dir == "up":  # L, left
        add_to_left_side(below)
        add_to_left_side(left)
    else:
        raise RuntimeError

    prev_node = start_node
    for node in nodes_in_loop[1:]:
        direction = get_direction(prev_node, node)

        left = get_left(node)
        right = get_right(node)
        above = get_above(node)
        below = get_below(node)

        node_char = input_data[node[0]][node[1]]
        if node_char == "-":
            if direction == "right":  # -, right
                add_to_left_side(above)
                add_to_right_side(below)
            elif direction == "left":  # -, left
                add_to_left_side(below)
                add_to_right_side(above)
            else:
                raise RuntimeError
        elif node_char == "7":
            if direction == "right":  # 7, right
                add_to_left_side(above)
                add_to_left_side(right)
            elif direction == "up":  # 7, up
                add_to_right_side(above)
                add_to_right_side(right)
            else:
                raise RuntimeError
        elif node_char == "|":
            if direction == "down":  # |, down
                add_to_left_side(right)
                add_to_right_side(left)
            elif direction == "up":  # |, up
                add_to_left_side(left)
                add_to_right_side(right)
            else:
                raise RuntimeError
        elif node_char == "L":
            if direction == "left":  # L, left
                add_to_left_side(below)
                add_to_left_side(left)
            elif direction == "down":  # L, down
                add_to_right_side(below)
                add_to_right_side(left)
            else:
                raise RuntimeError
        elif node_char == "F":
            if direction == "up":  # F, up
                add_to_left_side(left)
                add_to_left_side(above)
            elif direction == "left":  # F, left
                add_to_right_side(left)
                add_to_right_side(above)
            else:
                raise RuntimeError
        elif node_char == "J":
            if direction == "right":  # J, right
                add_to_right_side(below)
                add_to_right_side(right)
            elif direction == "down":  # J, down
                add_to_left_side(below)
                add_to_left_side(right)
            else:
                raise RuntimeError
        else:
            raise RuntimeError
        prev_node = node

    G_surroundings = nx.Graph()

    def add_to_G(node, neighbor):
        if (
            not node in nodes_in_loop
            and not neighbor in nodes_in_loop
            and (neighbor[0] > 0 and neighbor[0] < len(input_data))
            and (neighbor[1] > 0 and neighbor[1] < len(input_data[0]))
        ):
            G_surroundings.add_edge(node, neighbor)

    for row in tqdm(range(len(input_data))):
        row_value = input_data[row]
        for col in range(len(row_value)):
            tile = (row, col)
            add_to_G(tile, get_left(tile))
            add_to_G(tile, get_right(tile))
            add_to_G(tile, get_above(tile))
            add_to_G(tile, get_below(tile))

    n_left_side = len(set(left_side_nodes))
    n_right_side = len(set(right_side_nodes))
    inner_side = (
        set(left_side_nodes) if n_left_side < n_right_side else set(right_side_nodes)
    )

    inner_area = inner_side.copy()

    for node in inner_side:
        try:
            connected_nodes = nx.node_connected_component(G_surroundings, node)
        except KeyError:
            continue
        inner_area |= connected_nodes

    return len(inner_area)


"""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
