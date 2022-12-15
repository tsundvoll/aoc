import math
import os
import time

import cv2
import numpy as np
import pyperclip


def first_task(input_data):
    lines = []
    min_x = math.inf
    max_x = 0

    min_y = math.inf
    max_y = 0
    for i in range(len(input_data)):
        value = input_data[i]
        points = iter(value.split(" -> "))
        start_point = next(points)
        for end_point in points:
            x1, y1 = list(map(int, start_point.split(",")))
            x2, y2 = list(map(int, end_point.split(",")))
            if x1 > max_x:  # max_x
                max_x = x1
            if x2 > max_x:
                max_x = x2
            if x1 < min_x:  # min_x
                min_x = x1
            if x2 < min_x:
                min_x = x2
            if y1 > max_y:  # max_y
                max_y = y1
            if y2 > max_y:
                max_y = y2
            if y1 < min_y:  # min_y
                min_y = y1
            if y2 < min_y:
                min_y = y2
            lines.append([x1, y1, x2, y2])
            start_point = end_point

    # Insert the lines to the image
    img = np.zeros((max_y + 1, max_x + 1))
    for line in lines:
        x1, y1, x2, y2 = line
        img = cv2.line(img, (x1, y1), (x2, y2), color=1, thickness=1)

    def show_img(img):
        min_y = 0
        for row in range(min_y, max_y + 1):
            for col in range(min_x, max_x + 1):
                print(
                    "."
                    if img[row][col] == 0
                    else "#"
                    if img[row][col] == 1
                    else "o"
                    if img[row][col] == 9
                    else "~",
                    end="",
                )
            print()

    start_x, start_y = 500, 0
    img[start_y][start_x] = 8  # [y][x]

    count = 0
    x_pos = start_x
    y_pos = start_y
    while True:
        if y_pos >= max_y:
            break

        if img[y_pos + 1][x_pos] == 0:
            y_pos += 1
        elif img[y_pos + 1][x_pos - 1] == 0:
            y_pos += 1
            x_pos -= 1
        elif img[y_pos + 1][x_pos + 1] == 0:
            y_pos += 1
            x_pos += 1
        else:
            img[y_pos][x_pos] = 9
            count += 1
            # show_img(img)
            x_pos = start_x
            y_pos = start_y

    return count


def second_task(input_data):
    lines = []
    min_x = math.inf
    max_x = 0

    min_y = math.inf
    max_y = 0
    for i in range(len(input_data)):
        value = input_data[i]
        points = iter(value.split(" -> "))
        start_point = next(points)
        for end_point in points:
            x1, y1 = list(map(int, start_point.split(",")))
            x2, y2 = list(map(int, end_point.split(",")))
            if x1 > max_x:  # max_x
                max_x = x1
            if x2 > max_x:
                max_x = x2
            if x1 < min_x:  # min_x
                min_x = x1
            if x2 < min_x:
                min_x = x2
            if y1 > max_y:  # max_y
                max_y = y1
            if y2 > max_y:
                max_y = y2
            if y1 < min_y:  # min_y
                min_y = y1
            if y2 < min_y:
                min_y = y2
            lines.append([x1, y1, x2, y2])
            start_point = end_point

    min_y = 0
    max_y += 2
    min_x = 0
    max_x = max_x + max_y
    img = np.zeros((max_y + 1, max_x + 1))

    img = cv2.line(img, (min_x, max_y), (max_x, max_y), color=1, thickness=1)
    for line in lines:
        x1, y1, x2, y2 = line
        img = cv2.line(img, (x1, y1), (x2, y2), color=1, thickness=1)

    def show_img(img):
        for row in range(min_y, max_y + 1):
            for col in range(min_x, max_x + 1):
                print(
                    "."
                    if img[row][col] == 0
                    else "#"
                    if img[row][col] == 1
                    else "o"
                    if img[row][col] == 9
                    else "~",
                    end="",
                )
            print()
        print()

    start_x, start_y = 500, 0

    count = 0
    x_pos = start_x
    y_pos = start_y
    while True:
        if y_pos >= max_y:
            break

        if img[y_pos + 1][x_pos] == 0:
            y_pos += 1
        elif img[y_pos + 1][x_pos - 1] == 0:
            y_pos += 1
            x_pos -= 1
        elif img[y_pos + 1][x_pos + 1] == 0:
            y_pos += 1
            x_pos += 1
        else:
            img[y_pos][x_pos] = 9
            count += 1
            # show_img(img)
            if y_pos == 0 and x_pos == 500:
                break
            x_pos = start_x
            y_pos = start_y

    return count


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
