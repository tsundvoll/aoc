import os
import time

import matplotlib.pyplot as plt
import networkx as nx
import pyperclip


def first_task(input_data):
    count = 0
    G = nx.DiGraph()
    G_dirs = nx.DiGraph()
    dir_dict = {}
    current_dir = ""
    for i in range(len(input_data)):
        value: str = input_data[i]
        if value[0] == "$":  # Command
            command = value[2:4]
            if command == "ls":
                is_listing = True
            elif command == "cd":
                next_dir = value[5:]
                if next_dir == "..":
                    splitted_dirs = current_dir.split("/")
                    if len(splitted_dirs) == 2:
                        current_dir = "/"
                    else:
                        current_dir_len = len(splitted_dirs[-2]) + 1
                        current_dir = current_dir[:-current_dir_len]
                else:
                    if next_dir == "/":
                        current_dir = "/"
                    else:
                        current_dir = current_dir + next_dir + "/"
                is_listing = False
            else:
                raise RuntimeError
        elif is_listing:
            filetype, filename = value.split()
            if filetype.isdigit():
                size = int(filetype)
                next_file = current_dir + filename
                G.add_edge(current_dir, next_file, weight=size)
                if not current_dir in dir_dict.keys():
                    dir_dict[current_dir] = size
                else:
                    dir_dict[current_dir] += size
            else:
                next_dir = current_dir + filename + "/"
                G_dirs.add_edge(current_dir, next_dir)
                G.add_edge(current_dir, next_dir, weight=0)

    connections = []
    for connection in nx.bfs_successors(G_dirs, "/"):
        connections.append(connection)

    size_dict = {}
    for connection in reversed(connections):
        top_dir = connection[0]
        sub_dirs = connection[1]
        if not top_dir in size_dict.keys():
            try:
                size_dict[top_dir] = dir_dict[top_dir]
            except KeyError:
                size_dict[top_dir] = 0

        for sub_dir in sub_dirs:
            if sub_dir in size_dict.keys():
                size_dict[top_dir] += size_dict[sub_dir]
            else:
                try:
                    size_dict[top_dir] += dir_dict[sub_dir]
                except KeyError:
                    v = 0

    # Assign values to the dirs not containing other dirs
    for key in dir_dict.keys():
        if not key in size_dict.keys():
            size_dict[key] = dir_dict[key]

    for key, value in size_dict.items():
        if value <= 100000:
            count += value

    return count


def second_task(input_data):
    count = 0
    G = nx.DiGraph()
    G_dirs = nx.DiGraph()
    dir_dict = {}
    current_dir = ""
    for i in range(len(input_data)):
        value: str = input_data[i]
        if value[0] == "$":  # Command
            command = value[2:4]
            if command == "ls":
                is_listing = True
            elif command == "cd":
                next_dir = value[5:]
                if next_dir == "..":
                    splitted_dirs = current_dir.split("/")
                    if len(splitted_dirs) == 2:
                        current_dir = "/"
                    else:
                        current_dir_len = len(splitted_dirs[-2]) + 1
                        current_dir = current_dir[:-current_dir_len]
                else:
                    if next_dir == "/":
                        current_dir = "/"
                    else:
                        current_dir = current_dir + next_dir + "/"
                is_listing = False
            else:
                raise RuntimeError
        elif is_listing:
            filetype, filename = value.split()
            if filetype.isdigit():
                size = int(filetype)
                next_file = current_dir + filename
                G.add_edge(current_dir, next_file, weight=size)
                if not current_dir in dir_dict.keys():
                    dir_dict[current_dir] = size
                else:
                    dir_dict[current_dir] += size
            else:
                next_dir = current_dir + filename + "/"
                G_dirs.add_edge(current_dir, next_dir)
                G.add_edge(current_dir, next_dir, weight=0)

    connections = []
    for connection in nx.bfs_successors(G_dirs, "/"):
        connections.append(connection)

    size_dict = {}
    for connection in reversed(connections):
        top_dir = connection[0]
        sub_dirs = connection[1]
        if not top_dir in size_dict.keys():
            try:
                size_dict[top_dir] = dir_dict[top_dir]
            except KeyError:
                size_dict[top_dir] = 0

        for sub_dir in sub_dirs:
            if sub_dir in size_dict.keys():
                size_dict[top_dir] += size_dict[sub_dir]
            else:
                try:
                    size_dict[top_dir] += dir_dict[sub_dir]
                except KeyError:
                    v = 0

    # Assign values to the dirs not containing other dirs
    for key in dir_dict.keys():
        if not key in size_dict.keys():
            size_dict[key] = dir_dict[key]

    for key, value in size_dict.items():
        if value <= 100000:
            count += value

    unused_space = 70000000 - size_dict["/"]
    space_needed = 30000000 - unused_space

    lowest = min([v for v in size_dict.values() if v > space_needed])

    return lowest


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
