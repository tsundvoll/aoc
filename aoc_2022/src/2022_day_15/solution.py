import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data):
    # return 26
    x_min = math.inf
    x_max = 0
    y_min = math.inf
    y_max = 0
    pairs = []
    for i in range(len(input_data)):
        value = input_data[i]
        sensor_x, rest, beacon_y = value.strip("Sensor at x=").split(", y=")
        sensor_y, beacon_x = rest.split(": closest beacon is at x=")
        sensor_x = int(sensor_x)
        sensor_y = int(sensor_y)
        beacon_x = int(beacon_x)
        beacon_y = int(beacon_y)
        pairs.append([sensor_x, sensor_y, beacon_x, beacon_y])
        if sensor_x > x_max or beacon_x > x_max:
            x_max = max(sensor_x, beacon_x)
        if sensor_x < x_min or beacon_x < x_min:
            x_min = min(sensor_x, beacon_x)
        if sensor_y > y_max or beacon_y > y_max:
            y_max = max(sensor_y, beacon_y)
        if sensor_y < y_min or beacon_y < y_min:
            y_min = min(sensor_y, beacon_y)

    # .x ->
    # y
    # |
    # V
    # x_min -= 100
    # x_max += 100
    # y_min -= 100
    # y_max += 100

    check_y = 10
    check_y = 2000000

    print(f"{x_min=}, {x_max=}, {y_min=}, {y_max=}")
    height = y_max + abs(y_min) + 1
    width = x_max + abs(x_min) + 1
    # cave = np.zeros((height, width), dtype=int)
    non_beacons_at_check_row = set()
    beacons_at_check_row = set()
    for i in tqdm(range(len(pairs))):
        pair = pairs[i]
        sensor_x, sensor_y, beacon_x, beacon_y = pair
        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        dist_to_check_row = abs(sensor_y - check_y)
        horizontal_signal_length = manhattan_distance - dist_to_check_row

        if horizontal_signal_length <= 0:
            # print(f"No need to check pair {i}: {pair}")
            continue

        print()
        print(f"{sensor_x=}, {sensor_y=}, {beacon_x=}, {beacon_y=}")
        print(f"{manhattan_distance=}")

        left_range = range(sensor_x - horizontal_signal_length, sensor_x)
        right_and_center_range = range(
            sensor_x, sensor_x + horizontal_signal_length + 1
        )
        print(f"{left_range=}")
        print(f"{right_and_center_range=}")

        # To the left
        non_beacons_at_check_row = non_beacons_at_check_row.union(set(left_range))
        # To the right, incl. center
        non_beacons_at_check_row = non_beacons_at_check_row.union(
            set(right_and_center_range)
        )

        if beacon_y == check_y:
            beacons_at_check_row.add(beacon_x)

    print(non_beacons_at_check_row)
    print(beacons_at_check_row)
    return len(non_beacons_at_check_row.difference(beacons_at_check_row))


####B######################


def second_task(input_data):
    x_min = math.inf
    x_max = 0
    y_min = math.inf
    y_max = 0
    pairs = []
    for i in range(len(input_data)):
        value = input_data[i]
        sensor_x, rest, beacon_y = value.strip("Sensor at x=").split(", y=")
        sensor_y, beacon_x = rest.split(": closest beacon is at x=")
        sensor_x = int(sensor_x)
        sensor_y = int(sensor_y)
        beacon_x = int(beacon_x)
        beacon_y = int(beacon_y)
        pairs.append([sensor_x, sensor_y, beacon_x, beacon_y])
        if sensor_x > x_max or beacon_x > x_max:
            x_max = max(sensor_x, beacon_x)
        if sensor_x < x_min or beacon_x < x_min:
            x_min = min(sensor_x, beacon_x)
        if sensor_y > y_max or beacon_y > y_max:
            y_max = max(sensor_y, beacon_y)
        if sensor_y < y_min or beacon_y < y_min:
            y_min = min(sensor_y, beacon_y)

    # .x ->
    # y
    # |
    # V

    search_min = 0
    search_max = 20
    search_max = 4000000

    # check_y = 10
    # check_y = 2000000

    # 80000000 too low

    # #######
    # search_xs = set(range(search_max + 1))
    # for search_y in tqdm(range(search_max)):
    #     # print(search_y)
    #     non_beacons_at_check_row = set()
    #     for pair in pairs:
    #         sensor_x, sensor_y, beacon_x, beacon_y = pair
    #         manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
    #         dist_to_check_row = abs(sensor_y - search_y)
    #         horizontal_signal_length = manhattan_distance - dist_to_check_row
    #         if horizontal_signal_length <= 0:
    #             # print(f"No need to check pair {i}: {pair}")
    #             continue
    #         left_range = range(
    #             max(0, sensor_x - horizontal_signal_length),
    #             min(sensor_x, search_max),
    #         )
    #         right_and_center_range = range(
    #             max(0, sensor_x),
    #             min(sensor_x + horizontal_signal_length, search_max) + 1,
    #         )

    #         # To the left
    #         non_beacons_at_check_row = non_beacons_at_check_row.union(set(left_range))
    #         # To the right, incl. center
    #         non_beacons_at_check_row = non_beacons_at_check_row.union(
    #             set(right_and_center_range)
    #         )
    #     # print(non_beacons_at_check_row)
    #     # print(len(non_beacons_at_check_row))
    #     # print(len(search_xs))
    #     if len(non_beacons_at_check_row) != len(search_xs):
    #         missing_x = (search_xs - non_beacons_at_check_row).pop()
    #         print(missing_x)
    #         print(search_y)
    #         return missing_x * 4000000 + search_y
    # #######

    check_y = 2000000
    check_y = 11

    search_max = 4000000
    search_max = 20
    search_xs = set(range(search_max + 1))
    print(f"{x_min=}, {x_max=}, {y_min=}, {y_max=}")
    for search_y in range(search_max):
        non_beacons_at_check_row = set()
        for i in range(len(pairs)):
            pair = pairs[i]
            sensor_x, sensor_y, beacon_x, beacon_y = pair
            manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

            dist_to_check_row = abs(sensor_y - search_y)
            horizontal_signal_length = manhattan_distance - dist_to_check_row

            if horizontal_signal_length <= 0:
                # print(f"No need to check pair {i}: {pair}")
                continue

            # print()
            # print(f"{sensor_x=}, {sensor_y=}, {beacon_x=}, {beacon_y=}")
            # print(f"{manhattan_distance=}")

            left_range = range(
                max(0, sensor_x - horizontal_signal_length),
                min(sensor_x, search_max),
            )
            right_and_center_range = range(
                max(0, sensor_x),
                min(sensor_x + horizontal_signal_length, search_max) + 1,
            )
            # print(f"{left_range=}")
            # print(f"{right_and_center_range=}")

            # To the left
            non_beacons_at_check_row = non_beacons_at_check_row.union(set(left_range))
            # To the right, incl. center
            non_beacons_at_check_row = non_beacons_at_check_row.union(
                set(right_and_center_range)
            )

        if len(search_xs - non_beacons_at_check_row) == 1:
            missing_x = (search_xs - non_beacons_at_check_row).pop()
            return missing_x * 4000000 + search_y

    raise RuntimeError
    # non_beacons_at_check_row.remove(12)
    print(non_beacons_at_check_row)
    print(search_xs - non_beacons_at_check_row)
    return len(non_beacons_at_check_row)


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
