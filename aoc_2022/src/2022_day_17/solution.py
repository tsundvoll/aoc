import copy
import itertools
import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm

rocks = [
    np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0],
        ]
    ),
    np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ]
    ),
    np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
        ]
    ),
    np.array(
        [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ]
    ),
    np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
        ]
    ),
]

rock_ids = [
    [[3, 2], [3, 3], [3, 4], [3, 5]],
    [[1, 3], [2, 2], [2, 3], [2, 4], [3, 3]],
    [[1, 4], [2, 4], [3, 2], [3, 3], [3, 4]],
    [[0, 2], [1, 2], [2, 2], [3, 2]],
    [[2, 2], [2, 3], [3, 2], [3, 3]],
]
"""####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""


""" Rules
Alternate between:
* being pushed by a jet of hot gas one unit
* falling one unit down

* if flow movement -> collision, don't
* if downward falling -> collision, stop

"""


def draw_chamber_with_rock(chamber, rock):
    chamber_with_rock = copy.deepcopy(chamber)
    for pixel in rock:
        chamber_with_rock[pixel[0]][pixel[1]] = 1
    print(chamber_with_rock)


def first_task(input_data):
    count = 0
    width = 7
    start_height = 3
    max_rock_height = 4
    chamber = np.vstack([np.zeros((start_height, width), dtype=int), np.ones(7)])
    flows = itertools.cycle([-1 if f == "<" else 1 for f in input_data[0]])
    rocks = itertools.cycle(rock_ids)

    chamber_height = start_height
    for i_rock in range(4044):
        rock = next(rocks)
        # print(f"The {i_rock+1}. rock begins falling")
        chamber = np.vstack([np.zeros((max_rock_height, width), dtype=int), chamber])
        chamber_height += max_rock_height
        # draw_chamber_with_rock(chamber, rock)

        while True:
            flow = next(flows)
            possible_rock_after_flow = copy.deepcopy(rock)
            will_move_with_flow = True
            for pixel in possible_rock_after_flow:
                pixel[1] += flow
                if pixel[1] < 0 or pixel[1] >= width or chamber[pixel[0]][pixel[1]] > 0:
                    # Don't move with flow
                    will_move_with_flow = False
                    break

            if will_move_with_flow:
                rock = copy.deepcopy(possible_rock_after_flow)
                # print(f"Jet of gas pushes rock {'right' if flow == 1 else 'left'}:")
                # draw_chamber_with_rock(chamber, rock)
            # else:
            #     print(
            #         f"Jet of gas pushes rock {'right' if flow else 'left'}"
            #         f", but nothing happens:"
            #     )
            #     draw_chamber_with_rock(chamber, rock)

            possible_rock_after_downfall = copy.deepcopy(rock)
            will_fall_down = True
            for pixel in possible_rock_after_downfall:
                pixel[0] += 1
                if pixel[0] >= len(chamber) or chamber[pixel[0]][pixel[1]] > 0:
                    # Don't fall down; stop where the rock is
                    will_fall_down = False
                    break

            if will_fall_down:
                rock = copy.deepcopy(possible_rock_after_downfall)
                # print("Rock falls 1 unit")
                # draw_chamber_with_rock(chamber, rock)
            else:
                for pixel in rock:
                    chamber[pixel[0]][pixel[1]] = 1
                # print("Rock falls 1 unit, causing it to come to rest:")
                # print(chamber)
                # print()
                break

        empty_first_line = not chamber[0].any()
        while empty_first_line and len(chamber) > 1:
            chamber = chamber[1:]
            chamber_height -= 1
            empty_first_line = not chamber[0].any()

        if chamber[0].all():
            print(i_rock, len(chamber))
        chamber = np.vstack([np.zeros((3, width), dtype=int), chamber])
        chamber_height += 3

    empty_first_line = not chamber[0].any()
    while empty_first_line and len(chamber) > 1:
        chamber = chamber[1:]
        chamber_height -= 1
        empty_first_line = not chamber[0].any()
    return len(chamber) - 1


def second_task(input_data):
    return None
    width = 7
    start_height = 3
    max_rock_height = 4
    chamber = np.vstack([np.zeros((start_height, width), dtype=int), np.ones(7)])
    flows = itertools.cycle([-1 if f == "<" else 1 for f in input_data[0]])
    rocks = itertools.cycle(rock_ids)

    chamber_height = start_height
    for i_rock in range(2022):
        rock = next(rocks)
        # print(f"The {i_rock+1}. rock begins falling")
        chamber = np.vstack([np.zeros((max_rock_height, width), dtype=int), chamber])
        chamber_height += max_rock_height
        # draw_chamber_with_rock(chamber, rock)

        while True:
            flow = next(flows)
            possible_rock_after_flow = copy.deepcopy(rock)
            will_move_with_flow = True
            for pixel in possible_rock_after_flow:
                pixel[1] += flow
                if pixel[1] < 0 or pixel[1] >= width or chamber[pixel[0]][pixel[1]] > 0:
                    # Don't move with flow
                    will_move_with_flow = False
                    break

            if will_move_with_flow:
                rock = copy.deepcopy(possible_rock_after_flow)
                # print(f"Jet of gas pushes rock {'right' if flow == 1 else 'left'}:")
                # draw_chamber_with_rock(chamber, rock)
            # else:
            #     print(
            #         f"Jet of gas pushes rock {'right' if flow else 'left'}"
            #         f", but nothing happens:"
            #     )
            #     draw_chamber_with_rock(chamber, rock)

            possible_rock_after_downfall = copy.deepcopy(rock)
            will_fall_down = True
            for pixel in possible_rock_after_downfall:
                pixel[0] += 1
                if pixel[0] >= len(chamber) or chamber[pixel[0]][pixel[1]] > 0:
                    # Don't fall down; stop where the rock is
                    will_fall_down = False
                    break

            if will_fall_down:
                rock = copy.deepcopy(possible_rock_after_downfall)
                # print("Rock falls 1 unit")
                # draw_chamber_with_rock(chamber, rock)
            else:
                for pixel in rock:
                    chamber[pixel[0]][pixel[1]] = 1
                # print("Rock falls 1 unit, causing it to come to rest:")
                # print(chamber)
                # print()
                break

        empty_first_line = not chamber[0].any()
        while empty_first_line and len(chamber) > 1:
            chamber = chamber[1:]
            chamber_height -= 1
            empty_first_line = not chamber[0].any()
        chamber = np.vstack([np.zeros((3, width), dtype=int), chamber])
        chamber_height += 3

    empty_first_line = not chamber[0].any()
    while empty_first_line and len(chamber) > 1:
        chamber = chamber[1:]
        chamber_height -= 1
        empty_first_line = not chamber[0].any()
    return len(chamber) - 1


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
