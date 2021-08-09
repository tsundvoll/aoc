from functools import lru_cache
import time
import itertools
import numpy as np


def parse(data):
    rules = {}
    messages = []
    rules_or_messages = 0 # 0=RULES, 1=MESSAGES
    for line in data:
        if line == "":
            rules_or_messages += 1
        elif rules_or_messages == 0:
            # print(line)
            rule_number, rule_list = line.split(": ")
            if rule_list == '"a"':
                rules[int(rule_number)] = 'a'
            elif rule_list == '"b"':
                rules[int(rule_number)] = 'b'
            else:
                sub_rules = rule_list.split(" | ")
                sub_rules_array = []
                for sub_rule in sub_rules:
                    sub_rule_array = [int(x) for x in sub_rule.split(" ")]
                    sub_rules_array.append(sub_rule_array)
                rules[int(rule_number)] = sub_rules_array
        elif rules_or_messages == 1:
            messages.append(line)
        else:
            raise ValueError

    return rules, messages


# rules, messages = parse([x for x in open('input.txt').read().splitlines()])
# rules, messages = parse([x for x in open('input_switched.txt').read().splitlines()])
# rules, messages = parse([x for x in open('test_2_switched.txt').read().splitlines()])
rules = None

def set_rules(new_rules):
    global rules
    rules = new_rules


def all_combinations(list_1, list_2):
    array_1 = np.array(list_1)
    array_2 = np.array(list_2)
    combinations = ["".join(comb) for comb in np.array(np.meshgrid(array_1, array_2)).T.reshape(-1, 2)]
    return combinations


def get_options(rule_number):
    options = []
    rule = rules[rule_number]
    if isinstance(rule, str):
        return rule

    for sub_rule in rule:
        possible_options = []
        for match_rule in sub_rule:
            sub_rule_options = get_options(match_rule)
            if isinstance(sub_rule_options, str):
                possible_options.append(sub_rule_options)
            else:
                possible_options.append(sub_rule_options)
        
        combinations = possible_options[0]
        for i in range(1, len(possible_options)):
            combine_with = possible_options[i]
            combinations = all_combinations(combinations, combine_with)
        options += combinations
    return options


def solution_part_1():
    options = get_options(0)
    count = 0
    for message in messages:
        if message in options:
            count += 1
    return count


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
