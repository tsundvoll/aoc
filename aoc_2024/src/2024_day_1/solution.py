import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data: list[str]):
    count = 0
    left_list = []
    right_list = []
    for i in range(len(input_data)):
        input_line = input_data[i]
        first, second = input_line.split("   ")
        left_list.append(int(first))
        right_list.append(int(second))

    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        left = left_list[i]
        right = right_list[i]

        count += abs(left - right)

    return count


def second_task(input_data: list[str]):
    count = 0
    left_list = []
    right_list = []

    count_right = {}
    for i in range(len(input_data)):
        input_line = input_data[i]
        first, second = input_line.split("   ")
        left_list.append(int(first))
        right = int(second)

        if right in count_right.keys():
            count_right[right] = count_right[right] + 1
        else:
            count_right[right] = 1

    for i in range(len(left_list)):
        left = left_list[i]

        try:
            n_right = count_right[left]
        except KeyError:
            continue

        count += left * n_right

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
