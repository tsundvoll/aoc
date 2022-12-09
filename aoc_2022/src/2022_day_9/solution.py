import os
import time

import pyperclip


def first_task(input_data):
    head = [0, 0]  # [row, col]
    tail = [0, 0]
    tail_positions = set()
    for i in range(len(input_data)):
        dir, dist = input_data[i].split()
        for i in range(int(dist)):
            if dir == "R":
                head[1] += 1
            elif dir == "L":
                head[1] -= 1
            elif dir == "U":
                head[0] -= 1
            elif dir == "D":
                head[0] += 1
            else:
                raise RuntimeError

            head_row = head[0]
            head_col = head[1]

            tail_row = tail[0]
            tail_col = tail[1]

            diff_row = head_row - tail_row
            diff_col = head_col - tail_col

            if abs(diff_row) > 1:
                tail[0] += 1 if head_row > tail_row else -1
                if abs(diff_col) > 0:
                    tail[1] += 1 if head_col > tail_col else -1
            elif abs(diff_col) > 1:
                tail[1] += 1 if head_col > tail_col else -1
                if abs(diff_row) > 0:
                    tail[0] += 1 if head_row > tail_row else -1

            tail_positions.add(tuple(tail))

    return len(tail_positions)


def second_task(input_data):
    knots = [[0, 0] for _ in range(10)]  # [row, col]
    tail_positions = set()
    for i_line in range(len(input_data)):
        dir, dist = input_data[i_line].split()

        for _ in range(int(dist)):
            head = knots[0]  # Move the head first
            if dir == "R":
                head[1] += 1
            elif dir == "L":
                head[1] -= 1
            elif dir == "U":
                head[0] -= 1
            elif dir == "D":
                head[0] += 1
            else:
                raise RuntimeError

            for i_knot in range(len(knots) - 1):
                head = knots[i_knot]
                tail = knots[i_knot + 1]

                head_row = head[0]
                head_col = head[1]

                tail_row = tail[0]
                tail_col = tail[1]

                diff_row = head_row - tail_row
                diff_col = head_col - tail_col

                if abs(diff_row) > 1:
                    tail[0] += 1 if head_row > tail_row else -1
                    if abs(diff_col) > 0:
                        tail[1] += 1 if head_col > tail_col else -1
                elif abs(diff_col) > 1:
                    tail[1] += 1 if head_col > tail_col else -1
                    if abs(diff_row) > 0:
                        tail[0] += 1 if head_row > tail_row else -1

            tail_positions.add(tuple(tail))

    return len(tail_positions)


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
