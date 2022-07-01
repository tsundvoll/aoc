import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm
from utility import parse

def first_task(input):
    count = 0
    grid = np.zeros((101, 101, 101))
    for i, line in enumerate(input):
        on_off, coords = line.split(' ')
        numbers = [coord.split('=')[1] for coord in coords.split(',')]
        x_min, x_max = map(lambda a : a + 0, map(int, numbers[0].split('..')))
        y_min, y_max = map(lambda a : a + 0, map(int, numbers[1].split('..')))
        z_min, z_max = map(lambda a : a + 0, map(int, numbers[2].split('..')))

        if x_min < -50 or x_max > 50 or y_min < -50 or y_max > 50 or z_min < -50 or z_max > 50:
            continue
    
        # print(on_off)
        # print(x_min, x_max, y_min, y_max, z_min, z_max)

        if on_off == 'on':
            value = 1
        elif on_off == 'off':
            value = 0
        else:
            raise ValueError
        grid[x_min + 50:x_max + 51, y_min + 50:y_max + 51, z_min + 50:z_max + 51] = value


    return np.count_nonzero(grid)


def second_task(input):
    count = 0
    grid = np.zeros((101, 101, 101))

    x_minimum = math.inf
    x_maximum = -math.inf
    y_minimum = math.inf
    y_maximum = -math.inf
    z_minimum = math.inf
    z_maximum = -math.inf

    for i, line in enumerate(input):
        on_off, coords = line.split(' ')
        numbers = [coord.split('=')[1] for coord in coords.split(',')]
        x_min, x_max = map(lambda a : a + 0, map(int, numbers[0].split('..')))
        y_min, y_max = map(lambda a : a + 0, map(int, numbers[1].split('..')))
        z_min, z_max = map(lambda a : a + 0, map(int, numbers[2].split('..')))

        if x_min < x_minimum:
            x_minimum = x_min

        if x_max > x_maximum:
            x_maximum = x_max

        if y_min < y_minimum:
            y_minimum = y_min

        if y_max > y_maximum:
            y_maximum = y_max

        if z_min < z_minimum:
            z_minimum = z_min

        if z_max > z_maximum:
            z_maximum = z_max

        # if on_off == 'off':
        #     print(
        #         x_minimum,
        #         x_maximum,
        #         y_minimum,
        #         y_maximum,
        #         z_minimum,
        #         z_maximum,
        #     )
        #     break

    
    
    grid = np.zeros(
        (
            abs(int(x_minimum))+abs(int(x_maximum)),
            abs(int(y_minimum))+abs(int(y_maximum)),
            abs(int(z_minimum))+abs(int(z_maximum)),
        ),
        dtype='int'
    )

    for i, line in enumerate(input):
        on_off, coords = line.split(' ')
        numbers = [coord.split('=')[1] for coord in coords.split(',')]
        x_min, x_max = map(lambda a : a + x_minimum, map(int, numbers[0].split('..')))
        y_min, y_max = map(lambda a : a + y_minimum, map(int, numbers[1].split('..')))
        z_min, z_max = map(lambda a : a + z_minimum, map(int, numbers[2].split('..')))
    
        # print(on_off)
        # print(x_min, x_max, y_min, y_max, z_min, z_max)

        if on_off == 'on':
            value = 1
        elif on_off == 'off':
            value = 0
        else:
            raise ValueError
        grid[
            x_min + x_minimum:x_max + x_minimum+1,
            y_min + y_minimum:y_max + y_minimum+1,
            z_min + z_minimum:z_max + z_minimum+1
        ] = value


    return np.count_nonzero(grid)


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
