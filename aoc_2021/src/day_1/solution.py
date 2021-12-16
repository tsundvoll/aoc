import os

from utility.parse import parse_characters_on_a_line, parse_input, parse_lines


def first_task(input):
    count = 0
    for i, line in enumerate(input):
        if i == 0:
            prev = input[0]
        else:
            if input[i] > prev:
                count += 1
            prev = input[i]

    return count


def second_task(input):
    count = -1
    prev = 0
    for i, line in enumerate(input):
        if i == len(input)-1 or i == len(input)-2:
            continue
        else:
            A = input[i] + input[i+1] + input[i+2]
            if A > prev:
                count += 1
            prev = A 

    return count



def run_day():
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    input_data = parse_lines(input_file, data_type=int)

    print('#############################')
    print('The answer to the 1st task is')
    print(first_task(input_data))

    print()
    print('The answer to the 2nd task is')
    print(second_task(input_data))
    print('#############################')


if __name__ == '__main__':
    run_day()
