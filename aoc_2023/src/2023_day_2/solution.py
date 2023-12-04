import os
import time

import pyperclip


def first_task(input_data: list):
    count = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    for i in range(len(input_data)):
        value = input_data[i]
        game, list_of_subsets = value.split(": ")
        game_id = game.split(" ")[1]
        subsets = list_of_subsets.split("; ")
        is_valid = True
        for draws in subsets:
            draw = draws.split(", ")
            for d in draw:
                nbr, color = d.split(" ")
                nbr = int(nbr)
                if color == "red" and nbr > max_red:
                    is_valid = False
                if color == "green" and nbr > max_green:
                    is_valid = False
                if color == "blue" and nbr > max_blue:
                    is_valid = False
        if is_valid:
            count += int(game_id)
    return count


def second_task(input_data: list):
    count = 0

    for i in range(len(input_data)):
        max_red = 0
        max_green = 0
        max_blue = 0
        value = input_data[i]
        _, list_of_subsets = value.split(": ")
        subsets = list_of_subsets.split("; ")
        for draws in subsets:
            draw = draws.split(", ")
            for d in draw:
                nbr, color = d.split(" ")
                nbr = int(nbr)
                if color == "red" and nbr > max_red:
                    max_red = nbr
                if color == "green" and nbr > max_green:
                    max_green = nbr
                if color == "blue" and nbr > max_blue:
                    max_blue = nbr
        count += max_red * max_green * max_blue
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
