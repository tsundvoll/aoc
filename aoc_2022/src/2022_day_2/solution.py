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
        a, b = value.split(" ")

        score = 0
        if b == "X":
            score += 1
        if b == "Y":
            score += 2
        if b == "Z":
            score += 3

        if (
            (a == "A" and b == "X")
            or (a == "B" and b == "Y")
            or (a == "C" and b == "Z")
        ):
            score += 3

        if (
            (a == "A" and b == "Y")
            or (a == "B" and b == "Z")
            or (a == "C" and b == "X")
        ):
            score += 6

        if (
            (a == "A" and b == "Z")
            or (a == "B" and b == "X")
            or (a == "C" and b == "Y")
        ):
            score += 0

        count += score

    return count


def second_task(input_data):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        a, b = value.split(" ")

        score = 0
        if b == "X":
            score += 0
            if a == "A":
                # I must play scissors
                score += 3
            if a == "B":
                # I must play rock
                score += 1
            if a == "C":
                # I must play paper
                score += 2
        if b == "Y":
            score += 3
            if a == "A":
                # I must play rock
                score += 1
            if a == "B":
                # I must play paper
                score += 2
            if a == "C":
                # I must play scissors
                score += 3
        if b == "Z":
            score += 6
            if a == "A":
                # I must play paper
                score += 2
            if a == "B":
                # I must play scissors
                score += 3
            if a == "C":
                # I must play rock
                score += 1

        count += score
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
