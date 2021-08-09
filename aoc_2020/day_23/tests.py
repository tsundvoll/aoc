from solution import *
import pytest
from tqdm import tqdm
import numpy as np


def test_part_1():
    cup_arrangement = np.array([3, 8, 9, 1, 2, 5, 4, 6, 7], dtype=np.int32)
    # cup_arrangement = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    current_cup_idx = 0
    n_cups = 9


    for _ in range(10):
        current_cup_idx, cup_arrangement = move_cups(current_cup_idx, cup_arrangement, n_cups)

    assert get_answer(cup_arrangement) == '92658374'

    
    cup_arrangement = np.array([3, 8, 9, 1, 2, 5, 4, 6, 7], dtype=np.int32)
    # cup_arrangement = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    current_cup_idx = 0
    for _ in range(100):
        current_cup_idx, cup_arrangement = move_cups(current_cup_idx, cup_arrangement, n_cups)

    assert get_answer(cup_arrangement) == '67384529'

    # # Move 1
    # pick_up, destination, current_cup_idx, cup_arangement = move_cups_old(current_cup_idx, cup_arrangement_test)
    # assert pick_up == [8, 9, 1]
    # assert destination == 2
    # assert cup_arangement == [3, 2, 8, 9, 1, 5, 4, 6, 7]
    # print("Done with move 1")


def test_part_2():
    # cup_arrangement = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    cup_arrangement = [3, 1, 5, 6, 7, 9, 8, 2, 4]
    current_cup_idx = 0
    n_cups = 1000000


    for x in range(10, n_cups+1):
        cup_arrangement.append(x)

    cup_arrangement = np.array(cup_arrangement, dtype=np.int32)

    tic = time.perf_counter()
    for _ in tqdm(range(10000000)):
        current_cup_idx, cup_arrangement = move_cups(current_cup_idx, cup_arrangement, n_cups)
    toc = time.perf_counter()
    print(f"Ran all moves in {toc - tic:0.6f} seconds")


    next_1, next_2 = get_answer_task_2(cup_arrangement)
    product = next_1 * next_2

    print(f"{next_1=}")
    print(f"{next_2=}")
    print(f"{product=}")

    # assert next_1 == 934001
    # assert next_2 == 159792
    # assert next_1*next_2 == 149245887792



if __name__ == "__main__":
    # tic = time.perf_counter()
    # test_part_1()
    # toc = time.perf_counter()
    # print(f"Ran first tests in {toc - tic:0.6f} seconds")
    

    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()
    print(f"Ran second tests in {toc - tic:0.4f} seconds")