import os
import time

import networkx as nx
import numpy as np
import pyperclip


def first_task(input_data):
    count = 0
    x_max = 0
    y_max = 0
    z_max = 0
    for i in range(len(input_data)):
        x, y, z = list(map(int, input_data[i].split(",")))
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
        if z > z_max:
            z_max = z

    cubes = np.zeros((x_max + 1, y_max + 1, z_max + 1), dtype=int)
    cubes = np.pad(cubes, 1, mode="constant", constant_values=0)
    for i in range(len(input_data)):
        x, y, z = list(map(lambda n: int(n) + 1, input_data[i].split(",")))
        cubes[x][y][z] = 1

    for x in range(1, x_max + 2):
        for y in range(1, y_max + 2):
            for z in range(1, z_max + 2):
                if cubes[x][y][z] == 0:
                    continue

                neigbors = []
                neigbors.append((x - 1, y, z))
                neigbors.append((x + 1, y, z))
                neigbors.append((x, y - 1, z))
                neigbors.append((x, y + 1, z))
                neigbors.append((x, y, z - 1))
                neigbors.append((x, y, z + 1))

                local_count = 6
                for neigbor in neigbors:
                    if cubes[neigbor[0]][neigbor[1]][neigbor[2]] == 1:
                        local_count -= 1

                count += local_count

    assert np.count_nonzero(cubes) == len(input_data)
    return count


def second_task(input_data):
    G = nx.Graph()
    x_max = 0
    y_max = 0
    z_max = 0
    for i in range(len(input_data)):
        x, y, z = list(map(int, input_data[i].split(",")))
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
        if z > z_max:
            z_max = z

    cubes = np.zeros((x_max + 1, y_max + 1, z_max + 1), dtype=int)
    cubes = np.pad(cubes, 1, mode="constant", constant_values=0)
    for i in range(len(input_data)):
        x, y, z = list(map(lambda n: int(n) + 1, input_data[i].split(",")))
        cubes[x][y][z] = 1

    for x in range(1, x_max + 2):
        for y in range(1, y_max + 2):
            for z in range(1, z_max + 2):
                if cubes[x][y][z] == 1:
                    continue

                neigbors = []
                # x
                neigbors.append((x - 1, y, z))
                neigbors.append((x + 1, y, z))
                # y
                neigbors.append((x, y - 1, z))
                neigbors.append((x, y + 1, z))
                # z
                neigbors.append((x, y, z - 1))
                neigbors.append((x, y, z + 1))

                for neigbor in neigbors:
                    if cubes[neigbor[0]][neigbor[1]][neigbor[2]] == 0:
                        G.add_edge((x, y, z), (neigbor[0], neigbor[1], neigbor[2]))

    for x in range(0, x_max + 3):
        for y in range(0, y_max + 3):
            for z in range(0, z_max + 3):
                if (
                    x == 0
                    or x == x_max + 2
                    or y == 0
                    or y == y_max + 2
                    or z == 0
                    or z == z_max + 2
                ):
                    G.add_edge((0, 0, 0), (x, y, z))

    trapped_surfcae = 0
    for x in range(1, x_max + 2):
        for y in range(1, y_max + 2):
            for z in range(1, z_max + 2):
                if cubes[x][y][z] == 0:
                    try:
                        if nx.has_path(G, (0, 0, 0), (x, y, z)):
                            continue
                    except:
                        print(f"{(x, y, z)} not connected through air")
                    neigbors = []
                    # x
                    neigbors.append((x - 1, y, z))
                    neigbors.append((x + 1, y, z))
                    # y
                    neigbors.append((x, y - 1, z))
                    neigbors.append((x, y + 1, z))
                    # z
                    neigbors.append((x, y, z - 1))
                    neigbors.append((x, y, z + 1))

                    for neigbor in neigbors:
                        if cubes[neigbor[0]][neigbor[1]][neigbor[2]] == 1:
                            trapped_surfcae += 1

    assert np.count_nonzero(cubes) == len(input_data)
    surface_area = first_task(input_data) - trapped_surfcae
    return surface_area


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
