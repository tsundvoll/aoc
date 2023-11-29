import ast
import math
import operator
import os
import time

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pyperclip
from tqdm import tqdm


def draw_graph(graph):
    pos = nx.spring_layout(graph, seed=225)  # Seed for reproducible layout
    nx.draw(graph, pos, with_labels=True)
    plt.show()


def first_task(input_data, humn_value=None):
    G = nx.DiGraph()
    values = {}
    operations = {}
    for i in range(len(input_data)):
        value = input_data[i]
        var, rest = value.split(": ")
        if rest.isdigit():
            value = int(rest)
            if not humn_value is None and var == "humn":
                values[var] = humn_value
            else:
                values[var] = value
            G.add_edge(var, value)
        else:
            operand1, operator_str, operand2 = rest.split(" ")
            op = (
                operator.add
                if operator_str == "+"
                else operator.sub
                if operator_str == "-"
                else operator.mul
                if operator_str == "*"
                else operator.truediv
            )
            operations[var] = (operand1, op, operand2)
            G.add_edge(var, operand1)
            G.add_edge(var, operand2)

    # draw_graph(G)

    res = nx.bfs_tree(G, "root")
    go_order = list(reversed(list(res)))

    for go_ord in go_order:
        if isinstance(go_ord, int):
            continue
        if go_ord in values:
            continue

        operand1, op, operand2 = operations[go_ord]
        values[go_ord] = op(values[operand1], values[operand2])

    return int(values["root"])


"""
                    root
            |                   |
           pppw       +        sjmn
        //      \\          //      \\
      cczh  /  lfqf       drzm  *  dbpl
    //   \\     |       //    \\     |
  sllz + lgvd   4      hmdt - zczc   5
   |   //   \\          |      |
   4  ljgn * ptdq       32      2
       |    //  \\
       2  humn - dvpt
            |     |
            5     3


x - 3 = 298
x = 301


# hmdt: 32
# zczc: 2
# drzm: hmdt - zczc
# dbpl: 5
# lfqf: 4
# dvpt: 3
# humn: 5
# ptdq: humn - dvpt
# ljgn: 2
# lgvd: ljgn * ptdq
# sllz: 4
# cczh: sllz + lgvd
# sjmn: drzm * dbpl
# pppw: cczh / lfqf
# root: pppw + sjmn
"""


def second_task(input_data):
    from sympy import Symbol
    from sympy.solvers import solve

    humn = Symbol("humn")

    values = {}

    for i in range(len(input_data)):
        value = input_data[i]
        var, rest = value.split(": ")
        if var == "humn":
            continue
        elif var == "root":
            left_root, _, right_root = rest.split(" ")
        else:
            if rest.isdigit():
                value = int(rest)
                values[var] = value
            else:
                values[var] = Symbol(var)

    variables = {}
    for i in range(len(input_data)):
        value = input_data[i]
        var, rest = value.split(": ")
        if var != "humn" and var != "root" and not rest.isdigit():
            operand1, operator_str, operand2 = rest.split(" ")

            var_symbol = values[var]

            if operand1 in values.keys():
                op1 = values[operand1]
            else:
                op1 = Symbol(operand1)

            if operand2 in values.keys():
                op2 = values[operand2]
            else:
                op2 = Symbol(operand2)

            if operator_str == "+":
                variables[var] = solve(op1 + op2 - var_symbol, var_symbol)
            elif operator_str == "-":
                variables[var] = solve(op1 - op2 - var_symbol, var_symbol)
            elif operator_str == "*":
                variables[var] = solve(op1 * op2 - var_symbol, var_symbol)
            elif operator_str == "/":
                variables[var] = solve(op1 / op2 - var_symbol, var_symbol)

    print(left_root)

    left_root_symbol = Symbol(left_root)
    right_root_symbol = Symbol(right_root)

    left_root_result = solve(
        variables[left_root][0] - left_root_symbol, left_root_symbol
    )
    right_root_symbol = variables[right_root][0]

    print(left_root_symbol)

    equation = solve(variables[left_root][0] - variables[right_root][0], humn)

    print(equation)
    print(values)

    return equation


def second_task_old(input_data):
    """
    ((humn + 2) / (8 + 3)) * 4 == 253

    """
    G = nx.DiGraph()
    values = {0: 0}
    operations = {}
    for i in range(len(input_data)):
        value = input_data[i]
        var, rest = value.split(": ")
        if rest.isdigit():
            value = int(rest)
            if var == "humn":
                values[var] = None
            else:
                values[var] = value
            G.add_edge(var, value)
        elif var == "root":
            operand1, _, operand2 = rest.split(" ")
            G.add_edge("root", "root_a")
            G.add_edge("root", "root_b")
            operations["root"] = ("root_a", operator.add, "root_b")
            G.add_edge("root_a", operand1)
            G.add_edge("root_b", operand2)
            operations["root_a"] = (operand1, operator.add, 0)
            operations["root_b"] = (operand2, operator.add, 0)
        else:
            operand1, operator_str, operand2 = rest.split(" ")
            op = (
                operator.add
                if operator_str == "+"
                else operator.sub
                if operator_str == "-"
                else operator.mul
                if operator_str == "*"
                else operator.truediv
            )
            operations[var] = (operand1, op, operand2)
            G.add_edge(var, operand1)
            G.add_edge(var, operand2)

    # print(nx.has_path(G, "root_a", "humn"))
    # print(nx.has_path(G, "root_b", "humn"))

    def populate_values_from_node(node):
        vars = list(reversed(list(nx.bfs_tree(G, node))))
        for var in vars:
            if isinstance(var, int) or var in values:
                continue
            operand1, op, operand2 = operations[var]
            values[var] = op(values[operand1], values[operand2])

    populate_values_from_node("root_b")

    root_b = values["root_b"]
    """
            root_a
           /      |
         ccc      ddd
        /   |    /   |
       H     2  3     4

    """

    humn_value = root_b
    top_node = "root_a"

    while top_node != "humn":
        print("\nTop_node:", top_node)
        print("Other side is", humn_value)
        try:
            left, right = G.successors(top_node)
        except ValueError:
            (oposing_operand,) = G.successors(top_node)
            if isinstance(oposing_operand, str):
                top_node = oposing_operand
                continue
        else:
            print(f"Left: {left}, right: {right}")
            if nx.has_path(G, left, "humn"):
                populate_values_from_node(right)
                oposing_operand = values[right]
                print("Opposing operand right:", oposing_operand)
                next_top_node = left
            elif nx.has_path(G, right, "humn"):
                populate_values_from_node(left)
                oposing_operand = values[left]
                print("Opposing operand left:", oposing_operand)
                next_top_node = right
            else:
                raise RuntimeError

        _, op, _ = operations[top_node]
        if op == operator.add:
            humn_value -= oposing_operand
        elif op == operator.sub:
            humn_value += oposing_operand
        elif op == operator.mul:
            humn_value /= oposing_operand
        elif op == operator.truediv:
            humn_value *= oposing_operand
        else:
            raise RuntimeError

        top_node = next_top_node

    values["humn"] = humn_value
    populate_values_from_node("root_a")
    # populate_values_from_node("root")

    root_value = first_task(input_data=input_data, humn_value=humn_value)
    print(root_value)
    print(values["root_a"])
    print(values["root_b"])
    print(humn_value)

    # assert root_value == int(values["root_a"]) + int(values["root_b"])
    assert values["root_a"] == values["root_b"]

    return humn_value


# x / -2 = 10
# -x / 2 = 10
# -x = 20
# x = -20

# 11049074315969.875 is wrong
# 11049074315968 is too high


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
