import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


class Colors:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def visualize(area, highlight_idx=None):
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(len(area)):
        row = area[i]
        for j in range(len(row)):
            c = row[j]

            idx = np.array([i, j])

            if highlight_idx is not None and np.any(np.all(idx == highlight_idx)):
                color = Colors.YELLOW
                char = "o"
            else:
                color = ""
                if c == 1:
                    char = "#"
                else:
                    char = "."
            print(f"{color}{char}{Colors.ENDC}", end="")
        print()
    time.sleep(0.2)


def first_task(input_data: list[str]):
    count = 0
    area = []

    directions = [
        np.array([-1, 0]),
        np.array([0, 1]),
        np.array([1, 0]),
        np.array([0, -1]),
    ]
    for i in range(len(input_data)):
        input_line = input_data[i]
        row = []
        for j in range(len(input_line)):
            c = input_line[j]
            if c == "^":
                position = np.array([i, j])
            row.append(1 if c == "#" else 0)
        area.append(row)

    dir_idx = 0

    tuple_pos = (position[0], position[1])
    distinct_positions = set()
    distinct_positions.add(tuple_pos)

    while True:
        try_direction = directions[dir_idx]

        alt_dir_idx = (dir_idx + 1) % len(directions)
        alt_direction = directions[alt_dir_idx]

        try_position = position + try_direction
        alt_position = position + alt_direction

        try:
            value = area[try_position[0]][try_position[1]]
        except IndexError:
            break

        if value == 1:
            position = alt_position
            dir_idx = alt_dir_idx
        else:
            position = try_position

        # visualize(area, position)

        tuple_pos = (position[0], position[1])
        distinct_positions.add(tuple(tuple_pos))

    return len(distinct_positions)


def second_task(input_data: list[str]):
    count = 0
    for i in range(len(input_data)):
        input_line = input_data[i]
    return None


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
