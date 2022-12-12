import math
import operator
import os
import time

import pyperclip


def first_task(input_data):
    monkeys = []
    for i in range(0, len(input_data) - 1, 7):
        start_items = list(map(int, input_data[i + 1].split(": ")[1].split(", ")))
        operator_str = input_data[i + 2].split(" old ")[1].split()[0]
        value: str = input_data[i + 2].split(" old ")[1].split()[1]
        test = int(input_data[i + 3].split(" by ")[1])
        if_true = int(input_data[i + 4].split(" monkey ")[1])
        if_false = int(input_data[i + 5].split(" monkey ")[1])

        op = operator.add if operator_str == "+" else operator.mul
        operand = int(value) if value.isdigit() else None

        monkeys.append(
            [
                start_items,
                op,
                operand,
                test,
                if_true,
                if_false,
            ]
        )
    inspections = []
    for _ in range(20):
        for i, monkey in enumerate(monkeys):
            held_items, op, operand, test, if_true, if_false = monkey
            while held_items:
                inspections.append(i)
                item = held_items.pop(0)

                if operand:
                    new_after_inspection = op(item, operand)
                else:
                    new_after_inspection = op(item, item)

                new = new_after_inspection // 3
                if new % test == 0:
                    monkeys[if_true][0].append(new)
                else:
                    monkeys[if_false][0].append(new)

    each_inspections = []
    for i in range(len(monkeys)):
        each_inspections.append(inspections.count(i))

    return math.prod(sorted(each_inspections)[-2:])


def second_task(input_data):
    monkeys = []
    minimum_common_multiplier = 1
    for i in range(0, len(input_data) - 1, 7):
        start_items = list(map(int, input_data[i + 1].split(": ")[1].split(", ")))
        operator_str = input_data[i + 2].split(" old ")[1].split()[0]
        value: str = input_data[i + 2].split(" old ")[1].split()[1]
        test = int(input_data[i + 3].split(" by ")[1])
        minimum_common_multiplier *= test
        if_true = int(input_data[i + 4].split(" monkey ")[1])
        if_false = int(input_data[i + 5].split(" monkey ")[1])

        op = operator.add if operator_str == "+" else operator.mul
        operand = int(value) if value.isdigit() else None

        monkeys.append(
            [
                start_items,
                op,
                operand,
                test,
                if_true,
                if_false,
            ]
        )
    inspections = []
    for _ in range(10000):
        for i, monkey in enumerate(monkeys):
            held_items, op, operand, test, if_true, if_false = monkey
            while held_items:
                inspections.append(i)
                item = held_items.pop(0)

                if operand:
                    new_after_inspection = op(item, operand)
                else:
                    new_after_inspection = op(item, item)

                # Reduce the size of the worry level without losing any needed information
                if new_after_inspection > minimum_common_multiplier:
                    new_after_inspection %= minimum_common_multiplier

                if new_after_inspection % test == 0:
                    monkeys[if_true][0].append(new_after_inspection)
                else:
                    monkeys[if_false][0].append(new_after_inspection)

    each_inspections = []
    for i in range(len(monkeys)):
        each_inspections.append(inspections.count(i))

    return math.prod(sorted(each_inspections)[-2:])


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
