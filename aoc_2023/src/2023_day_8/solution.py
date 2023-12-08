import math
import os
import time

import pyperclip


def first_task(input_data: list):
    instructions = input_data[0]
    dict_graph = {}
    for i in range(2, len(input_data)):
        value = input_data[i]
        source, rest = value.split(" = ")
        rest = rest.strip("(")
        rest = rest.strip(")")
        left, right = rest.split(", ")
        dict_graph[source] = {"left": left, "right": right}

    parent = "AAA"
    child = ""

    step = 0
    while child != "ZZZ":
        instruction = instructions[step % len(instructions)]
        step += 1

        if instruction == "L":
            child = dict_graph[parent]["left"]
        else:
            child = dict_graph[parent]["right"]
        parent = child

    return step


def second_task(input_data: list):
    count = 0
    instructions = input_data[0]
    dict_graph = {}
    possible_goals = set()
    for i in range(2, len(input_data)):
        value = input_data[i]
        source, rest = value.split(" = ")
        rest = rest.strip("(")
        rest = rest.strip(")")
        left, right = rest.split(", ")
        if left[2] == "Z":
            possible_goals.add(left)
        if right[2] == "Z":
            possible_goals.add(right)

        dict_graph[source] = {"left": left, "right": right}

    parents = [source for source in dict_graph.keys() if source[2] == "A"]

    start_node_to_goal_steps = {k: [] for k in parents}

    possible_goals_to_start_nodes = {k: set() for k in possible_goals}

    start_nodes = parents

    childs = ["ZZZ"]
    step = 0
    while len([child for child in childs if child in []]) != len(parents):
        instruction = instructions[step % len(instructions)]
        step += 1

        childs = []
        for i, parent in enumerate(parents):
            if instruction == "L":
                child = dict_graph[parent]["left"]
            else:
                child = dict_graph[parent]["right"]
            childs.append(child)

            if child in possible_goals:
                start_node = start_nodes[i]
                start_node_to_goal_steps[start_node].append(step)
                possible_goals_to_start_nodes[child].add(start_node)

        parents = childs

        is_done = True
        for parent, goal in start_node_to_goal_steps.items():
            if len(goal) == 0:
                is_done = False
        if is_done:
            break

    goal_steps = list(map(lambda x: x[0], start_node_to_goal_steps.values()))
    return math.lcm(*goal_steps)


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
