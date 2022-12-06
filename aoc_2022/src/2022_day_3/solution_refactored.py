import os
import time

import pyperclip

lower_case = [chr(c) for c in range(ord("a"), ord("z") + 1)]
lower_case_values = [v for v in range(1, 27)]

upper_case = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
upper_case_values = [v for v in range(27, 53)]

D = {key: value for (key, value) in zip(lower_case, lower_case_values)}
D.update({key: value for (key, value) in zip(upper_case, upper_case_values)})


def first_task(input_data):
    score = 0
    for i in range(len(input_data)):
        value = input_data[i]
        n_half = len(value) // 2
        first = value[0:n_half]
        second = value[n_half:]
        duplicate = set(first).intersection(set(second)).pop()
        score += int(D[duplicate])
    return score


def second_task(input_data):
    score = 0
    sets = []
    for i in range(len(input_data)):
        value = input_data[i]
        sets.append(set(value))
        if i % 3 == 2:
            duplicate = sets[0].intersection(sets[1]).intersection(sets[2]).pop()
            score += int(D[duplicate])
            sets = []
    return score


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
