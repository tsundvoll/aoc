import os
import time

import pyperclip


def first_task(input_data):
    cur_cal = 0
    cal_max = 0
    for i in range(len(input_data)):
        value = input_data[i]
        if value == "":
            if cur_cal > cal_max:
                cal_max = cur_cal
            cur_cal = 0
            continue
        cur_cal += int(value)

    if cur_cal > cal_max:
        cal_max = cur_cal
    return cal_max


def second_task(input_data):
    cur_cal = 0
    cal_maxs = [0, 0, 0]
    for i in range(len(input_data)):
        value = input_data[i]
        if value == "":
            sorted_cal_maxs = sorted(cal_maxs)
            if cur_cal > sorted_cal_maxs[0]:
                sorted_cal_maxs[0] = cur_cal
                cal_maxs = sorted_cal_maxs
            cur_cal = 0
            continue
        cur_cal += int(value)

    sorted_cal_maxs = sorted(cal_maxs)
    if cur_cal > sorted_cal_maxs[0]:
        sorted_cal_maxs[0] = cur_cal
        cal_maxs = sorted_cal_maxs
    return sum(cal_maxs)


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
