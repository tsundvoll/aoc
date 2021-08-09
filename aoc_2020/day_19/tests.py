from solution import *
from solution import get_options
import pytest

rules, messages = parse([x for x in open('test.txt').read().splitlines()])
rules_2, messages_2 = parse([x for x in open('test_2.txt').read().splitlines()])
rules_2_switched, messages_2_switched = parse([x for x in open('test_2_switched.txt').read().splitlines()])

rules_input_switched, messages_input_switched = parse([x for x in open('input_switched.txt').read().splitlines()])

@pytest.mark.skip()
def test_part_1():
    print(f"{rules=}")
    print(f"{messages=}")

    list_1 = ['aa', 'bb']
    list_2 = ['ab', 'ba']

    assert set(all_combinations(list_1, list_2)) == {'aaab', 'aaba', 'bbab', 'bbba'}

    # set_rules(rules)

    assert get_options(3) == ['ab', 'ba']
    assert get_options(2) == ['aa', 'bb']
    assert get_options(1) == ['aaab', 'aaba', 'bbab', 'bbba', 'abaa', 'abbb', 'baaa', 'babb']
    assert set(get_options(0)) == {'aaaabb', 'aaabab', 'abbabb', 'abbbab', 'aabaab', 'aabbbb', 'abaaab', 'ababbb'}


    options = get_options(0)
    count = 0
    for message in messages:
        if message in options:
            count += 1
    assert count == 2



def test_part_2():
    set_rules(rules_input_switched)
    # set_rules(rules_2_switched)

    rule_42 = get_options(42)
    rule_31 = get_options(31)

    print(f"{rule_42=}")
    print(f"{rule_31=}")

    step = len(rule_42[0])
    print(f"{step=}")

    count = 0
    for message in messages_input_switched:
    # for message in messages_2_switched:
        i = 0
        is_valid_message = True
        n_steps = len(message)/step
        n_first_steps = (n_steps // 2) +1
        # print(f"{n_steps=} and {n_first_steps=}")
        is_on_42s = True
        while i < len(message):
            message_slice = message[i:i+step]
            if i < step*n_first_steps: # First 2 must be in 42
                # print("Start:", message_slice)
                if not (message_slice in rule_42):
                    is_valid_message = False
                    break
            elif i > len(message)-step-1:  # Must be in 31
                # print("End:", message_slice)
                if not (message_slice in rule_31):
                    is_valid_message = False
                    break
            else: # Must be in 42 or 31
                if message_slice in rule_31:
                    is_on_42s = False

                if (is_on_42s and not (message_slice in rule_42)):
                    is_valid_message = False
                    break
                elif (not is_on_42s and not (message_slice in rule_31)):
                    is_valid_message = False
                    break
                elif not (message_slice in rule_31 or message_slice in rule_42):
                    is_valid_message = False
                    break
            i += step
        if is_valid_message:
            count += 1
        # break
    print(count)
    assert count == 12




    # 0: 8 11
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31

    # 12

"""
42 42 31
42 42 42 31
42 42 42 42 31
42 42 42 31 31
42 42 42 31 31


"""




    # 42 42 31
    # 42 42 42 31
    #
    # 42 42 42 31 31


    # rule_0 = all_combinations(rule_8, rule_11)

    # count = 0
    # for message in messages_2:
    #     if message in rule_0:
    #         count += 1
    # assert count == 12

    # rule_8 = rule_42.copy()
    # rule_11 = all_combinations(rule_42, rule_31)
    # print(f"{len(rule_8[0])=}")
    # print(f"{len(rule_11[0])=}")


    # rule_8 = all_combinations(rule_8, rule_42)
    # rule_11 = all_combinations(all_combinations(rule_42, rule_11), rule_31)
    # print(f"{len(rule_8[0])=}")
    # print(f"{len(rule_11[0])=}")

    
    # rule_8 = all_combinations(rule_8, rule_42)
    # rule_11 = all_combinations(all_combinations(rule_42, rule_11), rule_31)
    # print(f"{len(rule_8[0])=}")
    # print(f"{len(rule_11[0])=}")

    # rule_42=['babbb', 'baabb', 'bbaab', 'bbabb', 'bbbab', 'bbbbb', 'abbbb', 'aabbb', 'aaaab', 'aaabb', 'aaaba', 'ababa', 'bbbba', 'aaaaa', 'baaaa', 'bbaaa']
    # rule_31=['bbaba', 'bbbaa', 'babab', 'babaa', 'babba', 'baaba', 'baaab', 'ababb', 'abaab', 'abbab', 'abaaa', 'abbaa', 'abbba', 'aabab', 'aabaa', 'aabba']

    # 0: 8 11 (#12)
    # 8: 42 (#4) | 42 8 (#8)
    # 11: 42 31 (#8) | 42 11 31 (#16)
    # 96: 6*11 or 24*8

    # 42 (42 31)

    # (42 8) (42 31)
    # (42 42) (42 31)

    # 42 (42 11 31)
    # 42 (42 (42 31) 31)


    # set_rules(rules_2_switched)

    # options = get_options(0)
    # count = 0
    # for message in messages_2_switched:
    #     if message in options:
    #         count += 1
    # assert count == 8



if __name__ == "__main__":
    # tic = time.perf_counter()
    # test_part_1()
    # toc = time.perf_counter()
    # print(f"Ran first tests in {toc - tic:0.4f} seconds")
    

    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran second tests in {toc - tic:0.4f} seconds")