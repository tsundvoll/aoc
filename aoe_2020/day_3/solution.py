data = [x for x in open('input.txt').read().splitlines()]


def parse_data(input_data):
    new_data = []
    for line in input_data:
        line_data = []
        for char in line:
            if char == '.':
                line_data.append(0)
            elif char == '#':
                line_data.append(1)
            else:
                raise ValueError("Invalid char")
        new_data.append(line_data)
    return new_data


def check_pos(input_data, r, d):
    width = len(input_data[0])
    return input_data[d][r%width]


def count_trees(input_data, right, down):
    height = len(input_data)
    r = 0
    d = 0
    counter = 0
    while (d < height):
        counter += check_pos(input_data, r, d)
        r += right
        d += down
    return counter


def solution_part_1():
    parsed_data = parse_data(data)
    return count_trees(parsed_data, 3, 1)


def solution_part_2():
    parsed_data = parse_data(data)
    a = count_trees(parsed_data, 1, 1)
    b = count_trees(parsed_data, 3, 1)
    c = count_trees(parsed_data, 5, 1)
    d = count_trees(parsed_data, 7, 1)
    e = count_trees(parsed_data, 1, 2)
    return a*b*c*d*e


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())
