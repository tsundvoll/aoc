import math
import os
import time

import cv2
import numpy as np
import pyperclip
from utility import parse

"""
list(map(int, word.split(',')))
"""

def first_task(input):
    size = 990
    img = np.zeros((size,size))
    max_val = 0
    for i, word in enumerate(input):
        one, two = word.split(' -> ')
        x1, y1 = list(map(int, one.split(',')))
        x2, y2 = list(map(int, two.split(',')))
        
        if x1 == x2 or y1 == y2:
            new_line = cv2.line(np.zeros((size,size)), (x1, y1), (x2, y2), color=1)
            img += new_line

        if x1 > max_val or y1 > max_val or x2 > max_val or y2 > max_val:
            max_val = max(x1, y1, y2, x2)

    return (img >= 2).sum()


def second_task(input):
    size = 990
    img = np.zeros((size,size))
    for i, word in enumerate(input):
        one, two = word.split(' -> ')
        x1, y1 = list(map(int, one.split(',')))
        x2, y2 = list(map(int, two.split(',')))
        
        new_line = cv2.line(np.zeros((size,size)), (x1, y1), (x2, y2), color=1)
        img += new_line

    return (img >= 2).sum()


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
