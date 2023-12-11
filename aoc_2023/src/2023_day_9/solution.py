import os
import time
from collections import Counter

import pyperclip


def first_task(input_data: list):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        first_sequence = list(map(int, value.split()))

        sequences = [first_sequence]

        while True:
            next_sequence = []
            for i in range(len(first_sequence) - 1):
                next_sequence.append(first_sequence[i + 1] - first_sequence[i])
            sequences.append(next_sequence)

            counter = Counter(next_sequence)
            first_sequence = next_sequence

            if len(counter.keys()) == 1:
                break

        val = 0
        for sequence in sequences:
            val += sequence[-1]

        count += val
    return count


def second_task(input_data: list):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        first_sequence = list(map(int, value.split()))

        sequences = [first_sequence]

        while True:
            next_sequence = []
            for i in range(len(first_sequence) - 1):
                next_sequence.append(first_sequence[i + 1] - first_sequence[i])
            sequences.append(next_sequence)

            counter = Counter(next_sequence)
            first_sequence = next_sequence

            if len(counter.keys()) == 1:
                break

        val = 0
        for sequence in reversed(sequences):
            val = sequence[0] - val

        count += val
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
