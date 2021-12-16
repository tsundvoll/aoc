import os
import time

import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    grid = np.zeros((1000, 1000), dtype=bool)
    for i, word in enumerate(input):
        line = word.split()
        if line[1].isalpha():
            command = line[1]
        else:
            command = line[0]

        from_coord = line[-3]
        to_coord = line[-1]

        # print(command, from_coord, to_coord)

        from_x, from_y = list(map(int, from_coord.split(',')))
        to_x, to_y = list(map(int, to_coord.split(',')))

        s = grid[from_x:to_x+1, from_y:to_y+1]

        if command == 'toggle':
            value = ~grid[from_x:to_x+1, from_y:to_y+1]
        if command == 'on':
            value = 1
        if command == 'off':
            value = 0

        grid[from_x:to_x+1, from_y:to_y+1] = value

        # print(s)
        # print(grid)
    
    grid = grid.astype(dtype=int)

    return np.count_nonzero(grid == 1)


def second_task(input):
    grid = np.zeros((1000, 1000))
    for i, word in enumerate(input):
        line = word.split()
        if line[1].isalpha():
            command = line[1]
        else:
            command = line[0]

        from_coord = line[-3]
        to_coord = line[-1]

        from_x, from_y = list(map(int, from_coord.split(',')))
        to_x, to_y = list(map(int, to_coord.split(',')))

        s = grid[from_x:to_x+1, from_y:to_y+1]

        if command == 'toggle':
            value = grid[from_x:to_x+1, from_y:to_y+1] + 2
        if command == 'on':
            value = grid[from_x:to_x+1, from_y:to_y+1] + 1
        if command == 'off':
            value = np.clip(grid[from_x:to_x+1, from_y:to_y+1] - 1, a_min=0, a_max=None)

        grid[from_x:to_x+1, from_y:to_y+1] = value

    score = int(np.sum(grid))
    print(score)
    return score


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

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
