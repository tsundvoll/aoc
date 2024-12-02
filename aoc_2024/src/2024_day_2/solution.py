import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def is_report_safe(report):
    prev = report[0]
    following = report[1]

    if following > prev:
        is_increasing = True
        if following - prev < 1 or following - prev > 3:
            return False
    else:
        is_increasing = False
        if prev - following < 1 or prev - following > 3:
            return False

    prev = following
    for i in range(2, len(report)):
        following = report[i]

        if is_increasing and following <= prev:
            return False

        if not is_increasing and following >= prev:
            return False

        if abs(following - prev) < 1 or abs(following - prev) > 3:
            return False

        prev = following

    return True


def first_task(input_data: list[str]):
    count = 0
    for i in range(len(input_data)):
        input_line = input_data[i]
        levels = list(map(int, input_line.split(" ")))

        prev = levels[0]
        following = levels[1]

        if following > prev:
            is_increasing = True
            if following - prev < 1 or following - prev > 3:
                continue
        else:
            is_increasing = False
            if prev - following < 1 or prev - following > 3:
                continue

        is_safe = True
        prev = following
        for i in range(2, len(levels)):
            following = levels[i]

            if is_increasing and following <= prev:
                is_safe = False
                break

            elif not is_increasing and following >= prev:
                is_safe = False
                break

            if abs(following - prev) < 1 or abs(following - prev) > 3:
                is_safe = False
                break
            prev = following

        if is_safe:
            count += 1

    return count


def second_task(input_data: list[str]):
    count = 0
    for i in range(len(input_data)):
        input_line = input_data[i]
        report = list(map(int, input_line.split(" ")))

        is_safe = is_report_safe(report)

        if is_safe:
            count += 1
            continue

        for j in range(len(report)):
            report = list(map(int, input_line.split(" ")))
            report.pop(j)
            is_safe = is_report_safe(report)
            report = list(map(int, input_line.split(" ")))

            if is_safe:
                count += 1
                break

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
