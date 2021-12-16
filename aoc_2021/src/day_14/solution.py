import functools
import math
import os
import time

import numpy as np
import pyperclip
from tqdm.auto import trange
from utility import parse


def first_task(input):
    count = 0
    polymer = input[0]
    rules = {}
    for i, word in enumerate(input[2:]):
        pair, insert = word.split(' -> ')
        rules[pair] = insert
    
    for _ in trange(10, desc='1st loop'):
        n_inserted = 0
        insert_at = ()
        for i in trange(len(polymer)-1, desc='2nd loop'):
            pair = polymer[i:i+2]
            if pair in rules:
                insert = rules[pair]
                insert_at += ((1 + i + n_inserted, insert),)
                n_inserted += 1

        for i in trange(int(len(insert_at)), desc='3rd loop'):
            idx, char = insert_at[i]
            polymer = polymer[:idx] + char + polymer[idx:]
    
    chars = set()
    for c in polymer:
        chars.add(c)

    most_common = 0
    least_common = len(polymer)
    for c in chars:
        count = polymer.count(c)
        if count > most_common:
            most_common = count
        if count < least_common:
            least_common = count
    return most_common - least_common


rules = {}
chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

@functools.cache
def unpack(pair, turn):
    if turn == 1:
        count = {c: 0 for c in chars}
        a, _ = rules[pair]
        first, second = a
        count[first] += 1
        count[second] += 1
        return count

    a, b = rules[pair]
    count_a = unpack(a, turn=turn-1)
    count_b = unpack(b, turn=turn-1)

    count = {c: 0 for c in chars}
    for char, value in count_a.items():
        count[char] += value
    for char, value in count_b.items():
        count[char] += value
    return count

"""

HHKONSO

HH -> HN , NH
      
      HN > HO OH


"""


def second_task(input):
    polymer = input[0]
    global rules
    for i, word in enumerate(input[2:]):
        pair, insert = word.split(' -> ')
        rules[pair] = (pair[0] + insert, insert + pair[1])
    
    count = {c: 0 for c in chars}
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        count_x = unpack(pair, turn=40)
        for char, value in count_x.items():
            count[char] += value

    last_char = polymer[-1]
    count[last_char] += 1

    most_common = 0
    least_common = math.inf
    for value in count.values():
        if value == 0:
            continue
        if value > most_common:
            most_common = value
        if value < least_common:
            least_common = value
    return most_common - least_common


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
