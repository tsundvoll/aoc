import math
import os
import time
from collections import defaultdict

import numpy as np
import pyperclip


def draw_grove(elves):
    min_row = math.inf
    max_row = -math.inf
    min_col = math.inf
    max_col = -math.inf

    for elf in elves:
        elf_row, elf_col = elf
        if elf_row < min_row:
            min_row = elf_row
        if elf_row > max_row:
            max_row = elf_row

        if elf_col < min_col:
            min_col = elf_col
        if elf_col > max_col:
            max_col = elf_col

    height = max_row - min_row + 1
    width = max_col - min_col + 1

    grove = np.zeros((height, width), dtype=int)

    for elf in elves:
        elf_row, elf_col = elf
        grove_row = elf_row - min_row
        grove_col = elf_col - min_col

        grove[grove_row][grove_col] = 1

    print()
    for row in grove:
        for col in row:
            print("#" if col else ".", end="")
        print()

    return np.count_nonzero(grove == 0)


def check_position(check_positions, elves):
    for check_pos in check_positions:
        if check_pos in elves:
            return None
    return check_positions[0]


def get_proposal(elf, elves, start_direction=0):
    elf_row, elf_col = elf

    north_west = (elf_row - 1, elf_col - 1)
    north = (elf_row - 1, elf_col)
    north_east = (elf_row - 1, elf_col + 1)

    east = (elf_row, elf_col + 1)

    south_east = (elf_row + 1, elf_col + 1)
    south = (elf_row + 1, elf_col)
    south_west = (elf_row + 1, elf_col - 1)

    west = (elf_row, elf_col - 1)

    check_positions_north = [north, north_east, north_west]
    check_positions_south = [south, south_east, south_west]
    check_positions_west = [west, north_west, south_west]
    check_positions_east = [east, north_east, south_east]

    check_positions_in_dir = [
        check_positions_north,
        check_positions_south,
        check_positions_west,
        check_positions_east,
    ]

    # Check all eight positions adjacent to the elf
    is_adjacent_empty = True
    for check_pos in [
        north_west,
        north,
        north_east,
        east,
        south_east,
        south,
        south_west,
        west,
    ]:
        if check_pos in elves:
            is_adjacent_empty = False
    if is_adjacent_empty:
        return None

    dir_id = start_direction
    for _ in range(4):
        proposal = check_position(check_positions_in_dir[dir_id], elves)
        if not proposal is None:
            return proposal
        dir_id = (dir_id + 1) % 4

    return None


def first_task(input_data):
    elves = []
    for row in range(len(input_data)):
        value = input_data[row]
        for col, char in enumerate(value):
            if char == "#":
                elf_position = (row, col)
                elves.append(elf_position)

    dir_id = 0

    for _ in range(10):
        proposals = defaultdict(list)
        for elf in elves:
            proposal = get_proposal(elf, elves, start_direction=dir_id)
            if not proposal is None:
                proposals[proposal].append(elf)

        for proposed_destination, proposed_origins in proposals.items():
            if len(proposed_origins) == 1:
                elves.remove(proposed_origins[0])
                elves.append(proposed_destination)

        n_empty_ground_tiles = draw_grove(elves)
        dir_id = (dir_id + 1) % 4

    # 4254 in 10.03 seconds

    return n_empty_ground_tiles


def second_task(input_data):
    count = 0
    elves = []
    for row in range(len(input_data)):
        value = input_data[row]
        for col, char in enumerate(value):
            if char == "#":
                elf_position = (row, col)
                elves.append(elf_position)

    dir_id = 0

    while True:
        proposals = defaultdict(list)
        for elf in elves:
            proposal = get_proposal(elf, elves, start_direction=dir_id)
            if not proposal is None:
                proposals[proposal].append(elf)

        should_stop = True
        for proposed_destination, proposed_origins in proposals.items():
            should_stop = False
            if len(proposed_origins) == 1:
                elves.remove(proposed_origins[0])
                elves.append(proposed_destination)

        count += 1
        dir_id = (dir_id + 1) % 4

        if should_stop:
            break

    # 992 in 1132.197 seconds

    return count


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
