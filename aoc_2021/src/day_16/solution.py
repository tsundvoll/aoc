import math
import os
import time

import numpy as np
import pyperclip
from utility import parse

debug = ''
count = 0

def first_task(input):
    global debug
    global count
    debug = ''
    count = 0

    packet = ''
    for i, c in enumerate(input):
        byte = bin(int(c, 16))[2:].zfill(4)
        packet += str(byte)
    packet = packet.strip()


    def parse_sub_package(start_i = 0, total_length = None, only_one_sub_packet = False):
        global debug
        global count
        i = start_i
        if not total_length is None:
            stop_at_i = start_i + total_length
        else:
            stop_at_i = len(packet)

        while i < stop_at_i:
            version = int(packet[i:i+3], 2)
            i += 3
            debug += 'V'*3

            if version == 0 and i > len(packet) - 6:
                raise StopIteration
            count += version

            type_id = int(packet[i:i+3], 2)
            i += 3
            debug += 'T'*3

            if type_id == 4:
                # Litteral
                n = 0
                group = packet[i:i+5]
                while int(group[0]) != 0:
                    i += 5
                    debug += chr(ord('A') + n)*5
                    n += 1

                    group = packet[i:i+5]

                i += 5
                debug += chr(ord('A') + n)*5

            else:
                # Operator
                length_type_id = int(packet[i:i+1], 2)
                i += 1
                debug += 'I'

                if length_type_id == 0:
                    total_length_in_bits = int(packet[i:i+15])
                    i += 15
                    debug += 'L'*15

                    end_id = parse_sub_package(
                        start_i=i,
                        total_length=total_length_in_bits,
                    )
                    i = end_id

                elif length_type_id == 1:
                    number_of_sub_packets = packet[i:11]
                    i += 11
                    debug += 'L'*11

                    for _ in number_of_sub_packets:
                        end_id = parse_sub_package(
                            start_i=i,
                            only_one_sub_packet=True,
                        )
                        i = end_id
                else:
                    raise ValueError(length_type_id)

            if only_one_sub_packet:
                return i
        return i

    try:
        parse_sub_package()
    except StopIteration:
        pass

    return count

def get_bits(packet, i, n_bits, debug_char):
    global debug

    data = int(packet[i:i+n_bits], 2)
    debug += debug_char*n_bits

    return data, i + n_bits

def second_task(input):
    global debug
    debug = ''

    packet = ''
    for i, c in enumerate(input):
        byte = bin(int(c, 16))[2:].zfill(4)
        packet += str(byte)
    packet = packet.strip()

    def parse_sub_package(start_i = 0, total_length = None, only_one_sub_packet = False):
        global debug
        global count
        i = start_i
        if not total_length is None:
            stop_at_i = start_i + total_length
        else:
            stop_at_i = len(packet)

        result = []

        while i < stop_at_i:
            version, i = get_bits(packet, i, 3, 'V')

            if version == 0 and i > len(packet) - 7:
                i -= 3
                debug = debug[:-3]
                return i, result

            type_id, i = get_bits(packet, i, 3, 'T')

            if type_id == 4:
                # Literal
                n = 0
                group = packet[i:i+5]
                literal = group[1:]
                while int(group[0]) != 0:
                    i += 5
                    debug += chr(ord('A') + n)*5
                    n += 1

                    group = packet[i:i+5]
                    literal += group[1:]

                i += 5
                debug += chr(ord('A') + n)*5
                literal = int(literal, 2)
                result.append(literal)
            else:
                # Operator
                length_type_id, i = get_bits(packet, i, 1, 'I')

                if length_type_id == 0:
                    total_length_in_bits, i = get_bits(packet, i, 15, 'L')

                    ii = i
                    end_id, r = parse_sub_package(
                        start_i=i,
                        total_length=total_length_in_bits,
                    )
                    i = end_id

                else:
                    assert length_type_id == 1
                    number_of_sub_packets, i = get_bits(packet, i, 11, 'L')
                    r = []
                    ii = i
                    for _ in range(number_of_sub_packets):
                        end_id, res = parse_sub_package(
                            start_i=i,
                            only_one_sub_packet=True,
                        )
                        i = end_id
                        r.extend(res)

                if type_id == 0:
                    op = 'Sum'
                    p = sum(r)
                elif type_id == 1:
                    op = 'Prod'
                    p = np.product(r)
                elif type_id == 2:
                    op = 'Min'
                    p = np.min(r)
                elif type_id == 3:
                    op = 'Max'
                    p = np.max(r)
                elif type_id == 5:
                    op = 'Greater then'
                    assert len(r) == 2
                    p = 1 if r[0] > r[1] else 0
                elif type_id == 6:
                    op = 'Smaller then'
                    assert len(r) == 2
                    p = 1 if r[0] < r[1] else 0
                elif type_id == 7:
                    op = 'Equal to'
                    assert len(r) == 2
                    p = 1 if r[0] == r[1] else 0
                result.append(p)

            if only_one_sub_packet:
                return i, result

        return i, result

    i, r = parse_sub_package()
    return r[0]


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse.parse_lines(input_file)[0]

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
