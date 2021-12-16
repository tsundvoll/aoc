import os
import time

import pyperclip
from utility import parse


def first_task(input):
    paper = 0
    for present in input:
        l, w, h = map(int, present.split('x'))
        a = 2*l*w
        b = 2*w*h
        c = 2*h*l
        paper += a + b + c + min(a, b, c)/2.0

    return int(paper)


def second_task(input):
    ribbon = 0
    for present in input:
        l, w, h = map(int, present.split('x'))
        a, b = sorted([l, w, h])[:2]
        bow = l*w*h
        ribbon += 2*a + 2*b + bow
    return ribbon


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)
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
