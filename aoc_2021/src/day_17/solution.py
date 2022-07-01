import math
import os
import time

import numpy as np
import pyperclip
from utility import parse
from tqdm import tqdm

def first_task(input):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    line = input[0].split(' ')
    for word in line:
        if word[0] == 'x':
            x_min, x_max = map(int, word.split('x=')[1].split(',')[0].split('..'))
        elif word[0] == 'y':
            y_min, y_max = map(int, word.split('y=')[1].split(',')[0].split('..'))

    print(x_min, x_max, y_min, y_max)
    print()

    start_vels_x = range(x_max)
    start_vels_y = range(y_min, 100)

    exprs = []
    for x_vel in start_vels_x:
        for y_vel in start_vels_y:
            in_target = 0
            highest_y = 0
            expr = np.array([0, 0, x_vel, y_vel, in_target, highest_y])
            exprs.append(expr)
    exprs = np.array(exprs)

    print(exprs.shape)

    y_max = 0
    valid_e = set()
    for _ in range(200):
        new_exprs = []
        for e in exprs:
            e[0] += e[2]
            e[1] += e[3]
            e[2] = max(0, e[2]-1)
            e[3] = e[3]-1

            if e[1] > e[5]:
                e[5] = e[1]

            if e[0] in range(x_min, x_max) and e[1] in range(y_min, y_max):
                e[4] = 1
                valid_e.add(tuple(e))
                if e[5] > y_max:
                    y_max = e[5]

            if e[0] > x_max or e[1] < y_min:
                pass
            else:
                # Keep experiment
                new_exprs.append(e)
        exprs = np.array(new_exprs)


    print('n_valid:', len(valid_e))

    return y_max


# def second_task(input):
#     x_min = 0
#     x_max = 0
#     y_min = 0
#     y_max = 0
#     line = input[0].split(' ')
#     for word in line:
#         if word[0] == 'x':
#             x_min, x_max = map(int, word.split('x=')[1].split(',')[0].split('..'))
#         elif word[0] == 'y':
#             y_min, y_max = map(int, word.split('y=')[1].split(',')[0].split('..'))

#     print(x_min, x_max, y_min, y_max)
#     print()

#     start_vels_x = range(x_max)
#     start_vels_y = range(y_min-10, 200)

#     exprs = []
#     for x_vel in start_vels_x:
#         for y_vel in start_vels_y:
#             in_target = 0
#             highest_y = 0
#             expr = np.array([0, 0, x_vel, y_vel, in_target, highest_y])
#             exprs.append(expr)
#     exprs = np.array(exprs)

#     print(exprs.shape)

#     count = 0
#     highest = 0

#     for _ in range(300):
#         for e in exprs:
#             e[0] += e[2]
#             e[1] += e[3]
#             e[2] = max(0, e[2]-1)
#             e[3] = e[3]-1

#             if e[0] in range(x_min, x_max+1) and e[1] in range(y_min, y_max+1):
#                 e[4] = 1
#                 count += 1
#                 if e[1] > highest:
#                     highest = e[1]
#                 # print(e[2], e[3])

#         expr_to_keep = np.nonzero(exprs[:,0] <= x_max)
#         exprs = exprs[expr_to_keep]

#         expr_to_keep = np.nonzero(exprs[:,1] >= y_min)
#         exprs = exprs[expr_to_keep]

#     print('highest:', highest)
#     return count
#     # valid_e = len(np.nonzero(expr[:,4] == 1))
#     # return valid_e

def second_task(input):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    line = input[0].split(' ')
    for word in line:
        if word[0] == 'x':
            x_min, x_max = map(int, word.split('x=')[1].split(',')[0].split('..'))
        elif word[0] == 'y':
            y_min, y_max = map(int, word.split('y=')[1].split(',')[0].split('..'))

    print(x_min, x_max, y_min, y_max)
    print()

    start_vels_x = range(1000)
    start_vels_y = range(y_min-100, 500)

    count = 0
    for x_vel_start in start_vels_x:
        for y_vel_start in start_vels_y:
            x_vel = x_vel_start
            y_vel = y_vel_start
            x_pos = 0
            y_pos = 0
            while True:
                x_pos += x_vel
                y_pos += y_vel
                if x_vel > 0:
                    x_vel = x_vel - 1
                elif x_vel < 0:
                    x_vel = x_vel + 1
                y_vel -= 1
                if x_pos in range(x_min, x_max+1) and y_pos in range(y_min, y_max+1):
                    count += 1
                    break
                elif x_pos > x_max or y_pos < y_min:
                    break
    
    return count



def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

    # t_start = time.time()
    # first_answer = first_task(input_data)
    # t_end = time.time()
    # first_time = round(t_end - t_start, 2)
    # if first_answer is not None:
    #     pyperclip.copy(str(first_answer))
    #     pyperclip.paste()

    # print('#############################')
    # print('The answer to the 1st task is')
    # print(first_answer, f'in {first_time} seconds')

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
