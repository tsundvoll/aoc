import os
import time

import networkx as nx
import numpy as np
import pyperclip


def get_neighbor_ids(row, col, height, width, diagonal=False) -> list:
    neighbor_ids = []
    # Left
    if col > 0:
        neighbor_ids.append((row, col - 1))
    # Right
    if col < width - 1:
        neighbor_ids.append((row, col + 1))
    # Up
    if row > 0:
        neighbor_ids.append((row - 1, col))
    # Down
    if row < height - 1:
        neighbor_ids.append((row + 1, col))

    if diagonal:
        # Left and up
        if col > 0 and row > 0:
            neighbor_ids.append((row - 1, col - 1))
        # Left and down
        if col > 0 and row < height - 1:
            neighbor_ids.append((row + 1, col - 1))

    return neighbor_ids


def first_task(input_data):
    start_pos = None
    top_pos = None
    input_height = len(input_data)
    input_width = len(input_data[0])
    heightmap = np.zeros((input_height, input_width), dtype=int)
    G = nx.DiGraph()
    for row in range(input_height):
        for col in range(input_width):
            value = input_data[row][col]
            if value == "S":
                start_pos = (row, col)
                heightmap[row][col] = ord("a")
            elif value == "E":
                top_pos = (row, col)
                heightmap[row][col] = ord("z")
            else:
                heightmap[row][col] = ord(input_data[row][col])

    for row in range(input_height):
        for col in range(input_width):
            current_pos = (row, col)
            current_height = heightmap[row][col]
            neighbors = get_neighbor_ids(
                row,
                col,
                input_height,
                input_width,
            )
            for neighbor_pos in neighbors:
                neighbor_height = heightmap[neighbor_pos]
                if neighbor_height <= current_height + 1:
                    G.add_edge(current_pos, neighbor_pos)

    return nx.shortest_path_length(G, source=start_pos, target=top_pos)


def second_task(input_data):
    starting_locations = []
    start_pos = None
    top_pos = None
    input_height = len(input_data)
    input_width = len(input_data[0])
    heightmap = np.zeros((input_height, input_width), dtype=int)
    G = nx.DiGraph()
    for row in range(input_height):
        for col in range(input_width):
            value = input_data[row][col]
            if value == "S":
                starting_locations.append((row, col))
                heightmap[row][col] = ord("a")
            elif value == "E":
                top_pos = (row, col)
                heightmap[row][col] = ord("z")
            else:
                heightmap[row][col] = ord(input_data[row][col])

            if value == "a":
                starting_locations.append((row, col))

    for row in range(input_height):
        for col in range(input_width):
            current_pos = (row, col)
            current_height = heightmap[row][col]
            neighbors = get_neighbor_ids(
                row,
                col,
                input_height,
                input_width,
            )
            for neighbor_pos in neighbors:
                neighbor_height = heightmap[neighbor_pos]
                if neighbor_height <= current_height + 1:
                    G.add_edge(current_pos, neighbor_pos)

    shortest_paths = []
    for start_pos in starting_locations:
        try:
            shortest_paths.append(
                nx.shortest_path_length(G, source=start_pos, target=top_pos)
            )
        except:
            continue

    return min(shortest_paths)


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
