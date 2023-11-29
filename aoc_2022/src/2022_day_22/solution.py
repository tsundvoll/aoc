import math
import os
import re
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data, max_line_length=150):
    # max_line_length = 16  # 16 or 150
    height = len(input_data)
    width = max_line_length + 2
    board = []
    row_to_start_end: list[tuple[int, int]] = []
    for i in range(len(input_data) - 2):
        line = input_data[i]
        start_coord = None
        end_coord = None
        board_row = []
        for j, tile in enumerate(line):
            if tile == "\n":
                break
            if tile == " ":
                board_row.append(-1)
            else:
                if start_coord is None:
                    start_coord = j + 1
                if tile == ".":
                    board_row.append(0)
                elif tile == "#":
                    board_row.append(1)
                else:
                    # print(line)
                    raise RuntimeError

        assert not start_coord is None
        assert end_coord is None
        end_coord = j + 1

        row_to_start_end.append((start_coord, end_coord))
        pad_length = max_line_length - len(board_row)
        board_row.extend([-1] * pad_length)
        # print(len(board_row))
        board.append(np.array(board_row, dtype=int))

    del i
    del j
    del board_row
    del pad_length
    del start_coord
    del end_coord
    del tile
    del line

    board = np.array(board, dtype=int)
    board = np.pad(board, pad_width=1, mode="constant", constant_values=-1)

    commands = input_data[-1]
    del input_data

    # print(board)
    # print()
    distances = iter(tuple(map(int, re.findall(r"\d+", commands))))
    rotations = iter(tuple(re.findall(r"[a-zA-Z]", commands)))
    del commands

    face_to_dir = [
        np.array([0, 1]),  # Right
        np.array([1, 0]),  # Down
        np.array([0, -1]),  # Left
        np.array([-1, 0]),  # Up
    ]

    # print(height, width)

    end_index_row = width - 1  # 17
    end_index_col = height - 1  # 13

    # for row in range(1, height - 1):
    #     leftmost_pos = np.argmax(board[row] >= 0)
    #     # print(f"{leftmost_pos=}")

    # for row in range(1, height - 1):
    #     rightmost_pos = end_index_row - np.argmax(board[row][::-1] >= 0)
    #     # print(f"{rightmost_pos=}")

    # for col in range(1, width - 1):
    #     uppermost_pos = np.argmax(board[:, col] >= 0)
    #     # - print(board[:, col])
    #     # print(f"{uppermost_pos=}")

    # for col in range(1, width - 1):
    #     downmost_pos = end_index_col - np.argmax(board[:, col][::-1] >= 0)
    #     # - print(board[:, col])
    #     # print(f"{downmost_pos=}")

    pos = np.array([1, row_to_start_end[0][0]])
    del row_to_start_end
    face = 0  # Right [0,1,2,3] -> [RIGHT, DOWN, LEFT UP]
    dist = next(distances)
    while True:
        for _ in range(dist):
            # print(pos)
            next_pos = pos + face_to_dir[face]

            next_pos_row = next_pos[0]
            next_pos_col = next_pos[1]

            next_pos_tile = board[next_pos_row][next_pos_col]

            if next_pos_tile == 0:  # Can go there
                pos = next_pos
            elif next_pos_tile == 1:  # Hit wall
                break
            elif next_pos_tile == -1:  # Hit end of board
                if face == 0:  # Right; find leftmost tile
                    current_row = pos[0]
                    leftmost_col = np.argmax(board[current_row] >= 0)
                    next_pos_tile = board[current_row][leftmost_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([current_row, leftmost_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
                if face == 1:  # Down; find upmost tile
                    current_col = pos[1]
                    upmost_row = np.argmax(board[:, current_col] >= 0)
                    next_pos_tile = board[upmost_row][current_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([upmost_row, current_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
                if face == 2:  # Left; find rightmost tile
                    current_row = pos[0]
                    rightmost_col = end_index_row - np.argmax(
                        board[current_row][::-1] >= 0
                    )
                    next_pos_tile = board[current_row][rightmost_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([current_row, rightmost_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
                if face == 3:  # Up; find downmost tile
                    current_col = pos[1]
                    downmost_row = end_index_col - np.argmax(
                        board[:, current_col][::-1] >= 0
                    )
                    next_pos_tile = board[downmost_row][current_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([downmost_row, current_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
            else:
                raise RuntimeError

        try:
            rotation = next(rotations)
            dist = next(distances)
        except StopIteration:
            break
        if rotation == "R":
            face = (face + 1) % 4
        elif rotation == "L":
            face = (face - 1) % 4

    return 1000 * pos[0] + 4 * pos[1] + face


def second_task(input_data):
    max_line_length = 16  # 151
    max_line_length = 150  # 151
    height = len(input_data)
    width = max_line_length + 2
    board = []
    row_to_start_end: list[tuple[int, int]] = []
    for i in range(len(input_data) - 2):
        line = input_data[i]
        start_coord = None
        end_coord = None
        board_row = []
        for j, tile in enumerate(line):
            if tile == "\n":
                break
            if tile == " ":
                board_row.append(-1)
            else:
                if start_coord is None:
                    start_coord = j + 1
                if tile == ".":
                    board_row.append(0)
                elif tile == "#":
                    board_row.append(1)
                else:
                    # print(line)
                    raise RuntimeError

        assert not start_coord is None
        assert end_coord is None
        end_coord = j + 1

        row_to_start_end.append((start_coord, end_coord))
        pad_length = max_line_length - len(board_row)
        board_row.extend([-1] * pad_length)
        # print(len(board_row))
        board.append(np.array(board_row, dtype=int))

    del i
    del j
    del board_row
    del pad_length
    del start_coord
    del end_coord
    del tile
    del line

    board = np.array(board, dtype=int)
    board = np.pad(board, pad_width=1, mode="constant", constant_values=-1)

    commands = input_data[-1]
    del input_data

    # print(board)
    # print()
    distances = iter(tuple(map(int, re.findall(r"\d+", commands))))
    rotations = iter(tuple(re.findall(r"[a-zA-Z]", commands)))
    del commands

    face_to_dir = [
        np.array([0, 1]),  # Right
        np.array([1, 0]),  # Down
        np.array([0, -1]),  # Left
        np.array([-1, 0]),  # Up
    ]

    # print(height, width)

    end_index_row = width - 1  # 17
    end_index_col = height - 1  # 13

    # for row in range(1, height - 1):
    #     leftmost_pos = np.argmax(board[row] >= 0)
    #     # print(f"{leftmost_pos=}")

    # for row in range(1, height - 1):
    #     rightmost_pos = end_index_row - np.argmax(board[row][::-1] >= 0)
    #     # print(f"{rightmost_pos=}")

    # for col in range(1, width - 1):
    #     uppermost_pos = np.argmax(board[:, col] >= 0)
    #     # - print(board[:, col])
    #     # print(f"{uppermost_pos=}")

    # for col in range(1, width - 1):
    #     downmost_pos = end_index_col - np.argmax(board[:, col][::-1] >= 0)
    #     # - print(board[:, col])
    #     # print(f"{downmost_pos=}")

    pos = np.array([1, row_to_start_end[0][0]])
    del row_to_start_end
    face = 0  # Right [0,1,2,3] -> [RIGHT, DOWN, LEFT UP]
    dist = next(distances)
    while True:
        for _ in range(dist):
            # print(pos)
            next_pos = pos + face_to_dir[face]

            next_pos_row = next_pos[0]
            next_pos_col = next_pos[1]

            next_pos_tile = board[next_pos_row][next_pos_col]

            if next_pos_tile == 0:  # Can go there
                pos = next_pos
            elif next_pos_tile == 1:  # Hit wall
                break
            elif next_pos_tile == -1:  # Hit end of board
                if face == 0:  # Right; find leftmost tile
                    current_row = pos[0]
                    leftmost_col = np.argmax(board[current_row] >= 0)
                    next_pos_tile = board[current_row][leftmost_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([current_row, leftmost_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
                if face == 1:  # Down; find upmost tile
                    current_col = pos[1]
                    upmost_row = np.argmax(board[:, current_col] >= 0)
                    next_pos_tile = board[upmost_row][current_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([upmost_row, current_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
                if face == 2:  # Left; find rightmost tile
                    current_row = pos[0]
                    rightmost_col = end_index_row - np.argmax(
                        board[current_row][::-1] >= 0
                    )
                    next_pos_tile = board[current_row][rightmost_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([current_row, rightmost_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
                if face == 3:  # Up; find downmost tile
                    current_col = pos[1]
                    downmost_row = end_index_col - np.argmax(
                        board[:, current_col][::-1] >= 0
                    )
                    next_pos_tile = board[downmost_row][current_col]
                    if next_pos_tile == 0:  # Can go there
                        pos = np.array([downmost_row, current_col])
                    elif next_pos_tile == 1:  # Hit wall
                        break
                    else:
                        raise RuntimeError
            else:
                raise RuntimeError

        try:
            rotation = next(rotations)
            dist = next(distances)
        except StopIteration:
            return 1000 * pos[0] + 4 * pos[1] + face
        if rotation == "R":
            face = (face + 1) % 4
        elif rotation == "L":
            face = (face - 1) % 4

    return count


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line, open(input_file, "r")))

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
