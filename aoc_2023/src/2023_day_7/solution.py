import math
import os
import time
from collections import Counter

import numpy as np
import pyperclip
from tqdm import tqdm


class Hand:
    def __init__(self, hand: str, bid: str):
        self.hand = hand
        self.bid = int(bid)
        self.value = self.get_hand_value()

    def __eq__(self, other) -> bool:
        return self.hand == other.hand

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return self.hand + " " + str(self.value)

    def get_hand_value(self):
        # 7 Five of a kind {'A': 5}
        # 6 Four of a kind {'A': 4, "B": 1}
        # 5 Full house: {'A': 3, "B": 2}
        # 4 Tree of a kind {'A': 3, "B": 1, "C": 1}
        # 3 Two pair {'A': 2, 'B':2, 'C': 1}
        # 2 One pair {'A': 2, 'B':1, 'C': 1, 'D': 1}
        # 1 High card {'A': 1, 'B':1, 'C': 1, 'D': 1, 'E': 1}

        char_values = {
            "A": 12,
            "K": 11,
            "Q": 10,
            "J": 9,
            "T": 8,
            "9": 7,
            "8": 6,
            "7": 5,
            "6": 4,
            "5": 3,
            "4": 2,
            "3": 1,
            "2": 0,
        }

        value = 1000000
        count_chars = Counter(self.hand)
        values = count_chars.values()
        if len(values) == 1:
            value *= 7
        elif len(values) == 2:
            if 4 in values:
                value *= 6
            else:
                value *= 5
        elif len(values) == 3:
            if 3 in values:
                value *= 4
            else:
                value *= 3
        elif len(values) == 4:
            value *= 2
        else:
            value *= 1

        for i, char in enumerate(reversed(self.hand)):
            bit_value = 13 ** (i)
            char_val = char_values[char]
            value += bit_value * char_val

        return value


class HandNew:
    def __init__(self, hand: str, bid: str):
        self.hand = hand
        self.bid = int(bid)
        self.value = self.get_hand_value()

    def __eq__(self, other) -> bool:
        return self.hand == other.hand

    def __gt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return self.hand + " " + str(self.value)

    def get_hand_value(self):
        # 7 Five of a kind {'A': 5}
        # 6 Four of a kind {'A': 4, "B": 1}
        # 5 Full house: {'A': 3, "B": 2}
        # 4 Tree of a kind {'A': 3, "B": 1, "C": 1}
        # 3 Two pair {'A': 2, 'B':2, 'C': 1}
        # 2 One pair {'A': 2, 'B':1, 'C': 1, 'D': 1}
        # 1 High card {'A': 1, 'B':1, 'C': 1, 'D': 1, 'E': 1}

        char_values = {
            "A": 12,
            "K": 11,
            "Q": 10,
            "T": 9,
            "9": 8,
            "8": 7,
            "7": 6,
            "6": 5,
            "5": 4,
            "4": 3,
            "3": 2,
            "2": 1,
            "J": 0,
        }

        value = 1000000
        count_chars = Counter(self.hand)

        n_jokers = count_chars["J"]

        max_char = ""
        max_val = 0
        if n_jokers > 0:
            for char in self.hand:
                if char != "J":
                    if count_chars[char] > max_val:
                        max_val = count_chars[char]
                        max_char = char
            new_hand = ""
            for c in self.hand:
                if c != "J":
                    new_hand += c
                else:
                    new_hand += max_char
        else:
            new_hand = self.hand

        if self.hand == "JJJJJ":
            new_hand = "AAAAA"

        count_chars = Counter(new_hand)
        values = count_chars.values()
        if len(values) == 1:
            value *= 7
        elif len(values) == 2:
            if 4 in values:
                value *= 6
            else:
                value *= 5
        elif len(values) == 3:
            if 3 in values:
                value *= 4
            else:
                value *= 3
        elif len(values) == 4:
            value *= 2
        else:
            value *= 1

        for i, char in enumerate(reversed(self.hand)):
            bit_value = 13 ** (i)
            char_val = char_values[char]
            value += bit_value * char_val

        return value


def first_task(input_data: list):
    count = 0
    list_of_hands = []
    for i in range(len(input_data)):
        value = input_data[i]
        hand, bid = value.split()
        list_of_hands.append(Hand(hand, bid))

    list_of_hands.sort()

    for i, hand in enumerate(list_of_hands):
        count += hand.bid * (i + 1)

    return count


def second_task(input_data: list):
    count = 0
    list_of_hands = []
    for i in range(len(input_data)):
        value = input_data[i]
        hand, bid = value.split()
        list_of_hands.append(HandNew(hand, bid))

    list_of_hands.sort()
    # print(list_of_hands)

    for i, hand in enumerate(list_of_hands):
        count += hand.bid * (i + 1)

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
