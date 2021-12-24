import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm
from utility import parse

prog = None

def run_alu(model_number):
    global prog

    variables = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for i, word in enumerate(prog):
        instr, *param = word.split(' ')

        if len(param) > 1 and (param[1].isdigit() or param[1][0] == '-'):
            b = int(param[1])
        elif len(param) > 1:
            b = variables[param[1]]

        if instr == 'inp':
            variables[param[0]] = next(model_number)
        elif instr == 'add':
            variables[param[0]] += b
        elif instr == 'mul':
            variables[param[0]] *= b
        elif instr == 'div':
            variables[param[0]] = int(variables[param[0]] / b)
        elif instr == 'mod':
            variables[param[0]] = variables[param[0]] % b
        elif instr == 'eql':
            variables[param[0]] = variables[param[0]] == b

    return variables

# def parse_alu(prog_list):
#     model_number = None
#     w = 0
#     x = 0
#     y = 0
#     z = 0

#     prog = []

#     for i, word in enumerate(prog_list):
#         instr, *param = word.split(' ')

#         if len(param) > 1 and (param[1].isdigit() or param[1][0] == '-'):
#             b = int(param[1])
#         elif len(param) > 1:
#             b = variables[param[1]]

#         if instr == 'inp':
#             variables[param[0]] = next(model_number)
#         elif instr == 'add':
#             variables[param[0]] += b
#         elif instr == 'mul':
#             variables[param[0]] *= b
#         elif instr == 'div':
#             variables[param[0]] = int(variables[param[0]] / b)
#         elif instr == 'mod':
#             variables[param[0]] = variables[param[0]] % b
#         elif instr == 'eql':
#             variables[param[0]] = variables[param[0]] == b

#     return variables


def first_task(input):
    global prog
    prog = input

    # model_number = map(int, '13579246899999')


    model_number_current = 99999999999999

    decr = list(range(10))
    decr[9] = 10


    count = 0
    # while model_number_current > 10000000000000:
    for _ in tqdm(range(99999999999999 - 10000000000000)):
        # model_number = map(int, str(model_number_current))
        model_number = map(int, '13579246899999')

        variables = run_alu(model_number)
        print()
        print(model_number_current)
        print(variables)
        if variables['z'] == 0:
            return model_number_current

        if str(model_number_current)[-1] == '1':
            model_number_current -= 2
        else:
            model_number_current -= 1

        break
        


def second_task(input):
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
