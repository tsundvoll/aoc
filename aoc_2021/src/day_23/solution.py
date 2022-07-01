import math
import os
import time
from attr import s

import numpy as np
import pyperclip
from tqdm import tqdm
from utility import parse

def first_task(input):
    
    start = []
    for line in input:
        start.append(line.split(' '))

    print(start[0])
    print(start[1])


def second_task(input):

    start = []
    for line in input:
        start.append(line.split(' '))

    print(start[0])
    print(start[1])
    print(start[2])
    print(start[3])
    return None


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

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()
