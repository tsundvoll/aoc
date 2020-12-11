import numpy as np
from scipy import ndimage
import copy


def t(x):
        if x == '.':
            return -1
        elif x == "L":
            return 0
        elif x == "#":
            return 1


def parse_data(input_data):
    data = []
    for l in input_data:
        line = []
        for c in l:
            line.append(t(c))
        data.append(np.array(line))
    data = np.array(data)
    return data


data_lines = parse_data([x for x in open('input.txt').read().splitlines()])


def print_seats(seats, title = "", is_chars=True):

    print(title)
    if is_chars:
        for line in seats:
            for seat in line:
                if seat == -1:
                    print(".", end="")
                elif seat == 0:
                    print("L", end="")
                elif seat == 1:
                    print("#", end="")
            print()
    else:
        print(seats)
    print()


def neighbours(values):
    return values.sum()

def first_neighbour(values, direction='right'):
    if direction == 'right':
        array = values
    elif direction == 'left':
        array = np.flip(values)

    seat_pos = np.where(array == 1)[0]
    empty_seat_pos = np.where(array == 2)[0]

    # Seat
    if len(seat_pos) > 0:
        first_seat = seat_pos[0]
    else:
        return 0

    # Empty seat
    if len(empty_seat_pos) > 0:
        first_empty_seat = empty_seat_pos[0]
    else:
        return 1

    return first_seat < first_empty_seat


def apply_rules_1(input_data):
    neighbours_filter = np.array([
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ])

    seats_empty = (input_data == 0).astype(int)
    seats_floor = (input_data == -1).astype(int)
    seats_occupied = (input_data == 1).astype(int)

    seats_occupied_pad = np.pad(seats_occupied, [(1, 1), (1, 1)], mode='constant')

    # occupied_neighbours = ndimage.generic_filter(seats_occupied_pad, neighbours, footprint=neighbours_filter)[1:-1, 1:-1]
    occupied_neighbours = ndimage.generic_filter(seats_occupied, neighbours, footprint=neighbours_filter, mode="constant", cval=0)

    can_be_occupied_if_empty = (occupied_neighbours == 0).astype(int)
    can_be_emptied_if_occupied = (occupied_neighbours >= 4).astype(int)

    new_occupied = np.bitwise_and(seats_empty, can_be_occupied_if_empty)
    new_empty = np.bitwise_and(seats_occupied, can_be_emptied_if_occupied)
    
    result = input_data.copy()
    result[new_empty == 1] = 0
    result[new_occupied == 1] = 1
    result[seats_floor == 1] = -1
    
    return result


height = len(data_lines)
width = len(data_lines[0])
size = max(height, width)+1

f = np.array([
    [0,0,0],
    [1,0,0],
    [0,0,0]
])
f_pad = np.pad(f, [(size,size),(size,size)], mode="edge")
f_left = f_pad
f_left_down = ndimage.rotate(f_pad, angle=45, reshape=False, mode="nearest")
f_down = ndimage.rotate(f_pad, angle=90, reshape=False, mode="nearest")
f_right_down = ndimage.rotate(f_pad, angle=135, reshape=False, mode="nearest")
f_right = ndimage.rotate(f_pad, angle=180, reshape=False, mode="nearest")
f_right_up = ndimage.rotate(f_pad, angle=225, reshape=False, mode="nearest")
f_up = ndimage.rotate(f_pad, angle=270, reshape=False, mode="nearest")
f_left_up = ndimage.rotate(f_pad, angle=315, reshape=False, mode="nearest")


def apply_rules_2(input_data):
    result_1 = copy.deepcopy(input_data)
    result = copy.deepcopy(input_data)

    seats_empty = (input_data == 0).astype(int)
    seats_floor = (input_data == -1).astype(int)
    seats_occupied = (input_data == 1).astype(int)

    result_1[input_data == 0] = 2
    result_1[input_data == -1] = 0

    occupied_neighbours_left = ndimage.generic_filter(result_1, first_neighbour, footprint=f_left, mode="constant", cval=0, extra_keywords={'direction': 'left'})
    occupied_neighbours_left_down = ndimage.generic_filter(result_1, first_neighbour, footprint=f_left_down, mode="constant", cval=0, extra_keywords={'direction': 'right'})
    occupied_neighbours_down = ndimage.generic_filter(result_1, first_neighbour, footprint=f_down, mode="constant", cval=0, extra_keywords={'direction': 'right'})
    occupied_neighbours_right_down = ndimage.generic_filter(result_1, first_neighbour, footprint=f_right_down, mode="constant", cval=0, extra_keywords={'direction': 'right'})
    occupied_neighbours_right = ndimage.generic_filter(result_1, first_neighbour, footprint=f_right, mode="constant", cval=0, extra_keywords={'direction': 'right'})
    occupied_neighbours_right_up = ndimage.generic_filter(result_1, first_neighbour, footprint=f_right_up, mode="constant", cval=0, extra_keywords={'direction': 'left'})
    occupied_neighbours_up = ndimage.generic_filter(result_1, first_neighbour, footprint=f_up, mode="constant", cval=0, extra_keywords={'direction': 'left'})
    occupied_neighbours_left_up = ndimage.generic_filter(result_1, first_neighbour, footprint=f_left_up, mode="constant", cval=0, extra_keywords={'direction': 'left'})

    occupied_neighbours_all = (
        occupied_neighbours_left
        + occupied_neighbours_left_down
        + occupied_neighbours_down
        + occupied_neighbours_right_down
        + occupied_neighbours_right
        + occupied_neighbours_right_up
        + occupied_neighbours_up
        + occupied_neighbours_left_up
    )

    can_be_occupied_if_empty = (occupied_neighbours_all == 0).astype(int)
    can_be_emptied_if_occupied = (occupied_neighbours_all >= 5).astype(int)

    new_occupied = np.bitwise_and(seats_empty, can_be_occupied_if_empty)
    new_empty = np.bitwise_and(seats_occupied, can_be_emptied_if_occupied)
    
    # result = input_data.copy()
    result[new_empty == 1] = 0
    result[new_occupied == 1] = 1
    result[seats_floor == 1] = -1
    
    return result


def simulate_1(input_data):
    old_seats = input_data
    new_seats = apply_rules_1(old_seats)
    while (old_seats != new_seats).any():
        old_seats = new_seats
        new_seats = apply_rules_1(old_seats)
    return new_seats


def simulate_2(input_data):
    old_seats = input_data
    new_seats = apply_rules_2(old_seats)
    count = 0
    while (old_seats != new_seats).any():
        print(count)
        count += 1
        old_seats = new_seats
        new_seats = apply_rules_2(old_seats)
    return new_seats


def solution_part_1():
    new_seats = simulate_1(data_lines)
    occupied = len(new_seats[new_seats == 1])
    
    return occupied


def solution_part_2():
    new_seats = simulate_2(data_lines)
    occupied = len(new_seats[new_seats == 1])

    return occupied


if __name__ == "__main__":
    # print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())