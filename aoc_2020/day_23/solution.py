import time
import numpy as np

data = [x for x in open('input.txt').read().splitlines()]


def move_cups_old(current_cup_idx, cup_arangement, n_cups):
    current_cup = cup_arangement[current_cup_idx]


    pick_up_idxs = [(current_cup_idx + 1) % n_cups, (current_cup_idx + 2) % n_cups, (current_cup_idx + 3) % n_cups]
    pick_up = [
        cup_arangement[pick_up_idxs[0]],
        cup_arangement[pick_up_idxs[1]],
        cup_arangement[pick_up_idxs[2]],
    ]


    destination_cup = current_cup - 1
    if destination_cup <= 0:
        destination_cup = n_cups
    while destination_cup in pick_up:
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = n_cups
    # print(f"{destination_cup=}")


    for pick in pick_up:
        cup_arangement.remove(pick)
    
    destination_idx = (cup_arangement.index(destination_cup) + 1) % n_cups
    cup_arangement[destination_idx:destination_idx] = pick_up

    current_cup_idx = (cup_arangement.index(current_cup) + 1) % n_cups

    return current_cup_idx, cup_arangement


def move_cups(current_cup_idx, cup_arangement, n_cups):
    current_cup = cup_arangement[current_cup_idx]

    # pick_up_idxs = np.mod(np.array([current_cup_idx+1, current_cup_idx+2, current_cup_idx+3]), n_cups)
    pick_up_idxs = [(current_cup_idx + 1) % n_cups, (current_cup_idx + 2) % n_cups, (current_cup_idx + 3) % n_cups]
    
    picked_up = cup_arangement[pick_up_idxs]

    destination_cup = ((current_cup - 2) % n_cups) + 1    
    while (destination_cup == picked_up[0]) or (destination_cup == picked_up[1]) or (destination_cup == picked_up[2]):
        destination_cup = ((destination_cup - 2) % n_cups) + 1

    cup_arangement = np.delete(cup_arangement, pick_up_idxs)
    
    destination_idx = np.mod(np.where(cup_arangement == destination_cup)[0][0] + 1, n_cups)
    cup_arangement = np.insert(cup_arangement, destination_idx, picked_up)

    current_cup_idx = np.mod(np.where(cup_arangement == current_cup)[0][0] + 1, n_cups)

    return current_cup_idx, cup_arangement



def get_answer(cup_arrangement):
    if isinstance(cup_arrangement, np.ndarray):
        one_index = np.where(cup_arrangement == 1)[0][0]
    else:
        one_index = cup_arrangement.index(1)
    print(one_index)
    answer = ""
    i = one_index + 1
    while len(answer) < 8:
        answer += str(cup_arrangement[i%9])
        i += 1
    return answer


def get_answer_task_2(cup_arrangement):
    if isinstance(cup_arrangement, np.ndarray):
        one_index = np.where(cup_arrangement == 1)[0][0]
    else:
        one_index = cup_arrangement.index(1)
    
    next_1 = cup_arrangement[(one_index+1)%1000000]
    next_2 = cup_arrangement[(one_index+2)%1000000]
    return next_1, next_2


def solution_part_1():
    cup_arrangement = [3,1,5,6,7,9,8,2,4]
    current_cup_idx = 0
    for _ in range(100):
        _, _, current_cup_idx, cup_arrangement = move_cups_old(current_cup_idx, cup_arrangement)

    return get_answer(cup_arrangement)


def solution_part_2():
    return "Not solved yet"


if __name__ == "__main__":
    print("Part 1")
    tic = time.perf_counter()
    print("- answer:", solution_part_1())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")

    print("Part 2")
    tic = time.perf_counter()
    print("- answer:", solution_part_2())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")
