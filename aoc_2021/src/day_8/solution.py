import math
import os
import time

import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    count = 0
    for i, line in enumerate(input):
        hints, numbers = line.split(' | ')
        hints = hints.split(' ')
        numbers = numbers.split(' ')
        
        for n in numbers:
            if len(n) == 2 or len(n) == 4 or len(n) == 3 or len(n) == 7:
                count += 1
        
    return count


def second_task(input):
    count = 0
    for i, line in enumerate(input):
        hints, numbers = line.split(' | ')
        hints = hints.split(' ')
        numbers = numbers.split(' ')

        M = {}

        for h in hints:
            if len(h) == 2:
                # One
                M[1] = set(h)
                
            elif len(h) == 4:
                # 4
                M[4] = set(h)

            elif len(h) == 3:
                # 7
                M[7] = set(h)

            elif len(h) == 7:
                # 8
                M[8] = set(h)

        for h in hints:
            if len(h) == 6:
                # 0, 6 or 9

                missing = M[8] - set(h)
                # 8, the missing segment should be in 8, but none of the others
                if missing.issubset(M[8] - M[1] - M[4] - M[7]):
                    M[9] = set(h)

                # 0 , the missing segment should be in 8, but not 1 and 7
                elif missing.issubset(M[8] - M[1] - M[7]):
                    M[0] = set(h)
                else:
                    M[6] = set(h)
        for h in hints:
            if len(h) == 5:
                found_number = False
                # 2, 3 or 5

                missing = M[8] - set(h)
                # 5, the missing segment should be in (8, but not 6) and (8, but not 9)
                if missing.issubset((M[8] - M[6]).union(M[8] - M[9])):
                    M[5] = set(h)
                    found_number = True

        for h in hints:
            if set(h) in M.values():
                continue

            missing = M[8] - set(h)
            for m in missing:
                if m not in M[9]:
                    M[3] = set(h)
                    break
        
        for h in hints:
            if set(h) in M.values():
                continue
            else:
                M[2] = set(h)
                break

        a = ''
        for n in numbers:
            for k, v in M.items():
                if v == set(n):
                    a += str(k)
                    break

        keys = set(M.keys())
        if len(set([0,1,2,3,4,5,6,7,8,9])-keys):
            print(set([0,1,2,3,4,5,6,7,8,9])-keys)

        print(a)
        count += int(a)

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
