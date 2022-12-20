import copy
import itertools
import os
import time

import numpy as np
import pyperclip

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


def first_task(input_data, n_rocks=2022):
    width = 7
    start_height = 3
    max_rock_height = 4
    chamber = np.vstack([np.zeros((start_height, width), dtype=int), np.ones(7)])
    flows = itertools.cycle(
        [(-1, f_id) if f == "<" else (1, f_id) for f_id, f in enumerate(input_data[0])]
    )
    rocks = itertools.cycle(rock_ids)

    chamber_height = start_height
    for i_rock in range(n_rocks):
        rock = next(rocks)
        # print(f"The {i_rock+1}. rock begins falling")
        chamber = np.vstack([np.zeros((max_rock_height, width), dtype=int), chamber])
        chamber_height += max_rock_height
        # draw_chamber_with_rock(chamber, rock)

        while True:
            flow, flow_id = next(flows)
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


def second_task(n_rocks=1000000000000):
    true_height_for_test__ = 1514285714288

    first_interval_rocks = 520  # rocks
    first_interval_height = 813
    second_interval_rocks = 2265
    second_interval_height = 3563
    rocks_per_interval = second_interval_rocks - first_interval_rocks
    height_per_interval = second_interval_height - first_interval_height

    n_intervals = (n_rocks - first_interval_rocks) // rocks_per_interval

    calculated_rocks = first_interval_rocks + n_intervals * rocks_per_interval
    missing_rocks = n_rocks - calculated_rocks

    calculated_height = first_interval_height + n_intervals * height_per_interval

    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))
    missing_height = (
        first_task(input_data, n_rocks=first_interval_rocks + missing_rocks)
    ) - first_interval_height

    print(f"{rocks_per_interval=}")
    print(f"{height_per_interval=}")
    print(f"{n_intervals=}")
    print(f"{n_rocks=}")
    print(f"{calculated_rocks=}")
    print(f"{missing_rocks=}")
    print(f"{true_height_for_test__=}")

    height_after_intervals = calculated_height + missing_height
    return height_after_intervals


"""
rocks height flow_id
520 813 3027
1805 2832 396
2265 3563 3027
3550 5582 396
4010 6313 3027
5295 8332 396
5755 9063 3027
7040 11082 396
7500 11813 3027
"""


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    for n_rocks in [2022, 5000, 10000, 20000]:
        print(n_rocks, ":", first_task(input_data, n_rocks))

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
    second_answer = second_task()
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
