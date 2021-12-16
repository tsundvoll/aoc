import copy
import os
import time

import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    n = len(input[0])
    m = len(input)
    gamma = np.zeros(n)
    for i, word in enumerate(input):
        l = np.array(list(map(int, list(word))))
        gamma += l

    gamma = gamma.astype(int)
    gamma = np.where(gamma > m/2, 0, 1)
    gamma_str = ''
    for el in gamma:
        gamma_str += str(el)
    epsilon = np.where(gamma == 1, 0, 1)
    epsilon_str = ''
    for el in epsilon:
        epsilon_str += str(el)

    return int(gamma_str, 2) *int(epsilon_str, 2)


def calc_gamma(input):
    n = len(input[0])
    m = len(input)
    gamma = np.zeros(n)
    for i, word in enumerate(input):
        l = np.array(list(map(int, list(word))))
        gamma += l            

    gamma = gamma.astype(int)
    gamma = np.where(gamma >= m/2.0, 1, 0)
    gamma_str = ''
    for el in gamma:
        gamma_str += str(el)

    return gamma_str


def calc_epsilon(input):
    n = len(input[0])
    m = len(input)
    gamma = np.zeros(n)
    for i, word in enumerate(input):
        l = np.array(list(map(int, list(word))))
        gamma += l

    gamma = gamma.astype(int)
    gamma = np.where(gamma >= m/2.0, 1, 0)
    gamma_str = ''
    for el in gamma:
        gamma_str += str(el)
    epsilon = np.where(gamma == 1, 0, 1)
    epsilon_str = ''
    for el in epsilon:
        epsilon_str += str(el)

    return epsilon_str


def second_task(input):
    n = len(input[0])
    m = len(input)
    gamma = np.zeros(n)
    for i, word in enumerate(input):
        l = np.array(list(map(int, list(word))))
        gamma += l

    gamma = gamma.astype(int)
    gamma = np.where(gamma >= m/2.0, 1, 0)
    gamma_str = ''
    for el in gamma:
        gamma_str += str(el)
    epsilon = np.where(gamma == 1, 0, 1)
    epsilon_str = ''
    for el in epsilon:
        epsilon_str += str(el)

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    # oxygen generator rating
    numbers = copy.deepcopy(input)
    oxygen = 0
    co2 = 0

    for i in range(len(input[0])):
        new_numbers = []
        for number in numbers:
            if int(number[i]) == int(gamma_str[i]):
                new_numbers.append(number)

        numbers = new_numbers
        gamma_str = calc_gamma(new_numbers)

        if len(numbers) == 1:
            oxygen = numbers[0]
            break
    
    numbers = copy.deepcopy(input)
    for i in range(len(input[0])):
        new_numbers = []
        for number in numbers:
            if int(number[i]) == int(epsilon_str[i]):
                new_numbers.append(number)

        numbers = new_numbers
        epsilon_str = calc_epsilon(new_numbers)

        if len(numbers) == 1:
            co2 = numbers[0]
            break

    return int(oxygen, 2) * int(co2, 2)


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input_Elias.txt')
    input_data = parse.parse_lines(input_file)

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 3)
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
