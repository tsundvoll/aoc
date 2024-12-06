import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm

XMAS = ["X", "M", "A", "S"]


class Colors:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


directions = {
    "west": [np.array([0, -1]), np.array([0, -2]), np.array([0, -3])],
    "north-west": [np.array([-1, -1]), np.array([-2, -2]), np.array([-3, -3])],
    "north": [np.array([-1, 0]), np.array([-2, 0]), np.array([-3, 0])],
    "north-east": [np.array([-1, 1]), np.array([-2, 2]), np.array([-3, 3])],
    "east": [np.array([0, 1]), np.array([0, 2]), np.array([0, 3])],
    "south-east": [np.array([1, 1]), np.array([2, 2]), np.array([3, 3])],
    "south": [np.array([1, 0]), np.array([2, 0]), np.array([3, 0])],
    "south-west": [np.array([1, -1]), np.array([2, -2]), np.array([3, -3])],
}


def visualize(rows, highlight_green_idx=[], highlight_yellow_idx=[]):
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            c = row[j]

            idx = np.array([i, j])

            if len(highlight_green_idx) > 0 and np.any(
                np.all(idx == highlight_green_idx, axis=1)
            ):
                color = Colors.GREEN
            elif len(highlight_yellow_idx) > 0 and np.any(
                np.all(idx == highlight_yellow_idx, axis=1)
            ):
                color = Colors.YELLOW
            else:
                color = ""
            print(f"{color}{c}{Colors.ENDC}", end=" ")
        print()
    time.sleep(0.5)


def first_task(input_data: list[str]):
    count = 0
    rows = []
    X_idxs = []
    size = len(input_data)
    for i in range(len(input_data)):
        input_line = input_data[i]
        row = []
        for j in range(len(input_line)):
            c = input_line[j]
            if c == "X":
                X_idxs.append(np.array([i, j]))
            row.append(c)
        rows.append(np.array(row))
    rows = np.array(rows)

    all_green_idx = np.empty((1, 2))

    for X_idx in X_idxs:
        all_yellow_idx = np.array([X_idx])
        current_green_idx = np.array([])
        # visualize(rows, current_green_idx, all_yellow_idx)

        for dir, locations in directions.items():
            current_yellow_idx = np.array([X_idx])
            for loc in locations:
                current_yellow_idx = np.append(
                    current_yellow_idx, np.array([X_idx + loc]), axis=0
                )
                all_yellow_idx = np.append(
                    all_yellow_idx, np.array([X_idx + loc]), axis=0
                )
                # visualize(rows, current_green_idx, all_yellow_idx)

            is_xmas = True
            for y in range(len(current_yellow_idx)):
                yellow_idx = current_yellow_idx[y]

                if (
                    yellow_idx[0] < 0
                    or yellow_idx[0] >= size
                    or yellow_idx[1] < 0
                    or yellow_idx[1] >= size
                ):
                    is_xmas = False
                    continue

                char = rows[yellow_idx[0]][yellow_idx[1]]

                if y == 0 and char != "X":
                    is_xmas = False
                elif y == 1 and char != "M":
                    is_xmas = False
                elif y == 2 and char != "A":
                    is_xmas = False
                elif y == 3 and char != "S":
                    is_xmas = False

            if is_xmas:
                count += 1
                current_green_idx = np.append(
                    current_yellow_idx, np.array([X_idx + loc]), axis=0
                )
                all_green_idx = np.append(all_green_idx, current_green_idx, axis=0)
            # visualize(rows, current_green_idx, all_yellow_idx)
    # visualize(rows, all_green_idx)
    return count


def second_task(input_data: list[str]):
    count = 0
    rows = []
    A_idxs = []
    size = len(input_data)
    for i in range(len(input_data)):
        input_line = input_data[i]
        row = []
        for j in range(len(input_line)):
            c = input_line[j]
            if c == "A":
                A_idxs.append(np.array([i, j]))
            row.append(c)
        rows.append(np.array(row))
    rows = np.array(rows)

    check_forwards = [np.array([1, -1]), np.array([-1, 1])]
    check_backwards = [np.array([-1, -1]), np.array([1, 1])]

    for A_idx in A_idxs:
        first_forwards_idxs = A_idx + check_forwards[0]
        second_forwards_idxs = A_idx + check_forwards[1]

        first_backwards_idxs = A_idx + check_backwards[0]
        second_backwards_idxs = A_idx + check_backwards[1]

        idxs_to_check = [
            first_forwards_idxs,
            second_forwards_idxs,
            first_backwards_idxs,
            second_backwards_idxs,
        ]

        is_valid = True
        for idx_to_check in idxs_to_check:
            if (
                idx_to_check[0] < 0
                or idx_to_check[0] >= size
                or idx_to_check[1] < 0
                or idx_to_check[1] >= size
            ):
                is_valid = False

        if not is_valid:
            continue

        first_forwards = rows[first_forwards_idxs[0]][first_forwards_idxs[1]]
        second_forwards = rows[second_forwards_idxs[0]][second_forwards_idxs[1]]
        first_backwards = rows[first_backwards_idxs[0]][first_backwards_idxs[1]]
        second_backwards = rows[second_backwards_idxs[0]][second_backwards_idxs[1]]

        is_xmas = True
        if not (
            (first_forwards == "M" and second_forwards == "S")
            or (first_forwards == "S" and second_forwards == "M")
        ):
            is_xmas = False

        if not (
            (first_backwards == "M" and second_backwards == "S")
            or (first_backwards == "S" and second_backwards == "M")
        ):
            is_xmas = False

        if is_xmas:
            count += 1

    return count


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    # input_file = os.path.join(os.path.dirname(__file__), "test_input.txt")
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
