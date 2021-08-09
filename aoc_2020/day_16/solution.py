data = [x for x in open('input.txt').read().splitlines()]




def invalid_values_on_nearby_tickets(input_data):
    category = 0
    ranges = []
    invalid_values = []
    for line in input_data:
        if line == "":
            continue
        if line == "your ticket:":
            category = 1
        elif line == "nearby tickets:":
            category = 2
        elif category == 0:
            rule, numbers = line.split(": ")
            first_range_str, second_range_str = numbers.split(" or ")
            first_range_start, first_range_end = first_range_str.split("-")
            second_range_start, second_range_end = second_range_str.split("-")
            ranges.append(range(int(first_range_start), int(first_range_end)+1))
            ranges.append(range(int(second_range_start), int(second_range_end)+1))
        elif category == 1:
            print("Your ticket doesn't count yet")
        elif category == 2:
            for n_str in line.split(","):
                n = int(n_str)
                is_valid = False
                for r in ranges:
                    if n in r:
                        is_valid = True
                if not is_valid:
                    invalid_values.append(n)

    return invalid_values


def find_field_values(input_data):
    category = 0
    ranges = []
    invalid_values = []
    valid_nearby_tickets = []
    your_ticket = []
    number_to_field = {}
    for line in input_data:
        if line == "":
            continue
        if line == "your ticket:":
            category = 1
        elif line == "nearby tickets:":
            category = 2
        elif category == 0:
            rule, numbers = line.split(": ")
            first_range_str, second_range_str = numbers.split(" or ")
            first_range_start, first_range_end = first_range_str.split("-")
            second_range_start, second_range_end = second_range_str.split("-")

            first_range = range(int(first_range_start), int(first_range_end)+1)
            second_range = range(int(second_range_start), int(second_range_end)+1)
            for n in first_range:
                if n in number_to_field:
                    number_to_field[n].append(rule)
                else:
                    number_to_field[n] = [rule]
            for n in second_range:
                if n in number_to_field:
                    number_to_field[n].append(rule)
                else:
                    number_to_field[n] = [rule]


            ranges.append(first_range)
            ranges.append(second_range)
        elif category == 1:
            your_ticket = list(map(int, line.split(",")))
        elif category == 2:
            is_all_valid = True
            for n_str in line.split(","):
                n = int(n_str)
                is_valid = False
                for r in ranges:
                    if n in r:
                        is_valid = True
                if not is_valid:
                    is_all_valid = False
                    invalid_values.append(n)
            if is_all_valid:
                valid_nearby_tickets.append(list(map(int, line.split(","))))


    # print(valid_nearby_tickets)
    # print(number_to_field)
    # for key, values in number_to_field.items():
    #     print(key, values)


    field_sets = []
    v_ticket = valid_nearby_tickets[0]
    for n in v_ticket:
        fields = set(number_to_field[n])
        field_sets.append(fields)
    

    for i in range(1,len(valid_nearby_tickets)):
        v_ticket = valid_nearby_tickets[i]
        for i, n in enumerate(v_ticket):
            fields = set(number_to_field[n])
            # print(fields)

            field_sets[i] = field_sets[i] & fields

    final_fields = ['' for _ in field_sets]

    has_changed = True
    i = 0
    while has_changed:
        has_changed = False
        for i in range(len(field_sets)):
            element = field_sets[i]
            if len(element) == 1:
                for element_to_remove in element:
                    final_fields[i] = element_to_remove
                    break
                for j in range(len(field_sets)):
                    field_sets[j].discard(element_to_remove)
                # map(lambda x: x.remove(element[0]), field_sets)
                has_changed = True

    print(final_fields)

    dictionary = {}
    for i in range(len(your_ticket)):
        your_value = your_ticket[i]
        your_field = final_fields[i]
        dictionary[your_field] = your_value
    return dictionary


def solution_part_1():
    invalid_values = invalid_values_on_nearby_tickets(data)
    return sum(invalid_values)


def solution_part_2():
    field_values = find_field_values(data)

    product = 1
    product = field_values["departure location"]* field_values["departure station"]* field_values["departure platform"]* field_values["departure track"]* field_values["departure date"]* field_values["departure time"]
    
    return product









if __name__ == "__main__":
    # print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())