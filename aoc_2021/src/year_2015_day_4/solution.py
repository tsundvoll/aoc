import hashlib
import os
import time

import pyperclip
from utility import parse


def first_task(input):
    number = 1
    
    while True:
        s = f'{input}{number}'.encode('ascii')
        md5 = hashlib.md5(s).hexdigest()
        if md5[:5] == '00000':
            return number
        number += 1

    return number


def second_task(input):
    number = 1
    
    while True:
        s = f'{input}{number}'.encode('ascii')
        md5 = hashlib.md5(s).hexdigest()
        if md5[:6] == '000000':
            return number
        number += 1

    return number


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)[0]

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
