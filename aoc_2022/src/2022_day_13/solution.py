import copy
import os
import time

import pyperclip


def compare(left, right):
    while True:
        # print()
        # print(f"{left}")
        # print(f"{right}")

        if type(left) == int and type(right) == int:
            # print("Comparing ints")
            if left < right:
                # print(f"Left side is smaller, so inputs are IN THE RIGHT ORDER")
                return True
            elif left > right:
                # print(f"Right side is smaller, so inputs are NOT in the right order")
                return False
            else:  # left == right:
                # print(f"Undesisive")
                return None  # Undesisive
        elif type(left) == list and type(right) == list:
            # print("Comparing lists")
            if len(left) == 0 and len(right) == 0:
                # print(f"Pair is done checking")
                return None  # Undecisive
            elif len(left) == 0 and len(right) > 0:
                # print(f"Left side ran out of items, so inputs are IN THE RIGHT ORDER")
                return True
            elif len(left) > 0 and len(right) == 0:
                # print(
                #     f"Right side ran out of items, so inputs are NOT in the right order"
                # )
                return False
            else:  # len(left) > 0 and len(right) > 0
                first_left = left.pop(0)
                first_right = right.pop(0)
                result = compare(first_left, first_right)
                if result is None:
                    continue  # Undecisive
                return result
        elif type(left) == list and type(right) == int:
            # print("Comparing list and int")
            right = [right]
            result = compare(left, right)
            if result is None:
                continue  # Undecisive
            return result
        elif type(left) == int and type(right) == list:
            # print("Comparing int and list")
            left = [left]
            result = compare(left, right)
            if result is None:
                continue  # Undecisive
            return result
        else:
            # print(first_left)
            # print(first_right)
            raise RuntimeError("Invalid combination of types")


def first_task(input_data):
    pair = []
    pairs = []
    for i in range(len(input_data)):
        value = input_data[i]
        if value == "":
            pairs.append(pair)
            pair = []
        else:
            pair.append(eval(value))
    pairs.append(pair)

    count = 0
    for pair_id, pair in enumerate(pairs):
        left = pair[0]
        right = pair[1]
        header = f"Pair {pair_id+1}"
        # print()
        # print("#" * len(header))
        # print(header)
        # print("#" * 88, end="")
        result = compare(left, right)
        if result is None:
            raise RuntimeError

        # print(f"Pair {pair_id+1}: {result}")
        if result:
            # print("Add", pair_id + 1)
            count += pair_id + 1
            # print("Sum", count)

    return count


def second_task(input_data):
    packets_in_order = [[[2]], [[6]]]
    packets = []
    for i in range(len(input_data)):
        value = input_data[i]
        if value == "":
            continue
        packets.append(eval(value))

    print()
    for packet in packets:
        print(packet)
    print()

    print()
    for packet in packets_in_order:
        print(packet)
    print()

    for packet in packets:
        print(f"Inserting package: {packet}")
        is_inserted = False
        for i in range(len(packets_in_order)):
            left = copy.deepcopy(packet)
            right = copy.deepcopy(packets_in_order[i])
            result = compare(left, right)
            if result:
                # Insert if package is smaller than the next in the line
                packets_in_order.insert(i, packet)
                is_inserted = True
                break
        if not is_inserted:
            packets_in_order.append(packet)

        print()
        for packet in packets_in_order:
            print(packet)

    return (packets_in_order.index([[2]]) + 1) * (packets_in_order.index([[6]]) + 1)


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
