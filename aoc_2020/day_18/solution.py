import time
import ast
from astor.source_repr import add_parens
import astunparse
import astor

# from functools import reduce
# from itertools import groupby, takewhile, repeat, count, dropwhile, filterfalse
# from scipy import ndimage
# import math
# import networkx as nx
# import numpy as np
# import operator
# import re


def parse(data):
    """Initial parsing of the input data"""
    return data


input_data = parse([x for x in open('input.txt').read().splitlines()])


#############
# Functions #
#############

# class ChangePrecedenceOrder(ast.NodeVisitor):
#     def __init__(self):
#         self.result = 0
#         self.res_string = ""

#     def get_string(self):
#         return self.res_string

#     def visit_Constant(self, node):
#         self.res_string += str(node.value)
#         print(node.value)
#         node = self.generic_visit(node)

#     def visit_BinOp(self, node):
#         self.res_string += ('(')
#         self.generic_visit(node)
#         self.res_string += (')')
#         # self.visit(node.op)
#         # self.visit(node.right)
    
#     def visit_Add(self, node):
#         self.res_string += "+"
#         node = self.generic_visit(node)

#     def visit_Mult(self, node):
#         self.res_string += "*"
#         node = self.generic_visit(node)


class Add2Mult(ast.NodeVisitor):
    def __init__(self):
        self.result = 0
        self.res_string = ""

    def get_string(self):
        return self.res_string

    def visit_Constant(self, node):
        self.res_string += str(node.value)
        node = self.generic_visit(node)

    def visit_BinOp(self, node):
        self.generic_visit(node)
    
    def visit_Add(self, node):
        self.res_string += "*"
        node = self.generic_visit(node)

    def visit_Mult(self, node):
        self.res_string += "+"
        node = self.generic_visit(node)


class ChangeOperand(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            new_node = ast.BinOp(left=node.left, op=ast.Mult, right=node.right)
            ast.copy_location(new_node, node)
            ast.fix_missing_locations(new_node)
            return node
        # elif isinstance(node.op, ast.Mult):    
        #     new_node = ast.BinOp(left=node.left, op=ast.Mult, right=node.right)
        #     ast.copy_location(new_node, node)
        #     ast.fix_missing_locations(new_node)
        #     return new_node
        return node

    # tree = ast.parse(line)
    # expr = tree.body[0]
    # CPO = Add2Mult()
    # CPO.visit(expr)
    # new_string = CPO.get_string()
    # new_expr = ast.parse(new_string).body[0]
    # print(astor.to_source(new_expr))

    # newest_expr = ChangeOperand().visit(new_expr)
    # print(astor.to_source(newest_expr))


def calc_line(line):
    i = 0
    total = None
    operator = '+'
    while i < len(line):
        c = line[i]
        if c.isdigit():
            operand = int(c)
            if i == 0:
                total = operand
            elif operator == '+':
                total += operand
            elif operator == '*':
                total *= operand
            i += 1
        elif c == '(':
            step, operand = calc_line(line[i+1:])
            i += step+1
            if total is None:
                total = operand
            elif operator == '+':
                total += operand
            elif operator == '*':
                total *= operand
        elif c == ')':
            return i+1, total
        elif c == '+':
            operator = '+'
            i += 1
        elif c == '*':
            operator = '*'
            i += 1
        else:
            i += 1
    return i+1, total


def calc_lines(data):
    answers = []
    for line in data:
        _, res = calc_line(line)
        answers.append(res)
    return answers



class MyNum():
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyNum(self.value * other.value)

    def __mul__(self, other):
        return MyNum(self.value + other.value)

    def __repr__(self):
        return f"MyNum({self.value})"
    


def calc_line_advanced(line):

    add_to_mult = []
    for c in line:
        if c == '+':
            add_to_mult.append('*')
        elif c == '*':
            add_to_mult.append('+')
        elif c.isdigit():
            add_to_mult.append(str(MyNum(int(c))))
        else:
            add_to_mult.append(c)
        
    add_to_mult = "".join(add_to_mult)
    result = eval(add_to_mult)

    return result.value


def calc_lines_advanced(data):
    answers = []
    for line in data:
        res = calc_line_advanced(line)
        answers.append(res)
    return answers


#####################
# Run the solutions #
#####################

def solution_part_1():
    lines_answers = calc_lines(input_data)
    return sum(lines_answers)


def solution_part_2():
    lines_answers = calc_lines_advanced(input_data)
    return sum(lines_answers)


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
