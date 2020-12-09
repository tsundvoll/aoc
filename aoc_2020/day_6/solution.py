data = [x for x in open('input.txt').read().splitlines()]


def parse_data(data):
    new_data = []
    tmp = []
    count = 0
    for element in data:
        if element == '':
            new_data.append(tmp)
            tmp = []
        else:
            tmp.append(set(list(element)))
    new_data.append(tmp)
    return new_data


def sum_of_answers(input_data):
    pd = parse_data(input_data)
    count = 0
    for group in pd:
        q_yes = set()
        for person in group:
            q_yes.update(person)
        count += len(q_yes)
    return count


def sum_of_all_yes_answers(input_data):
    pd = parse_data(input_data)
    count = 0
    for group in pd:
        common = group[0]
        for person in group:
            common = set(common).intersection(person)
        count += len(common)
    return count


def solution_part_1():
    return sum_of_answers(data)


def solution_part_2():
    return sum_of_all_yes_answers(data)



if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())