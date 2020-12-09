input_data = [int(x) for x in open('input.txt').read().splitlines()]


def is_two_sum(array, number):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if (i != j) and (array[i] + array[j] == number):
                return True
    return False


def first_invalid(data, preamble_length):
    numbers = data[preamble_length:]

    for i, num in enumerate(numbers):
        preamble = data[i:i+preamble_length]
        if not is_two_sum(preamble, num):
            return num


def find_contiguous_set(data, preamble_length):
    f = first_invalid(data, preamble_length)
    for start in range(0,len(data)):
        for end in range(len(data), 0, -1):
            if start == end:
                break
            window = data[start:end]
            s = sum(window)
            if s == f:
                return window


def solution_part_1():
    return first_invalid(input_data, 25)


def solution_part_2():
    result = find_contiguous_set(data=input_data, preamble_length=25)
    s_result = sorted(result)

    return s_result[0] + s_result[-1]


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())