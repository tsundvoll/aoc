import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm
from utility import parse


def run_alu(prog, input_var, variables):
    for word in prog:
        instr, *param = word.split(' ')

        if len(param) > 1 and (param[1].isdigit() or param[1][0] == '-'):
            b = int(param[1])
        elif len(param) > 1:
            b = variables[param[1]]

        if instr == 'inp':
            variables[param[0]] = input_var
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


def first_task(input):
    chunks = []
    chunk = []
    is_first = True
    for line in input:
        op, *param = line.split(' ')
        if op == 'inp':
            if not is_first:
                chunks.append(chunk)
            chunk = []
        
        is_first = False
        chunk.append(line)
    chunks.append(chunk)

    variables_start = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    variables = variables_start.copy()

    possibilities = []

    variables = variables_start.copy()
    for chunk in chunks[::-1]:
        for w in range(1,10):
            for z in tqdm(range(100000000)):
                variables = variables_start.copy()
                variables['z'] = z
                run_alu(chunk, w, variables)
                if variables['z'] == 0:
                    print(variables['z'])
                    print(variables)
                    break
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
