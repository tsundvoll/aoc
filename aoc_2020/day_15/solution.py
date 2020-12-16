
from tqdm import tqdm
import time

data = [11,18,0,20,1,7,16]


def play_game_until(starting_numbers, stop_at_turn):
    history = {}
    # Set up the first rounds
    turn = 1
    last_number = 0
    for number in starting_numbers:
        history[number] = [turn, None] # [prev, prev_prev]
        last_number = number
        turn += 1
        if turn > stop_at_turn:
            return last_number

    # while turn <= stop_at_turn:
    for turn in range(len(starting_numbers)+1, stop_at_turn+1):
        # print("\nNew turn")
        # print("Turn:", turn)
        # print("History:", history)
        # print("Last number:", last_number)
        prev_turn_spoken, prev_prev_turn_spoken = history[last_number]
        
        # print("Prev turn spoken:", prev_turn_spoken)
        # print("Prev prev turn spoken:", prev_prev_turn_spoken)

        if prev_prev_turn_spoken is None:
            new_number = 0
        else:
            new_number = prev_turn_spoken - prev_prev_turn_spoken
        # print("Spoken number:", new_number)

        # If spken number not in history, it is new
        if new_number in history.keys():
            prev, prev_prev = history[new_number]
            history[new_number] = [turn, prev]
        else:
            history[new_number] = [turn, None]


        last_number = new_number
        turn += 1

    return last_number



def solution_part_1():
    return play_game_until(data, 2020)


def solution_part_2():
    return play_game_until(data, 30000000)


if __name__ == "__main__":
    tic = time.perf_counter()
    print("Answer Part 1:", solution_part_1())
    toc = time.perf_counter()
    print(f"Time Part 1: {toc-tic}")

    tic = time.perf_counter()
    print("Answer Part 2:", solution_part_2())
    toc = time.perf_counter()
    print(f"Time Part 2: {toc-tic}")

    # 639
    # 266