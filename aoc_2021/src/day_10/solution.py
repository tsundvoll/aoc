import math
import os
import time

import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    count = 0
    for word in input:
        stack = []
        open_c = {'(': 0, '[': 0, '{': 0, '<': 0}
        for i in range(len(word)):
            c = word[i]

            if c in open_c.keys():
                closing_match = {'(': ')', '[': ']', '{': '}', '<': '>'}[c]
                stack.append(closing_match)
            else:
                next_closing_c = stack.pop()

                if c != next_closing_c:
                    # print(f'At {i}, found {c}, expected {next_closing_c}')
                    count += {
                        ')': 3, ']': 57, '}': 1197, '>': 25137
                    }[c]
    return count


def second_task(input):
    VALUES = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for word in input:
        stack = []
        open_chars = ['(', '[', '{', '<']
        corrupt = False
        for c in word:
            if c in open_chars:
                closing_match = {'(': ')', '[': ']', '{': '}', '<': '>'}[c]
                stack.append(closing_match)
            else:
                next_closing_c = stack.pop()
                if c != next_closing_c:
                    # If so, this is a corrupt line
                    corrupt = True

        if not corrupt:
            r = stack[::-1]
            if len(stack) > 0:
                # If so, this is an invalid line
                s = 0
                for c in r:
                    s = s * 5 + VALUES[c]
                scores.append(s)

    scores.sort()
    return int(scores[len(scores)//2])



def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()
