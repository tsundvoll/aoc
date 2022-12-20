import os
import time
from typing import List

import pyperclip
from tqdm import tqdm


class Number:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def move_forward(self, n):
        # a = self
        # [a_prev, a, b, b_next] - > [a_prev, b, a, b_next]
        for _ in range(n):
            a_prev = self.prev
            a = self
            b = self.next
            b_next = self.next.next

            a_prev.prev = a_prev.prev  # Unchanged
            a_prev.next = b

            a.prev = b
            a.next = b_next

            b.prev = a_prev
            b.next = a

            b_next.prev = a
            b_next.next = b_next.next  # Unchanged

    def move_backward(self, n):
        # b = self
        # [a_prev, a, b, b_next] - > [a_prev, b, a, b_next]
        for _ in range(n):
            a_prev = self.prev.prev
            a = self.prev
            b = self
            b_next = self.next

            a_prev.prev = a_prev.prev  # Unchanged
            a_prev.next = b

            a.prev = b
            a.next = b_next

            b.prev = a_prev
            b.next = a

            b_next.prev = a
            b_next.next = b_next.next  # Unchanged

    def get_next_number(self, n=1):
        next_number = self.next
        next_value = None
        for _ in range(n):
            next_value = next_number.value
            next_number = next_number.next
        return next_value

    def yield_numbers(self):
        yield self.value
        yield from self.next.yield_numbers()

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, self):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            raise ValueError(f"Invalid comparisson <Number> == {type(other)}")


def first_task(input_data):
    numbers = list(map(int, input_data))
    n_numbers = len(numbers)
    list_of_numbers: List(Number) = []
    for i in range(n_numbers):
        n = numbers[i]
        number = Number(value=n)
        list_of_numbers.append(number)

    for i in range(n_numbers - 1):
        list_of_numbers[i].next = list_of_numbers[i + 1]
        list_of_numbers[i + 1].prev = list_of_numbers[i]

    list_of_numbers[0].prev = list_of_numbers[-1]
    list_of_numbers[-1].next = list_of_numbers[0]

    zero_number = None
    for i in tqdm(range(len(list_of_numbers))):
        number = list_of_numbers[i]
        if number.value > 0:
            number.move_forward(number.value)
        elif number.value < 0:
            number.move_backward(abs(number.value))
        else:  # Found the zero index
            zero_number = number

    number = zero_number
    sum_of_numbers = 0
    # Look for the three coordinates
    for i in tqdm(range(3001)):
        if i in [1000, 2000, 3000]:
            print(i, number.value)
            sum_of_numbers += number.value
        number = number.next

    return sum_of_numbers


def print_list_of_numbers(start, length):
    number = start
    for i in tqdm(range(length)):
        print(number.value, end=", ")
        number = number.next
    print()


def second_task(input_data):
    DECRYPTION_KEY = 811589153
    numbers = list(map(int, input_data))
    n_numbers = len(numbers)
    list_of_numbers: List(Number) = []
    for i in range(n_numbers):
        n = numbers[i] * DECRYPTION_KEY
        number = Number(value=n)
        list_of_numbers.append(number)

    for i in range(n_numbers - 1):
        list_of_numbers[i].next = list_of_numbers[i + 1]
        list_of_numbers[i + 1].prev = list_of_numbers[i]

    list_of_numbers[0].prev = list_of_numbers[-1]
    list_of_numbers[-1].next = list_of_numbers[0]

    for _ in tqdm(range(10)):
        zero_number = None
        for i in tqdm(range(len(list_of_numbers))):
            number = list_of_numbers[i]

            len_to_move = abs(number.value) % (len(list_of_numbers) - 1)
            if number.value > 0:
                number.move_forward(len_to_move)
            elif number.value < 0:
                number.move_backward(len_to_move)
            else:  # Found the zero index
                zero_number = number

        # print_list_of_numbers(zero_number, len(list_of_numbers))

    number = zero_number
    sum_of_numbers = 0
    # Look for the three coordinates
    for i in tqdm(range(3001)):
        if i in [1000, 2000, 3000]:
            print(i, number.value)
            sum_of_numbers += number.value
        number = number.next

    return sum_of_numbers


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
