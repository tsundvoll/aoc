import os
import time
from collections import defaultdict

import pyperclip


def first_task(input_data: list):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        _, numbers = value.split(": ")
        winning_numbers, my_numbers = numbers.split(" | ")

        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))

        print(winning_numbers)
        print(my_numbers)

        val = 0
        for my_num in my_numbers:
            if my_num in winning_numbers:
                if val == 0:
                    val = 1
                else:
                    val *= 2
        count += val

    return count


def second_task(input_data: list):
    count = 0
    max_cards = len(input_data)

    copies = {}
    copies = defaultdict(lambda: 1, copies)
    for i in range(len(input_data)):
        value = input_data[i]
        card, numbers = value.split(": ")
        _, card_id = card.split()
        card_id = int(card_id)
        winning_numbers, my_numbers = numbers.split(" | ")

        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))

        print(winning_numbers)
        print(my_numbers)

        matches = 0
        for my_num in my_numbers:
            if my_num in winning_numbers:
                matches += 1

        number_of_current_card = copies[card_id]

        for copy_i in range(card_id + 1, card_id + matches + 1):
            print(f"Copy cards: {copy_i}")
            copies[copy_i] += number_of_current_card

        print(copies)
        print()

    for value in copies.values():
        count += value

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
