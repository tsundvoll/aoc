import math
import os
import time

import pyperclip


def first_task(input_data: list):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        number = ""
        for char in value:
            print(char)
            try:
                val = int(char)
                number += char
            except:
                pass
        print(number)
        line_number = number[0] + number[-1]
        count += int(line_number)
        number = ""

    return count


def second_task(input_data: list):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        ids = [
            value.find("one"),
            value.find("two"),
            value.find("three"),
            value.find("four"),
            value.find("five"),
            value.find("six"),
            value.find("seven"),
            value.find("eight"),
            value.find("nine"),
        ]
        ids_numbers = [
            value.find("1"),
            value.find("2"),
            value.find("3"),
            value.find("4"),
            value.find("5"),
            value.find("6"),
            value.find("7"),
            value.find("8"),
            value.find("9"),
        ]
        min_val = (
            min([x for x in ids if x >= 0]) if [x for x in ids if x >= 0] else math.inf
        )
        min_num = (
            min([x for x in ids_numbers if x >= 0])
            if [x for x in ids_numbers if x >= 0]
            else math.inf
        )
        if min_val < min_num:
            first_number = ids.index(min_val) + 1
        else:
            first_number = ids_numbers.index(min_num) + 1

        ids = [
            value.rfind("one"),
            value.rfind("two"),
            value.rfind("three"),
            value.rfind("four"),
            value.rfind("five"),
            value.rfind("six"),
            value.rfind("seven"),
            value.rfind("eight"),
            value.rfind("nine"),
        ]
        ids_numbers = [
            value.rfind("1"),
            value.rfind("2"),
            value.rfind("3"),
            value.rfind("4"),
            value.rfind("5"),
            value.rfind("6"),
            value.rfind("7"),
            value.rfind("8"),
            value.rfind("9"),
        ]

        max_val = (
            max([x for x in ids if x >= 0]) if [x for x in ids if x >= 0] else -math.inf
        )
        max_num = (
            max([x for x in ids_numbers if x >= 0])
            if [x for x in ids_numbers if x >= 0]
            else -math.inf
        )
        if max_val > max_num:
            last_number = ids.index(max_val) + 1
        else:
            last_number = ids_numbers.index(max_num) + 1

        line_number = int(str(first_number) + str(last_number))
        print(line_number)

        count += line_number
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
