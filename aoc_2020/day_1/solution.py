def expenses_2020(expenses):
    num_expenses = len(expenses)
    for i in range(num_expenses):
        for j in range(i, num_expenses):
            if expenses[i] + expenses[j] == 2020:
                return expenses[i] * expenses[j]


def expenses_three_2020(expenses):
    num_expenses = len(expenses)
    for i in range(num_expenses):
        for j in range(i, num_expenses):
            for k in range(j, num_expenses):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i] * expenses[j] * expenses[k]


def solution_part_1():
    return expenses_2020(data)


def solution_part_2():
    return expenses_three_2020(data)


if __name__ == "__main__":
    data = [int(x) for x in open('input.txt').read().splitlines()]
    print(data)
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())