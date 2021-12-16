import functools
import math
import os
import time

import cv2
import numpy as np
import pyperclip
from _pytest.fixtures import FixtureLookupError
from utility import parse


def first_task(input):
    count = 0
    numbers = list(map(int, input.split(',')))
    high = max(numbers)
    low = min(numbers)
    fuel_min = math.inf
    low_pos = 0
    for pos in range(low, high + 1):
        fuel = 0
        for n in numbers:
            fuel += abs(n - pos)
        if fuel < fuel_min:
            fuel_min = fuel
            low_pos = pos

    return fuel_min


def second_task(input):
    numbers = list(map(int, input.split(',')))
    high = max(numbers)
    low = min(numbers)
    fuel_min = math.inf
    low_pos = 0
    for pos in range(low, high + 1):
        fuel = 0
        for n in numbers:
            to_add = abs(n - pos)
            for i in range(1, to_add+1):
                f = i
                fuel += f
        if fuel < fuel_min:
            fuel_min = fuel
            low_pos = pos

    return fuel_min


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)[0]

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()
