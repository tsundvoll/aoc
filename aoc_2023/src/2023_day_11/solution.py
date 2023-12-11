import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data: list[str]):
    count = 1

    universe_rows = []
    for i in range(len(input_data)):
        value = input_data[i]
        is_empty = True
        universe_row = []
        for char in value:
            if char == ".":
                universe_row.append(0)
            else:
                is_empty = False
                universe_row.append(count)
                count += 1

        np_universe_row = np.array(universe_row)

        universe_rows.append(np_universe_row)
        if is_empty:
            universe_rows.append(np_universe_row)

    np_universe_rows = np.array(universe_rows)

    expanded_universe_transposed = []

    for col_id in range(np_universe_rows.shape[1]):
        np_col = np_universe_rows[:, col_id]
        expanded_universe_transposed.append(np_col)
        if np.sum(np_col) == 0:
            expanded_universe_transposed.append(np_col)

    expanded_universe_transposed = np.array(expanded_universe_transposed)
    expanded_universe = expanded_universe_transposed.T

    pairs = list((a, b) for a in range(1, count) for b in range(a, count) if a != b)

    total = 0
    for pair in tqdm(pairs):
        first_val, second_val = pair
        first_position = list(zip(*np.where(expanded_universe == first_val)))[0]
        second_position = list(zip(*np.where(expanded_universe == second_val)))[0]

        distance = abs(second_position[0] - first_position[0]) + abs(
            second_position[1] - first_position[1]
        )

        total += distance

    return total


def second_task(input_data: list):
    count = 1

    universe_rows = []
    for i in range(len(input_data)):
        value = input_data[i]
        universe_row = []
        for char in value:
            if char == ".":
                universe_row.append(0)
            else:
                universe_row.append(count)
                count += 1
        np_universe_row = np.array(universe_row)
        universe_rows.append(np_universe_row)

    np_universe = np.array(universe_rows)

    pairs = list((a, b) for a in range(1, count) for b in range(a, count) if a != b)

    total = 0
    expansion_rate = 1000000 - 1 if len(input_data[0]) > 10 else 10 - 1
    for pair in tqdm(pairs):
        first_val, second_val = pair
        first_position = list(zip(*np.where(np_universe == first_val)))[0]
        second_position = list(zip(*np.where(np_universe == second_val)))[0]

        first_pos_row = first_position[0]
        second_pos_row = second_position[0]

        first_pos_col = first_position[1]
        second_pos_col = second_position[1]

        if second_pos_row > first_pos_row:
            rows_between_positions = list(range(first_pos_row + 1, second_pos_row))
        elif second_pos_row < first_pos_row:
            rows_between_positions = list(range(second_pos_row + 1, first_pos_row))
        else:
            rows_between_positions = []

        if second_pos_col > first_pos_col:
            cols_between_positions = list(range(first_pos_col + 1, second_pos_col))
        elif second_pos_col < first_pos_col:
            cols_between_positions = list(range(second_pos_col + 1, first_pos_col))
        else:
            cols_between_positions = []

        n_row_expansions = 0
        for row in rows_between_positions:
            np_row = np_universe[row]
            if np.sum(np_row) == 0:
                n_row_expansions += 1

        n_col_expansions = 0
        for col in cols_between_positions:
            np_col = np_universe[:, col]
            if np.sum(np_col) == 0:
                n_col_expansions += 1

        row_distance = (
            abs(second_pos_row - first_pos_row) + n_row_expansions * expansion_rate
        )

        col_distance = (
            abs(second_pos_col - first_pos_col) + n_col_expansions * expansion_rate
        )

        distance = row_distance + col_distance

        total += distance

    return total


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
