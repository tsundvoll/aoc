import os
import time

import numpy as np
import pyperclip


def first_task(input_data):
    count = 0
    height = len(input_data)
    width = len(input_data[0])

    trees = np.zeros((height, width), dtype=int)
    for row in range(height):
        for col in range(width):
            trees[row][col] = input_data[row][col]

    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                count += 1
                continue

            tree = trees[row][col]

            left = trees[row, :col]
            right = trees[row, col + 1 :]
            up = trees[:row, col]
            down = trees[row + 1 :, col]

            if (
                tree > max(left)
                or tree > max(right)
                or tree > max(up)
                or tree > max(down)
            ):
                count += 1
    return count


def second_task(input_data):
    count = 0
    height = len(input_data)
    width = len(input_data[0])

    trees = np.zeros((height, width), dtype=int)
    for row in range(height):
        for col in range(width):
            trees[row][col] = input_data[row][col]

    max_scenic_score = 0

    for row in range(height):
        for col in range(width):
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                count += 1
                continue

            tree = trees[row][col]

            left = list(reversed(trees[row, :col]))
            right = trees[row, col + 1 :]
            up = list(reversed(trees[:row, col]))
            down = trees[row + 1 :, col]

            dist_left = len(left)
            for i, val in enumerate(left):
                if val >= tree:
                    dist_left = i + 1
                    break

            dist_right = len(right)
            for i, val in enumerate(right):
                if val >= tree:
                    dist_right = i + 1
                    break

            dist_up = len(up)
            for i, val in enumerate(up):
                if val >= tree:
                    dist_up = i + 1
                    break

            dist_down = len(down)
            for i, val in enumerate(down):
                if val >= tree:
                    dist_down = i + 1
                    break

            scenic_score = dist_left * dist_right * dist_up * dist_down
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
