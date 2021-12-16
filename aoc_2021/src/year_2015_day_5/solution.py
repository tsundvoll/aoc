import os
import time

import pyperclip
from utility import parse


def first_task(input):
    count = 0 

    for word in input:
        n_vowels = sum([
            word.count('a'),
            word.count('e'),
            word.count('i'),
            word.count('o'),
            word.count('u'),
        ])

        n_letter_twice = 0
        for i in range(len(word)-1):
            c0 = word[i]
            c1 = word[i+1]
            if c0 == c1:
                n_letter_twice += 1

        bad_strings = sum([
            word.count('ab'),
            word.count('cd'),
            word.count('pq'),
            word.count('xy'),
        ])

        if n_vowels >= 3 and n_letter_twice and not bad_strings:
            count += 1

    return count

def second_task(input):
    count = 0 
    for word in input:
        n_pair_twice = 0
        n_letter_repeats = 0
        for i in range(len(word)-2):
            c0 = word[i]
            c1 = word[i+1]
            c2 = word[i+2]
            if c0 == c2:
                n_letter_repeats += 1

            if word[i+2:].count(c0 + c1):
                n_pair_twice += 1

        if n_pair_twice and n_letter_repeats:
            count += 1

    return count


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
