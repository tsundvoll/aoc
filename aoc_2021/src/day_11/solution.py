import math
import os
import time

import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    count = 0
    octo = []
    for i, word in enumerate(input):
        line = []
        for d in word:
            line.append(int(d))
        octo.append(np.array(line))

    octo = np.array(octo)
    # print(octo)

    for s in range(100):
        octo += 1
        # print()
        print(f'"Round {s+1} """""""""""""""""""""""""')
        print()
        # print(octo)

        has_flashed = set()

        while True:
            l_9 = np.where(octo > 9)

            to_flash = {
                (x, y)
                for x, y in zip(l_9[0], l_9[1])
                if (x, y) not in has_flashed
            }
            assert len(to_flash.intersection(has_flashed)) == 0

            if len(to_flash) == 0:
                for x, y in has_flashed:
                    print(len(has_flashed))
                    octo[x][y] = 0
                count += len(has_flashed)
                break

            for x, y in to_flash:
                has_flashed.add((x, y))
                idx = [
                    (x, y),
                    (x, y-1),
                    (x+1, y-1),
                    (x+1, y),
                    (x+1, y+1),
                    (x, y+1),
                    (x-1, y+1),
                    (x-1, y),
                    (x-1, y-1),
                ]
                for i in idx:
                    if i[0] < 0 or i[0] > 9 or i[1] < 0 or i[1] > 9:
                        continue
                    octo[i] += 1

        # print(has_flashed)
    print(octo)

    return count


def second_task(input):
    count = 0
    octo = []
    for i, word in enumerate(input):
        line = []
        for d in word:
            line.append(int(d))
        octo.append(np.array(line))

    octo = np.array(octo)

    for s in range(20000000):
        octo += 1

        has_flashed = set()
        while True:
            l_9 = np.where(octo > 9)

            to_flash = {
                (x, y)
                for x, y in zip(l_9[0], l_9[1])
                if (x, y) not in has_flashed
            }
            assert len(to_flash.intersection(has_flashed)) == 0

            if len(to_flash) == 0:
                for x, y in has_flashed:
                    print(len(has_flashed))
                    octo[x][y] = 0
                if len(has_flashed) == 100:
                    return s + 1 
                count += len(has_flashed)
                break

            for x, y in to_flash:
                has_flashed.add((x, y))
                idx = [
                    (x, y),
                    (x, y-1),
                    (x+1, y-1),
                    (x+1, y),
                    (x+1, y+1),
                    (x, y+1),
                    (x-1, y+1),
                    (x-1, y),
                    (x-1, y-1),
                ]
                for i in idx:
                    if i[0] < 0 or i[0] > 9 or i[1] < 0 or i[1] > 9:
                        continue
                    octo[i] += 1

    return count


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
