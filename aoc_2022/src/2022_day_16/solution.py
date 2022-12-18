import math
import os
import time
from functools import lru_cache

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pyperclip
from tqdm import tqdm


def draf_graph(graph):
    pos = nx.spring_layout(graph, seed=225)  # Seed for reproducible layout
    nx.draw(graph, pos, with_labels=True)
    plt.show()


def first_task(input_data):
    count = 0
    G = nx.DiGraph()
    for i in range(len(input_data)):
        value = input_data[i].strip("Valve ")
        start_valve, rest = value.split(" has flow rate=")
        flow_rate, rest = rest.split("; tunnels lead to valves ")
        flow_rate = int(flow_rate)
        end_valves = rest.split(", ")

        start_valve_flow = start_valve + "_flow"

        for end_valve in end_valves:
            G.add_edge(start_valve, end_valve)
            G.add_edge(end_valve, start_valve)

            if flow_rate > 0:
                G.add_edge(start_valve, start_valve_flow)
                G.add_edge(start_valve_flow, end_valve, flow_rate=flow_rate)

        print(start_valve, flow_rate, end_valves)

    preassures = []
    global max_pressure_released
    max_pressure_released = 0

    @lru_cache()
    def visit_valve(valve, time_stamp, valves_opened, current_flow, preassure_released):
        global max_pressure_released
        neighbors = G.neighbors(valve)

        if time_stamp >= 30:
            if preassure_released > max_pressure_released:
                max_pressure_released = preassure_released
                print(f"New max pressure found: {max_pressure_released}")
            # preassures.append(preassure_released)
            return preassure_released

        preassures = []

        for neighbor in neighbors:
            try:
                flow_rate = G[valve][neighbor]["flow_rate"]
                if neighbor not in valves_opened:
                    preassures.append(
                        visit_valve(
                            neighbor,
                            time_stamp + 1,
                            tuple(valves_opened + (neighbor,)),
                            current_flow + flow_rate,
                            preassure_released + current_flow,
                        )
                    )

            except KeyError:
                pass

            preassures.append(
                visit_valve(
                    neighbor,
                    time_stamp + 1,
                    valves_opened,
                    current_flow,
                    preassure_released + current_flow,
                )
            )

        print(f"Returning local max pressure: {max(preassures)}")
        return max(preassures)

    start_valve = "AA"
    # visit_valve(
    #     valve=start_valve,
    #     time_stamp=0,
    #     valves_opened=tuple(),
    #     current_flow=0,
    #     preassure_released=0,
    # )

    paths = nx.dfs_edges(G, start_valve, depth_limit=30)
    print(paths)
    for path in paths:
        print(path)

    # draf_graph(G)
    return count


def second_task(input_data):
    count = 0
    for i in range(len(input_data)):
        value = input_data[i]
        pass
    return None


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
