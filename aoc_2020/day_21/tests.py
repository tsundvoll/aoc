from solution import *
import pytest



def test_part_1():
    ingredients_list, allergens_and_lines = parse([x for x in open('input.txt').read().splitlines()])
    print(f"{ingredients_list=}")
    print(f"{allergens_and_lines=}")

    common_ingredients_dict = {}

    for allergens, line_idxs in allergens_and_lines.items():
        idxs = line_idxs[0]
        common_ingredients = ingredients_list[idxs]
        for i in range(1, len(line_idxs)):
            idx = line_idxs[i]
            common_ingredients = common_ingredients.intersection(ingredients_list[idx])

        common_ingredients_dict[allergens] = common_ingredients

    known_allergens = {}
    print(f"{common_ingredients_dict=}")

    safe_ingredients = set()

    for ingr in ingredients_list:
        for ingredient in ingr:
            safe_ingredients.add(ingredient)
    print(f"{safe_ingredients=}")

    for _ in range(4):
        for allergen, ingredients in common_ingredients_dict.items():
            if len(ingredients) == 1:
                found_ingredient = ingredients.pop()
                ingredients.add(found_ingredient)
                known_allergens[allergen] = found_ingredient

                print(f"{common_ingredients_dict=}")
                for key in common_ingredients_dict.keys():
                    try:
                        common_ingredients_dict[key].remove(found_ingredient)
                    except KeyError:
                        continue

    print(f"{common_ingredients_dict=}")
    print(f"{known_allergens=}")

    for value in known_allergens.values():
        safe_ingredients.remove(value)
    print("Remaining ingredients:", safe_ingredients)

    count_safe = 0
    for ingr in ingredients_list:
        for ingredient in ingr:
            if ingredient in safe_ingredients:
                count_safe += 1
            
    print(count_safe)
    assert count_safe == 5


@pytest.mark.skip("Not implemented yet")
def test_part_2():
    raise NotImplementedError


if __name__ == "__main__":
    tic = time.perf_counter()
    test_part_1()
    toc = time.perf_counter()
    print(f"Ran first tests in {toc - tic:0.4f} seconds\n")
    

    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran second tests in {toc - tic:0.4f} seconds")