import math
import os
import time
from enum import Enum

import numpy as np
import pyperclip
from tqdm import tqdm


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Player:
    def __init__(self, entry):
        self.shape = (
            Shape.ROCK
            if entry in ["A", "X", "rock"]
            else Shape.PAPER
            if entry in ["B", "Y", "paper"]
            else Shape.SCISSORS
            if entry in ["C", "Z", "scissors"]
            else None
        )

    def __gt__(self, other):
        return (
            (self.shape == Shape.ROCK and other == Shape.SCISSORS)
            or (self.shape == Shape.PAPER and other == Shape.ROCK)
            or (self.shape == Shape.SCISSORS and other == Shape.PAPER)
        )

    def __eq__(self, other):
        return (
            (self.shape == Shape.ROCK and other == Shape.ROCK)
            or (self.shape == Shape.PAPER and other == Shape.PAPER)
            or (self.shape == Shape.SCISSORS and other == Shape.SCISSORS)
        )

    def __lt__(self, other):
        return (
            (self.shape == Shape.ROCK and other == Shape.PAPER)
            or (self.shape == Shape.PAPER and other == Shape.SCISSORS)
            or (self.shape == Shape.SCISSORS and other == Shape.ROCK)
        )

    def __lshift__(self, other):
        assert other == 1
        return (
            Player("rock")
            if self.shape == Shape.PAPER
            else Player("paper")
            if self.shape == Shape.SCISSORS
            else Player("scissors")
            if self.shape == Shape.ROCK
            else None
        )

    def __rshift__(self, other):
        assert other == 1
        return (
            Player("rock")
            if self.shape == Shape.SCISSORS
            else Player("paper")
            if self.shape == Shape.ROCK
            else Player("scissors")
            if self.shape == Shape.PAPER
            else None
        )

    def __repr__(self):
        return (
            "rock"
            if self.shape == Shape.ROCK
            else "paper"
            if self.shape == Shape.PAPER
            else "scissors"
            if self.shape == Shape.SCISSORS
            else None
        )

    @property
    def value(self):
        return self.shape.value


def outcome(opponent, me):
    if me < opponent:
        return 0
    if me == opponent:
        return 3
    if me > opponent:
        return 6


def first_task(input_data):
    score = 0
    for match in input_data:
        a, b = match.split(" ")
        opponent = Player(a)
        me = Player(b)
        score += me.value + outcome(opponent, me)
    return score


def second_task(input_data):
    score = 0
    for match in input_data:
        a, b = match.split(" ")
        opponent = Player(a)
        if b == "X":  # I need to lose
            me = opponent << 1
        if b == "Y":  # I need to draw
            me = opponent
        if b == "Z":  # I need to win
            me = opponent >> 1
        score += me.value + outcome(opponent, me)
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
