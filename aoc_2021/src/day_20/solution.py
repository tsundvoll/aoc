import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm
from utility import parse

def first_task(input):
    count = 0

    img_enhancement = [1 if c == '#' else 0 for c in input[0]]

    img = []
    for i, word in enumerate(input[2:]):
        line = np.array([1 if c == '#' else 0 for c in word])
        img.append(line)
    
    img = np.array(img)

    pad_size = 3
    for s in range(2):
        if img_enhancement[0] == 1:
            img = np.pad(img, pad_size, 'constant', constant_values=s)
        else:
            img = np.pad(img, pad_size, 'constant', constant_values=0)
        h, w = img.shape
        new_img = img.copy()

        for row in range(1, h - 1):
            for col in range(1, w - 1):
                # print(row, col)
                idx = ''
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        idx += str(img[r][c])
                        # print(idx)
                i = int(idx, 2)
                new_pixel = img_enhancement[i]
                new_img[row][col] = new_pixel
        img = new_img.copy()
        img = img[1:-1, 1:-1]
    count = np.count_nonzero(img)
    
    return count


def second_task(input):
    count = 0

    img_enhancement = [1 if c == '#' else 0 for c in input[0]]

    img = []
    for i, word in enumerate(input[2:]):
        line = np.array([1 if c == '#' else 0 for c in word])
        img.append(line)
    
    img = np.array(img)

    pad_size = 2
    for s in range(50):
        if img_enhancement[0] == 1:
            img = np.pad(img, pad_size, 'constant', constant_values=s%2)
        else:
            img = np.pad(img, pad_size, 'constant', constant_values=0)
        h, w = img.shape
        new_img = img.copy()

        for row in range(1, h - 1):
            for col in range(1, w - 1):
                # print(row, col)
                idx = ''
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        idx += str(img[r][c])
                        # print(idx)
                i = int(idx, 2)
                new_pixel = img_enhancement[i]
                new_img[row][col] = new_pixel
        img = new_img.copy()
        img = img[1:-1, 1:-1]
    count = np.count_nonzero(img)
    
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
