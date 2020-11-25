def read_input():
    with open("input.txt", 'r') as f:
        data = f.readlines()
    return data


def calc_fuel_module(mass):
    return (mass // 3 - 2)


def calc_fuel_extended(mass):
    fuel = calc_fuel_module(mass)
    sum_fuel = 0
    while fuel > 0:
        sum_fuel += fuel
        fuel = calc_fuel_module(fuel)
    return sum_fuel


def solution_part_1():
    data = read_input()
    sum_fuel = 0
    for mass in data:
        sum_fuel += calc_fuel_module(int(mass))
    return sum_fuel


def solution_part_2():
    data = read_input()
    sum_fuel = 0
    for mass in data:
        sum_fuel += calc_fuel_extended(int(mass))
    return sum_fuel


print("Answer Part 1:", solution_part_1())
print("Answer Part 2:", solution_part_2())