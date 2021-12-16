import math
import os
import time

import cv2
import numpy as np
import pyperclip
from utility import parse


def first_task(input):
    lines = [] 
    folds = []
    is_folds = False
    max_x = 0
    max_y = 0
    for i, word in enumerate(input):
        if word == '':
            is_folds = True
            continue

        if is_folds:
            a, l = word.split(' ')[2].split('=')
            folds.append((a, int(l)))
        else:
            x, y = list(map(int, word.split(',')))
            lines.append((x,y))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    
    page = np.zeros((max_y+1, max_x+1))

    for x, y in lines:
        page[y][x] = 1


    axis, line = folds[0]
    if axis == 'y':
        page_to_keep = page[:line,:]
        page_to_fold = page[line+1:,:]

        flipped_page_to_fold = np.flip(page_to_fold, axis=0)

        new_page = page_to_keep + flipped_page_to_fold

    elif axis == 'x':
        page_to_keep = page[:, :line]
        page_to_fold = page[:, line+1:]

        flipped_page_to_fold = np.flip(page_to_fold, axis=1)

        new_page = page_to_keep + flipped_page_to_fold

    return np.count_nonzero(new_page)


def second_task(input):
    lines = [] 
    folds = []
    is_folds = False
    max_x = 0
    max_y = 0
    for i, word in enumerate(input):
        if word == '':
            is_folds = True
            continue

        if is_folds:
            a, l = word.split(' ')[2].split('=')
            folds.append((a, int(l)))
        else:
            x, y = list(map(int, word.split(',')))
            lines.append((x,y))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
    
    page = np.zeros((max_y+1, max_x+1))

    for x, y in lines:
        page[y][x] = 1

    for axis, line in folds:
        if axis == 'y':
            page_to_keep = page[:line,:]
            page_to_fold = page[line+1:,:]

            flipped_page_to_fold = np.flip(page_to_fold, axis=0)

            new_page = page_to_keep + flipped_page_to_fold

        elif axis == 'x':
            page_to_keep = page[:, :line]
            page_to_fold = page[:, line+1:]

            flipped_page_to_fold = np.flip(page_to_fold, axis=1)

            new_page = page_to_keep + flipped_page_to_fold

        page = new_page

    cv2.imshow('Image', new_page)
    cv2.waitKey(0) # waits until a key is pressed
    cv2.destroyAllWindows() # destroys the window showing image
    return np.count_nonzero(new_page)


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
