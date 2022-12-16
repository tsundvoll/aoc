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
    for i in range(len(input_data)):
        value = input_data[i]
        value = value.strip("Sensor at x=")
        sensor_x, rest, beacon_y = value.split(", y=")
        sensor_y, beacon_x = rest.split(": closest beacon is at x=")
        print(sensor_x, sensor_y, beacon_x, beacon_y)

        m = abs(beacon_x-sensor_x) + abs(beacon_y-sensor_y)

        left_point = (sensor_x - m, sensor_y)
        right_point = (sensor_x + m, sensor_y)
        top_point = (sensor_x, sensor_y - m)
        bottom_point = (sensor_x, sensor_y + m)

        slope_top_left = top_point[0]
        
        pass
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
