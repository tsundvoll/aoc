import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data):
    count = 0
    moves = []
    on_moves = True
    on_ids = False
    on_containers = False
    n_containers = None
    containers = []
    for i in range(len(input_data) - 1, -1, -1):
        value = input_data[i]
        if value == "\n" or value == "":
            on_moves = False
            on_ids = True
            continue

        if on_moves:
            try:
                _, rest = value.split("move ")
                n, rest = rest.split(" from ")
                start, end = rest.split(" to ")
                moves.append([int(n), int(start), int(end)])
            except Exception as e:
                print(value, e)

        if on_ids:
            ids = [int(n) for n in value.split(" ") if n != ""]
            n_containers = ids[-1]

            for i in ids:
                containers.append([i])

            on_ids = False
            on_containers = True
            continue

        if on_containers:
            for i in range(1, n_containers + 1):
                container = value[(i - 1) * 4 : i * 4]
                if "[" in container:
                    containers[i - 1].append(container[1])

    for move in reversed(moves):
        n_moves = move[0]
        start = move[1]
        end = move[2]

        print(move)
        print(containers[start - 1])
        print(containers[end - 1])
        for _ in range(n_moves):
            try:
                containers[end - 1].append(containers[start - 1].pop())
            except:
                continue
            print(containers[start - 1])
            print(containers[end - 1])
        print()

    word = ""
    for container in containers:
        word += container[-1]

    return word


def second_task(input_data):
    count = 0
    moves = []
    on_moves = True
    on_ids = False
    on_containers = False
    n_containers = None
    containers = []
    for i in range(len(input_data) - 1, -1, -1):
        value = input_data[i]
        if value == "\n" or value == "":
            on_moves = False
            on_ids = True
            continue

        if on_moves:
            try:
                _, rest = value.split("move ")
                n, rest = rest.split(" from ")
                start, end = rest.split(" to ")
                moves.append([int(n), int(start), int(end)])
            except Exception as e:
                print(value, e)

        if on_ids:
            ids = [int(n) for n in value.split(" ") if n != ""]
            n_containers = ids[-1]

            for i in ids:
                containers.append([i])

            on_ids = False
            on_containers = True
            continue

        if on_containers:
            for i in range(1, n_containers + 1):
                container = value[(i - 1) * 4 : i * 4]
                if "[" in container:
                    containers[i - 1].append(container[1])

    for move in reversed(moves):
        n_moves = move[0]
        start = move[1]
        end = move[2]

        print(move)
        print(containers[start - 1])
        print(containers[end - 1])
        containers[end - 1].extend(containers[start - 1][-n_moves:])
        for _ in range(n_moves):
            containers[start - 1].pop()
        print(containers[start - 1])
        print(containers[end - 1])
        print()

    word = ""
    for container in containers:
        word += container[-1]

    return word


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(open(input_file, "r"))

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
