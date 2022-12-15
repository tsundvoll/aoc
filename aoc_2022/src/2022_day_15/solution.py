import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data):
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

    check_y = 2000000

    print(f"{x_min=}, {x_max=}, {y_min=}, {y_max=}")
    height = y_max + abs(y_min) + 1
    width = x_max + abs(x_min) + 1
    cave = np.zeros((height, width), dtype=int)
    for pair in pairs:
        sensor_x, sensor_y, beacon_x, beacon_y = pair
        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        # print(f"{sensor_x=}, {sensor_y=}, {beacon_x=}, {beacon_y=}")
        # print(f"{manhattan_distance=}")

        for x in range(
            sensor_x - manhattan_distance, sensor_x + manhattan_distance + 1
        ):
            for y in range(
                sensor_y - manhattan_distance, sensor_y + manhattan_distance + 1
            ):
                try:
                    if abs(sensor_x - x) + abs(sensor_y - y) <= manhattan_distance:
                        y_pos = max(0, y + abs(y_min))
                        x_pos = max(0, x + abs(x_min))
                        if cave[y_pos][x_pos] == 0:
                            cave[y_pos][x_pos] = 1
                except:
                    ##print(f"Avoiding {row_pos=} {col_pos=}")
                    pass
        try:
            # cave[sensor_y + abs(y_min)][sensor_x + abs(x_min)] = 2
            cave[beacon_y + abs(y_min)][beacon_x + abs(x_min)] = 3
        except:
            pass
        # print(cave)
    print(cave)
    print(cave[10 + abs(y_min)])
    print(len(cave[10 + abs(y_min)]))
    print(len(cave))
    count = np.count_nonzero(cave[10 + abs(y_min)] == 1)
    return count


####B######################


def second_task(input_data):

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
