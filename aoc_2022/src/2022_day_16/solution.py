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


def second_task(input_data):
    count = 0
    points_to_check = []
    for i in range(len(input_data)):
        value = input_data[i]
        value = value.strip("Sensor at x=")
        sensor_x, rest, beacon_y = value.split(", y=")
        sensor_y, beacon_x = rest.split(": closest beacon is at x=")
        sensor_x = int(sensor_x)
        sensor_y = int(sensor_y)
        beacon_x = int(beacon_x)
        beacon_y = int(beacon_y)
        print(sensor_x, sensor_y, beacon_x, beacon_y)

        m = abs(beacon_x-sensor_x) + abs(beacon_y-sensor_y)

        left_point = (sensor_x - m, sensor_y)
        right_point = (sensor_x + m, sensor_y)
        top_point = (sensor_x, sensor_y - m)
        bottom_point = (sensor_x, sensor_y + m)

        def add_line(start_x, start_y, end_x, end_y, incr_x, incr_y):
            x = start_x
            y = start_y
            while True:
                points_to_check.append((x, y))
                x += incr_x
                y += incr_y
                if x*incr_x > end_x*incr_x or y*incr_y > end_y*incr_y:
                    break

        # Top left line
        start_x = sensor_x - 1
        start_y = sensor_y - m - 1
        end_x = sensor_x - m - 1
        end_y = sensor_y - 1
        incr_x = -1
        incr_y = 1
        add_line(start_x, start_y, end_x, end_y, incr_x, incr_y)

        # Top right line
        start_x = sensor_x + 1
        start_y = sensor_y - m - 1
        end_x = sensor_x + m + 1
        end_y = sensor_y - 1
        incr_x = 1
        incr_y = 1
        add_line(start_x, start_y, end_x, end_y, incr_x, incr_y)

        # Bottom right line
        start_x = sensor_x + m + 1
        start_y = sensor_y + 1
        end_x = sensor_x + 1
        end_y = sensor_y + m + 1
        incr_x = -1
        incr_y = 1
        add_line(start_x, start_y, end_x, end_y, incr_x, incr_y)

        # Bottom right line
        start_x = sensor_x - 1
        start_y = sensor_y + m + 1
        end_x = sensor_x - m - 1
        end_y = sensor_y + 1
        incr_x = -1
        incr_y = -1
        add_line(start_x, start_y, end_x, end_y, incr_x, incr_y)

    print(len(points_to_check))
    return None


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    #if first_answer is not None:
    #    pyperclip.copy(str(first_answer))
    #    pyperclip.paste()

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    #if second_answer is not None:
    #    pyperclip.copy(str(second_answer))
    #    pyperclip.paste()

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
