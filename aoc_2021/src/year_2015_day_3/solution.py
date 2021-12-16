import os
import time

import pyperclip
from utility import parse


def first_task(input):
    l = [0, 0]
    locations = set()
    locations.add(tuple(l))

    for c in input:
        if c == '^':
            l = l[0]+1, l[1]
        if c == 'v':
            l = l[0]-1, l[1]
        if c == '>':
            l = l[0], l[1]+1
        if c == '<':
            l = l[0], l[1]-1

        locations.add(tuple(l))

    return len(locations)


def second_task(input):
    s = [0, 0]
    r = [0, 0]
    locations = set()
    locations.add(tuple(s))
    locations.add(tuple(r))

    for i, c in enumerate(input):
        if i % 2 == 0:
            if c == '^':
                s = [s[0]+1, s[1]]
            if c == 'v':
                s = [s[0]-1, s[1]]
            if c == '>':
                s = [s[0], s[1]+1]
            if c == '<':
                s = [s[0], s[1]-1]

            locations.add(tuple(s))
        else:
            if c == '^':
                r = [r[0]+1, r[1]]
            if c == 'v':
                r = [r[0]-1, r[1]]
            if c == '>':
                r = [r[0], r[1]+1]
            if c == '<':
                r = [r[0], r[1]-1]
            locations.add(tuple(r))
    return len(locations)


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)[0]
    print(input_data)

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(first_answer)
        pyperclip.paste()

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(second_answer)
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
