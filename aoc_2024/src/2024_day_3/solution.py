import math
import os
import re
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data: list[str]):
    count = 0
    for i in range(len(input_data)):
        input_line = input_data[i]

        first = input_line.split("mul(")

        keep = []
        for f in first:
            if len(f) > 1 and f[0].isdigit():
                last = f.split(")")

                # print(last)
                for l in last:
                    comma = l.split(",")
                    if len(comma) == 2:
                        # print(comma)
                        left = comma[0]
                        right = comma[1]
                        if left.isdigit() and right.isdigit():
                            # print(comma)
                            count += int(left) * int(right)

    return count


def second_task(input_data: list[str]):
    count = 0
    is_dont_from_last_line = False
    for i in range(len(input_data)):
        input_line = input_data[i]

        all_valids, *questionable = input_line.split("don't()")
        print(all_valids)
        print(questionable)
        for q in questionable:
            invalid, *valids = q.split("do()")
            all_valids += "".join(valids)
            print(f"{invalid=}")
            print(f"{valids=}")

        print(all_valids)

        first = all_valids.split("mul(")
        for f in first:
            if len(f) > 1 and f[0].isdigit():
                last = f.split(")")
                for l in last:
                    comma = l.split(",")
                    if len(comma) == 2:
                        left = comma[0]
                        right = comma[1]
                        if left.isdigit() and right.isdigit():
                            count += int(left) * int(right)

    return count


# def second_task(input_data: list[str]):
#     count = 0
#     is_dont_from_last_line = False
#     for i in range(len(input_data)):
#         input_line = input_data[i]
#         first = input_line.split("mul(")

#         keep = []
#         for f in first:
#             # print(f)
#             if len(f) > 1 and f[0].isdigit():
#                 last = f.split(")")

#                 for l in last:
#                     comma = l.split(",")
#                     if len(comma) == 2:
#                         # print(comma)
#                         left = comma[0]
#                         right = comma[1]
#                         if left.isdigit() and right.isdigit():
#                             # print(comma)
#                             keep.append(f"mul({left},{right})")
#                             # count += int(left) * int(right)

#         DO_BACKWARDS = ")(od"
#         DONT_BACKWARDS = ")(t'nod"
#         for k in keep:
#             try:
#                 before, _ = input_line.split(k)
#             except ValueError:
#                 print()
#                 print(len(input_line.split(k)))
#                 print(input_line.split(k))
#                 print(k)
#                 raise RuntimeError
#             # print()
#             before_backwards = before[::-1]
#             # print(before_backwards)

#             dont_idx = before_backwards.find(DONT_BACKWARDS)
#             do_idx = before_backwards.find(DO_BACKWARDS)

#             # print(f"{dont_idx=}")
#             # print(f"{do_idx=}")
#             if dont_idx != -1:
#                 if do_idx == -1 or do_idx > dont_idx:
#                     continue

#             # if do_idx != -1 and is_dont_from_last_line:
#             #     continue

#             first, last = list(map(int, k.split("mul(")[1].split(")")[0].split(",")))
#             # print(first, last)
#             count += first * last

#         last_dont_idx = input_line[::-1].find(DONT_BACKWARDS)
#         last_do_idx = input_line[::-1].find(DO_BACKWARDS)

#         if last_dont_idx < last_do_idx:
#             is_dont_from_last_line = True
#             print("ending with a dont", count)
#         else:
#             print("ending with a do", count)
#             is_dont_from_last_line = False

#     return count


# Wrong
# 110561937
# 92803930
# 66251992


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
