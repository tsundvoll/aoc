import functools
import math
import os
import time


import numpy as np
import pyperclip
from tqdm import tqdm
from utility import parse

def first_task(input):
    count = 0
    p0 = int(input[0])
    p1 = int(input[1])

    placement = [p0, p1]

    score = [0, 0]

    die = 0
    turn = 0
    while True:

        roll = 0
        for _ in range(3):
            count += 1
            die += 1
            if die > 100:
                die = 1
            
            roll += die

        print(roll, end=' ')

        placement[turn] = (((placement[turn] + roll)-1) % 10 ) + 1
        
        print(placement[turn], end=' ')

        score[turn] += placement[turn]
        
        print(score[turn])

        print(turn+1)
        turn = (turn + 1)%2


        if score[0] >= 1000:
            print(score, count)
            return score[1] * count
        elif score[1] >= 1000:
            print(score, count)
            return score[0] * count


POSSIBLE_OUTCOMES = [
    1+1+1,
    1+1+2,
    1+1+3,
    1+2+1,
    1+2+2,
    1+2+3,
    1+3+1,
    1+3+2,
    1+3+3,
    2+1+1,
    2+1+2,
    2+1+3,
    2+2+1,
    2+2+2,
    2+2+3,
    2+3+1,
    2+3+2,
    2+3+3,
    3+1+1,
    3+1+2,
    3+1+3,
    3+2+1,
    3+2+2,
    3+2+3,
    3+3+1,
    3+3+2,
    3+3+3,
]

@functools.cache
def game(placement_in, score_in, turn, roll_value):

    placement = list(placement_in)
    score = list(score_in)

    placement[turn] = (((placement_in[turn] + roll_value)-1) % 10 ) + 1
    score[turn] += placement[turn]

    if score[0] >= 21:
        return 1, 0
    elif score[1] >= 21:
        return 0, 1

    p0_wins = 0
    p1_wins = 0
    for r in POSSIBLE_OUTCOMES:
        p0_win, p1_win = game(tuple(placement), tuple(score), turn=(turn + 1)%2, roll_value=r)
        p0_wins += p0_win
        p1_wins += p1_win

    return p0_wins, p1_wins


def second_task(input):
    count = 0
    p0 = int(input[0])
    p1 = int(input[1])

    placement = (p0, p1)
    score = (0, 0)
    
    p0_wins = 0
    p1_wins = 0
    for r in POSSIBLE_OUTCOMES:
        p0_win, p1_win = game(placement, score, turn=0, roll_value=r)
        p0_wins += p0_win
        p1_wins += p1_win

    return max(p0_wins, p1_wins)


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
