import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data: list[str]):
    count = 0
    for i in range(len(input_data)):
        value: list[str] = input_data[i]
        first_digit = None
        last_digit = None
        for char in value:
            if char.isdigit():
                first_digit = char
                break

        for char in value[::-1]:
            if char.isdigit():
                last_digit = char
                break
        number = int(first_digit + last_digit)
        count += number
    return count


def second_task(input_data: list[str]):
    count = 0
    words_to_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for i in range(len(input_data)):
        value = input_data[i]

        location_to_number = {}

        for word, number in words_to_numbers.items():
            idx_word = value.find(word)
            if idx_word != -1:
                location_to_number[idx_word] = number
            idx_number = value.find(number)
            if idx_number != -1:
                location_to_number[idx_number] = number

        min_loc = min(location_to_number.keys())
        max_loc = max(location_to_number.keys())

        min_number = location_to_number[min_loc]
        max_number = location_to_number[max_loc]

        number = int(min_number + max_number)
        count += number

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
