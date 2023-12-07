import math
import os
import time

import numpy as np
import pyperclip
from tqdm import tqdm


def first_task(input_data: list):
    count = 1
    times = list(map(int, input_data[0].strip("Time:").split()))
    distances = list(map(int, input_data[1].strip("Distance:").split()))

    n_races = len(times)
    for race_id in range(n_races):
        race_duration = times[race_id]
        record_distance = distances[race_id]

        possible_hold_time = []
        for hold_time in range(race_duration):
            remaining_time = race_duration - hold_time
            speed = hold_time
            distance = remaining_time * speed
            if distance > record_distance:
                possible_hold_time.append(hold_time)

        count *= len(possible_hold_time)

        print(race_duration)
        print(record_distance)

    return count


def second_task(input_data: list):
    times = list(input_data[0].strip("Time:").split())
    distances = list(input_data[1].strip("Distance:").split())

    race_duration = ""
    for time in times:
        race_duration += time
    race_duration = int(race_duration)

    race_distance = ""
    for distance in distances:
        race_distance += distance
    race_distance = int(race_distance)

    possible_hold_time = []
    for hold_time in range(race_duration):
        remaining_time = race_duration - hold_time
        speed = hold_time
        distance = remaining_time * speed
        if distance > race_distance:
            possible_hold_time.append(hold_time)

    return len(possible_hold_time)


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
