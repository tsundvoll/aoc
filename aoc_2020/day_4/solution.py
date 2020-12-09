import re

data = [x for x in open('input.txt').read().splitlines()]

"""
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
"""

mand_keys = [
    'byr',
    'ecl',
    'eyr',
    'hcl',
    'hgt',
    'iyr',
    'pid'
]
optional_keys = [
    'cid'
]
all_keys = [
    'byr',
    'cid',
    'ecl',
    'eyr',
    'hcl',
    'hgt',
    'iyr',
    'pid',
]

def parse_data(data):
    new_data = []
    tmp = {}
    count = 0
    for element in data:
        if element == '':
            new_data.append(tmp)
            if set(tmp.keys()) == set(all_keys) or set(tmp.keys()) == set(mand_keys):
                count += 1
            tmp = {}
        else:
            inner_elements = element.split(' ')
            for i_e in inner_elements:
                key, val = i_e.split(':')
                tmp[key] = val
    new_data.append(tmp)
    return new_data


def is_valid(line):
    for key, value in line.items():
        if key == 'byr':
            if not value.isdigit() or len(value) != 4 or int(value) < 1920 or int(value) > 2002:
                return False
        if key == 'iyr':
            if not value.isdigit() or len(value) != 4 or int(value) < 2010 or int(value) > 2020:
                return False
        if key == 'eyr':
            if not value.isdigit() or len(value) != 4 or int(value) < 2020 or int(value) > 2030:
                return False
        if key == 'hgt':
            tail = value.lstrip('0123456789')
            head = int("".join([str(i) for i in value if i.isdigit()]))
            if not (tail == 'cm' and (head >= 150 and head <= 193)) and not (tail == 'in' and (head >= 59 and head <= 76)):
                return False
        if key == 'hcl':
            if value[0] != '#':
                return False

            res = value[1:]
            if len(res) != 6:
                return False
            
            for char in res:
                if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    return False
        if key == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if key == 'pid':
            if not value.isdigit() or len(value) != 9:
                return False
    return True


def count_valid_passports(input_data, task):
    count = 0
    for line in input_data:
        keys = line.keys()
        if set(keys) == set(all_keys) or set(keys) == set(mand_keys):
            if task == 1:
                count += 1
            if task == 2:
                if is_valid(line):
                    count += 1
    return count

def solution_part_1():
    pd = parse_data(data)
    return count_valid_passports(pd, 1)


def solution_part_2():
    pd = parse_data(data)
    return count_valid_passports(pd, 2)


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())