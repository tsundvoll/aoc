import math
import os
import time
from copy import deepcopy

import numpy as np
import pyperclip
from tqdm import tqdm


def visualize_platform(platform: list[str]):
    for row in platform:
        print(row)


def visualize_column(column: list[str]):
    print(column)


def tilt_column_once(column: list[str]):
    column_str = "".join(column)
    new_column = list(column_str.replace(".O", "O."))
    if tuple(column) == tuple(new_column):
        is_different = False
    else:
        is_different = True
    return new_column, is_different


def rotate_platform(platform: list[str]) -> list[str]:
    rotated_platform = []
    for column in zip(*platform):
        rotated_platform.append(column)
    return rotated_platform


def first_task(input_data: list[str]):
    count = 0
    platform = []
    for i in range(len(input_data)):
        platform.append(list(input_data[i]))

    # visualize_platform(platform)
    # print()

    rotated_platform = rotate_platform(platform)

    has_moved = False
    while True:
        platform_moved_once = []
        for column in rotated_platform:
            tilted_column, is_different = tilt_column_once(column)
            if is_different:
                has_moved = True
            platform_moved_once.append(tilted_column)

        rotated_platform = deepcopy(platform_moved_once)

        # visualize_platform(rotate_platform(rotated_platform))
        # print()
        # print(has_moved)

        if not has_moved:
            break

        has_moved = False

    rotated_back_platform = rotate_platform(rotated_platform)

    n_rows = len(rotated_back_platform)

    value = n_rows
    for row in rotated_back_platform:
        count += row.count("O") * value
        value -= 1

    return count


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
