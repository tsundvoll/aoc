import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def get_pairs(list_of_values):
    pairs = []
    for i in range(0, len(list_of_values) - 1):
        first = list_of_values[i]
        for j in range(i + 1, len(list_of_values)):
            second = list_of_values[j]
            pairs.append((first, second))
    return pairs


def first_task(input_data: list[str]):
    count = 0
    rules = []
    updates = []
    is_processing_first_section = True
    for i in range(len(input_data)):
        input_line = input_data[i]

        if input_line == "":
            is_processing_first_section = False
            continue

        if is_processing_first_section:
            rule = tuple(map(int, input_line.split("|")))
            rules.append(rule)
        else:
            update = list(map(int, input_line.split(",")))
            updates.append(update)

    for update in updates:
        pairs = get_pairs(update)

        is_correct = True
        for pair in pairs:
            if pair not in rules:
                is_correct = False

        if is_correct:
            count += update[int(len(update) / 2)]

    return count


class PageNumber:
    def __init__(self, value: int, rules: tuple[int, int]):
        self.value = value
        self.rules = rules

    def __lt__(self, other):
        if (self.value, other.value) in self.rules:
            return True
        else:
            return False

    def __repr__(self):
        return str(self.value)


def second_task(input_data: list[str]):
    count = 0
    rules = []
    updates = []
    is_processing_first_section = True
    for i in range(len(input_data)):
        input_line = input_data[i]

        if input_line == "":
            is_processing_first_section = False
            continue

        if is_processing_first_section:
            rule = tuple(map(int, input_line.split("|")))
            rules.append(rule)
        else:
            update = list(map(int, input_line.split(",")))
            updates.append(update)

    for update in updates:
        pairs = get_pairs(update)

        is_correct = True
        for pair in pairs:
            if pair not in rules:
                is_correct = False

        if not is_correct:
            page_numbers: list[PageNumber] = [PageNumber(val, rules) for val in update]
            page_numbers.sort()

            mid_val = page_numbers[int(len(page_numbers) / 2)].value
            count += mid_val

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
