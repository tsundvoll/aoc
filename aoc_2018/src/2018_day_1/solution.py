import math
import os
import time
from typing import Generator

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data: list):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        op = value[0]
        val = int(value[1:])
        if op == "+":
            count += val
        else:
            count -= val
    return count


def give_value(iterable) -> Generator[int, None, None]:
    while 1:
        for i in iterable:
            yield i


def second_task(input_data: list):
    count = 0
    frequencies = set([0])

    values = give_value(input_data)
    for value in values:
        op = value[0]
        val = int(value[1:])
        if op == "+":
            count += val
        else:
            count -= val

        if count in frequencies:
            return count
        frequencies.add(count)

    raise RuntimeError("Should not reach this")


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
