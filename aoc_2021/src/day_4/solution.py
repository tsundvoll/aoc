import os
import time

import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    boards = []
    board = []
    n_boards = 0
    for i, word in enumerate(input):
        if i == 0:
            numbers = list(map(int, input[0].split(',')))
        elif word == '' or i == len(input):
            if len(board) != 0:
                boards.append(np.array(board))
                n_boards += 1
            board = []
        else:
            row = np.array(list(map(int, word.split())))
            board.append(row)

    boards = np.array(boards, dtype=int)
    score = np.array([np.zeros((5,5))]*n_boards)
    for n in numbers:
        for i, board in enumerate(boards):
            if len(np.where((board==n))[0]):
                s = [i, np.where((board==n))[0][0], np.where((board==n))[1][0]]
                score[i][s[1]][s[2]] = 1
            
            is_winning = True
            for row in score[i]:
                is_winning = True
                for el in row:
                    if el == 0:
                        is_winning = False

                if is_winning:
                    s = 0
                    for row in range(5):
                        for col in range(5):
                            if score[i][row][col] == 0:
                                s += board[row][col]
                    print(i, 'is winning with', n, s, n*s)
                    return n* s

            for c in range(5):
                col = score[i][:,c]
                for el in col:
                    if el == 0:
                        is_winning = False

                if is_winning:
                    s = 0
                    for row in range(5):
                        for col in range(5):
                            if score[i][row][col] == 0:
                                s += board[row][col]
                    print(i, 'is winning with', n, s, n*s)
                    return n* s
    return None


def second_task(input):
    boards = []
    board = []
    n_boards = 0
    for i, word in enumerate(input):
        if i == 0:
            numbers = list(map(int, input[0].split(',')))
        elif word == '' or i == len(input):
            if len(board) != 0:
                boards.append(np.array(board))
                n_boards += 1
            board = []
        else:
            row = np.array(list(map(int, word.split())))
            board.append(row)

    boards = np.array(boards, dtype=int)
    board_idx = set([b for b in range(len(boards))])

    score = np.array([np.zeros((5,5))]*n_boards)
    for n in numbers:
        for i, board in enumerate(boards):
            if not i in board_idx:
                continue
            if len(np.where((board==n))[0]):
                s = [i, np.where((board==n))[0][0], np.where((board==n))[1][0]]
                score[i][s[1]][s[2]] = 1
            
            is_winning = True
            for row in score[i]:
                is_winning = True
                for el in row:
                    if el == 0:
                        is_winning = False

                if is_winning:
                    s = 0
                    for row in range(5):
                        for col in range(5):
                            if score[i][row][col] == 0:
                                s += board[row][col]
                    board_idx.remove(i)
                    if len(board_idx) == 0:
                        print(i, 'is winning with row', n, s, n*s)
                        return n* s
            if not is_winning:

                is_winning = True
                for c in range(5):
                    col = score[i][:,c]
                    is_winning = True

                    for el in col:
                        if el == 0:
                            is_winning = False

                    if is_winning and i in board_idx:
                        s = 0
                        for row in range(5):
                            for col in range(5):
                                if score[i][row][col] == 0:
                                    s += board[row][col]
                        board_idx.remove(i)
                        if len(board_idx) == 0:
                            print(i, 'is winning with col', n, s, n*s)
                            return n * s
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
