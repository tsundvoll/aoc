import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        pass
    return count


def check_coordinates(input_data, check_x, check_y):
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

    for i in tqdm(range(len(pairs))):
        pair = pairs[i]
        sensor_x, sensor_y, beacon_x, beacon_y = pair
        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        dist_to_check_row = abs(sensor_y - check_y)
        horizontal_signal_length = manhattan_distance - dist_to_check_row

        if horizontal_signal_length > 0:
            left_range = range(sensor_x - horizontal_signal_length, sensor_x)
            right_and_center_range = range(
                sensor_x, sensor_x + horizontal_signal_length + 1
            )

            if check_x in left_range or check_x in right_and_center_range:
                return False

    return True


def second_task(input_data):
    top_lefts = []
    top_rights = []
    bottom_lefts = []
    bottom_rights = []
    for i in range(len(input_data)):
        value = input_data[i]
        value = value.strip("Sensor at x=")
        sensor_x, rest, beacon_y = value.split(", y=")
        sensor_y, beacon_x = rest.split(": closest beacon is at x=")
        sensor_x = int(sensor_x)
        sensor_y = int(sensor_y)
        beacon_x = int(beacon_x)
        beacon_y = int(beacon_y)
        # print(sensor_x, sensor_y, beacon_x, beacon_y)

        m = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        left_point = (sensor_x - m, sensor_y)
        right_point = (sensor_x + m, sensor_y)
        top_point = (sensor_x, sensor_y - m)
        bottom_point = (sensor_x, sensor_y + m)

        """
        Find where all the top left lines crosses the y axis

        (x1, y1)
        y = ax + y_offset
        y_offset = y - ax

        # --> x
        |
        V        T
                . .
        y      .   .
              .     .
               .   .
                . .
                 B

        Top left: a = -1
        Top right a = 1
        Bottom left a = 1
        Bottom rigth a = -1

        Top left must be one bigger than another bottom right
        Top right must be one bigger than another bottom left
        """

        top_x = top_point[0]
        top_y = top_point[1]

        top_left_a = -1
        top_right_a = 1

        bottom_x = bottom_point[0]
        bottom_y = bottom_point[1]

        bottom_left_a = 1
        bottom_right_a = -1

        top_left_crosses_y = top_y - top_left_a * top_x
        top_right_crosses_y = top_y - top_right_a * top_x

        bottom_left_crosses_y = bottom_y - bottom_left_a * bottom_x
        bottom_right_crosses_y = bottom_y - bottom_right_a * bottom_x

        top_lefts.append(top_left_crosses_y)
        top_rights.append(top_right_crosses_y)
        bottom_lefts.append(bottom_left_crosses_y)
        bottom_rights.append(bottom_right_crosses_y)

    print(top_lefts)
    print(top_rights)
    print(bottom_lefts)
    print(bottom_rights)

    # Top left must be one bigger than another bottom right
    # This is the line with a = -1
    a_minus_one_line = []
    for top_left in top_lefts:
        for bottom_right in bottom_rights:
            if top_left == bottom_right + 2:
                a_minus_one_line.append(bottom_right + 1)

    # Top right must be one bigger than another bottom left
    # This is the line with a = 1
    a_one_line = []
    for top_right in top_rights:
        for bottom_left in bottom_lefts:
            if top_right == bottom_left + 2:
                a_one_line.append(bottom_left + 1)

    print()
    print(a_minus_one_line)
    print(a_one_line)

    """

    y1 = -x1 + y_offset_a_minus_one_line
    y2 = x2 + y_offset_a_one_line

    x2 + y_offset_a_one_line = -x1 + y_offset_a_minus_one_line

    2x = y_offset_a_minus_one_line - y_offset_a_one_line
    x = (y_offset_a_minus_one_line - y_offset_a_one_line) / 2
    """

    for offset_y_a_minus_one_line in set(a_minus_one_line):
        for offset_y_a_one_line in set(a_one_line):
            x = (offset_y_a_minus_one_line - offset_y_a_one_line) // 2
            y = x + offset_y_a_one_line
            print(x, y)
            if check_coordinates(input_data, x, y):
                return x * 4000000 + y
    return None


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    # if first_answer is not None:
    #    pyperclip.copy(str(first_answer))
    #    pyperclip.paste()

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    # if second_answer is not None:
    #    pyperclip.copy(str(second_answer))
    #    pyperclip.paste()

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
