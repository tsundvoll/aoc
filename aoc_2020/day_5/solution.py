data = [x for x in open('input.txt').read().splitlines()]


def get_row(seat):
    b_row = seat[0:7]
    binary_list = ['0' if x=='F' else '1' for x in b_row]
    binary_str = "".join(binary_list)
    integer = int(binary_str, 2)
    return integer


def get_col(seat):
    b_column = seat[7:]
    binary_list = ['0' if x=='L' else '1' for x in b_column]
    binary_str = "".join(binary_list)
    integer = int(binary_str, 2)
    return integer


def get_seat_id(row, column):
    return row*8+column


def solution_part_1():
    max_id = 0
    all_seats = []
    for seat in data:
        row = get_row(seat)
        col = get_col(seat)
        seat_id = get_seat_id(row, col)
        all_seats.append(seat_id)
        if seat_id > max_id:
            max_id = seat_id
    
    L = sorted(all_seats)
    start, end = L[0], L[-1]
    my_id = sorted(set(range(start, end + 1)).difference(L))[0]

    return max_id, my_id


def solution_part_2():
    return "Not solved yet"


if __name__ == "__main__":
    print("Answer Part 1: {0}\nAnswer Part 2: {1}".format(*solution_part_1()))
