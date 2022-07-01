import collections
import math
import os
import time

import numpy as np
import pyperclip
# from collections import namedtuple, Sequence
from tqdm import tqdm
from utility import parse
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt




class Pair:
    def __init__(self, left, right, depth):
        self.left
        self.right
        self.depth


# def print_number(number):
#     if isinstance(number, Sequence):
#         left, right = number
#         print(print_number(left), print_number(right))
#     else:
#         print(number)
       

def first_task(input):
    count = 0
    snail_sum = eval(input[0])

    for i, snail_number in enumerate(input[1:]):
        new = [snail_sum, eval(snail_number)]

        lst = str(new)
        print(lst)

        depth = 0
        for i, c in enumerate(lst):
            if c == '[':
                depth += 1
            if c == ']':
                depth -= 1
            
            if c == ',' and depth > 4:
                left_value = lst[:i].split('[')[-1]
                right_value = lst[i+2:].split(']')[0]

                len_left_value = len(left_value)
                len_right_value = len(right_value)

                for r in range(i+2+len_right_value, len(lst)):
                    if lst[r].isdigit():
                        new_num = str(int(lst[r]) + int(left_value))
                        lst = lst[:r] + new_num + lst[r+len_right_value:]
                        break
                print()
                print('lst:', lst)
                print()

                for l in range(i-1-len_left_value, 0, -1):
                    print(lst[l], end=' ')
                break


    return count


def second_task(input):
    return None


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    print('#############################')
    print('The answer to the 1st task is')
    print(first_answer, f'in {first_time} seconds')

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print('The answer to the 2nd task is')
    print(second_answer, f'in {second_time} seconds')
    print('#############################')


if __name__ == '__main__':
    run_day()



"""
Notes from walkthrough


Visualization: Åsmund Rognerud Birkeland
Highest climb since start: Julius Parulek
Highest climb since last year: Anna Kvashchuk
Best newcomer: Maia Haugen Tømmerbakk




Huskeliste:
Føre timer
Føre middagsrefusjon for 20. desember
Sende melding til Andreas



Hei Andreas,
Jeg har fått med meg at dette er siste måneden din i Equinor.

Lykke til videre i den nye jobben!

Jeg vil også benytte anledningen til å takke deg for måten jeg ble tatt imot på når
jeg begynte i fjor høst.

Håper vi får jobbe sammen en gang igjen i fremtiden.

God jul og godt nytt år!

"""




