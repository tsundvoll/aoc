import time



def parse(data):
    data_list = []
    allergens_register = {}
    for line_idx, line in enumerate(data):
        ingredients, allergens = line.split(" (contains ")
        ingredients_list = set(ingredients.split(" "))
        allergens_list = allergens[:-1].split(", ")
        # line_list = [ingredients_list, allergens_list]
        data_list.append(ingredients_list)
        for allergen in allergens_list:
            try:
                allergens_register[allergen].append(line_idx)
            except KeyError:
                allergens_register[allergen] = [line_idx]
    return data_list, allergens_register


def solution_part_1():
    data = [x for x in open('input.txt').read().splitlines()]
    return "Not solved yet"


def solution_part_2():
    return "Not solved yet"


if __name__ == "__main__":
    print("Part 1")
    tic = time.perf_counter()
    print("- answer:", solution_part_1())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")

    print("Part 2")
    tic = time.perf_counter()
    print("- answer:", solution_part_2())
    toc = time.perf_counter()
    print(f"- runtime: {toc - tic:0.4f} seconds")
