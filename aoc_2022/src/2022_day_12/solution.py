import os
import time

import networkx as nx
import numpy as np
import pyperclip


def first_task(input_data):
    heightmap = np.zeros((len(input_data), len(input_data[0])), dtype=int)
    start_pos = None
    top_pos = None
    G = nx.DiGraph()
    for row in range(len(input_data)):
        for col in range(len(input_data[0])):
            value = input_data[row][col]
            if value == "S":
                start_pos = (row, col)
                heightmap[row][col] = ord("a")
            elif value == "E":
                top_pos = (row, col)
                heightmap[row][col] = ord("z")
            else:
                heightmap[row][col] = ord(input_data[row][col])

    for row in range(len(input_data)):
        for col in range(len(input_data[0])):
            current_pos = (row, col)
            current_height = heightmap[row][col]
            # Left
            if col > 0:
                left_height = heightmap[row][col - 1]
                left_pos = (row, col - 1)
                if left_height <= current_height + 1:
                    G.add_edge(current_pos, left_pos)
            # Right
            if col < len(input_data[0]) - 1:
                right_height = heightmap[row][col + 1]
                right_pos = (row, col + 1)
                if right_height <= current_height + 1:
                    G.add_edge(current_pos, right_pos)
            # Up
            if row > 0:
                up_height = heightmap[row - 1][col]
                up_pos = (row - 1, col)
                if up_height <= current_height + 1:
                    G.add_edge(current_pos, up_pos)
            # Down
            if row < len(input_data) - 1:
                down_height = heightmap[row + 1][col]
                down_pos = (row + 1, col)
                if down_height <= current_height + 1:
                    G.add_edge(current_pos, down_pos)

    return nx.shortest_path_length(G, source=start_pos, target=top_pos)


def second_task(input_data):
    heightmap = np.zeros((len(input_data), len(input_data[0])), dtype=int)
    starting_locations = []
    top_pos = None
    G = nx.DiGraph()
    for row in range(len(input_data)):
        for col in range(len(input_data[0])):
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

    for row in range(len(input_data)):
        for col in range(len(input_data[0])):
            current_pos = (row, col)
            current_height = heightmap[row][col]
            # Left
            if col > 0:
                left_height = heightmap[row][col - 1]
                left_pos = (row, col - 1)
                if left_height <= current_height + 1:
                    G.add_edge(current_pos, left_pos)
            # Right
            if col < len(input_data[0]) - 1:
                right_height = heightmap[row][col + 1]
                right_pos = (row, col + 1)
                if right_height <= current_height + 1:
                    G.add_edge(current_pos, right_pos)
            # Up
            if row > 0:
                up_height = heightmap[row - 1][col]
                up_pos = (row - 1, col)
                if up_height <= current_height + 1:
                    G.add_edge(current_pos, up_pos)
            # Down
            if row < len(input_data) - 1:
                down_height = heightmap[row + 1][col]
                down_pos = (row + 1, col)
                if down_height <= current_height + 1:
                    G.add_edge(current_pos, down_pos)

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
