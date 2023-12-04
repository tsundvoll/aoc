import os
import time

import pyperclip


def check(input_data, line, col, height, width):
    print(f"Checking ({line}, {col})")

    if line < 0 or col < 0 or line >= height or col >= width:
        return False

    char: str = input_data[line][col]

    if not char == ".":
        if not char.isdigit():
            print("Char:", char, "at (", line, ",", col, ")")
            return not char.isdigit()
    return False


def check_gear(input_data, line, col, height, width):
    print(f"Checking ({line}, {col})")

    if line < 0 or col < 0 or line >= height or col >= width:
        return False, (-1, -1)

    char: str = input_data[line][col]

    if not char == ".":
        if char == "*":
            print("Char:", char, "at (", line, ",", col, ")")
            return (not char.isdigit(), (line, col))
    return False, (-1, -1)


def first_task(input_data: list):
    count = 0
    height = len(input_data)
    width = len(input_data[0])
    for i in range(len(input_data)):
        line = input_data[i]
        number = ""
        number_idxs = []
        is_number = False
        for col, char in enumerate(line):
            if char.isdigit():
                number += char
                number_idxs.append(col)
                is_number = True

            if (
                number != ""
                and is_number
                and (not char.isdigit() or col == len(line) - 1)
            ):
                # Do check
                print()
                is_adjacent = False
                for number_idx in number_idxs:
                    print(f"Checking {number} at ({i}, {number_idx})")

                    if (
                        check(input_data, i - 1, number_idx - 1, height, width)
                        or check(input_data, i - 1, number_idx, height, width)
                        or check(input_data, i - 1, number_idx + 1, height, width)
                        or check(input_data, i, number_idx - 1, height, width)
                        or check(input_data, i, number_idx + 1, height, width)
                        or check(input_data, i + 1, number_idx - 1, height, width)
                        or check(input_data, i + 1, number_idx, height, width)
                        or check(input_data, i + 1, number_idx + 1, height, width)
                    ):
                        is_adjacent = True
                    print()

                if is_adjacent:
                    count += int(number)
                    print("Found:", number)

                is_number = False
                number = ""
                number_idxs = []
    return count


def second_task(input_data: list):
    count = 0
    height = len(input_data)
    width = len(input_data[0])
    gears = {}
    for i in range(len(input_data)):
        line = input_data[i]
        number = ""
        number_idxs = []
        is_number = False
        for col, char in enumerate(line):
            if char.isdigit():
                number += char
                number_idxs.append(col)
                is_number = True

            if (
                number != ""
                and is_number
                and (not char.isdigit() or col == len(line) - 1)
            ):
                # Do check
                print()
                is_adjacent = False
                is_gear = False
                for number_idx in number_idxs:
                    print(f"Checking {number} at ({i}, {number_idx})")

                    for line_id, col_id in [
                        (i - 1, number_idx - 1),
                        (i - 1, number_idx),
                        (i - 1, number_idx + 1),
                        (i, number_idx - 1),
                        (i, number_idx + 1),
                        (i + 1, number_idx - 1),
                        (i + 1, number_idx),
                        (i + 1, number_idx + 1),
                    ]:
                        is_gear, tag = check_gear(
                            input_data, line_id, col_id, height, width
                        )
                        if is_gear:
                            print("Found:", number)
                            int_number = int(number)
                            if tag in gears.keys():
                                gears[tag].append(int_number)
                            else:
                                gears[tag] = [int_number]
                            break
                    if is_gear:
                        break

                is_number = False
                number = ""
                number_idxs = []

    print(gears)

    count = 0
    for key, value in gears.items():
        if len(value) == 2:
            count += value[0] * value[1]

    print(count)
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
