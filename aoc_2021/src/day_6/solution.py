import functools
import math
import os
import time

import numpy as np
import pyperclip
from utility import parse

"""
18    3
17    2
16    1
15    0
14    6-8
13    5 7
12    4 6
11    3 5
10    2 4
09    1 3
08    0 2 
07    6-1----- 8
06    5 0      7
05    4 6-8    6
04    3 5 7    5
03    2 4 6    4
02    1 3 5    3
01    0 2 4    2    
00    6-1-3--- 1-- 8

"""

@functools.cache
def spawn_fish(timer, days_left):
    fish = 1
    days_left_at_next_spawn = days_left - timer - 1

    if days_left_at_next_spawn >= 0:
        fish += spawn_fish(timer=8, days_left=days_left_at_next_spawn)
    else:
        return 1

    days_left_at_next_spawn -= 7
    while days_left_at_next_spawn >= 0:
        fish += spawn_fish(timer=8, days_left=days_left_at_next_spawn)
        days_left_at_next_spawn -= 7

    return fish


def first_task(input):
    fish = np.array(list(map(int, input.split(','))))

    rounds_left = 80

    s = sum([
        spawn_fish(timer=i, days_left=rounds_left) for i in fish
    ])
    return s


def second_task(input):
    fish = np.array(list(map(int, input.split(','))))

    rounds_left = 256

    s = sum([
        spawn_fish(timer=i, days_left=rounds_left) for i in fish
    ])
    return s


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)[0]


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
