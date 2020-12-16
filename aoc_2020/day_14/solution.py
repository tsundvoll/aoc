data = [x for x in open('input.txt').read().splitlines()]


def apply_mask(value, mask):
    if mask == "X":
        return value
    if mask == "0":
        return "0"
    if mask == "1":
        return "1"


def read_program(input_data):
    memory = {}

    for line in input_data:
        command, value = line.split(' = ')
        if command[:3] == "mas":
            current_mask = value            
            # print(f"New mask: {current_mask}")
        elif command[:3] == "mem":
            memory_address = command[4:-1]
            new_value = int(value)

            b_value = bin(new_value).split('b')[1].zfill(36)

            # print(f"Binary: {b_value}")
            # print(f"Mask  : {current_mask}")
            
            res_str = "".join(map(apply_mask, b_value, current_mask))
            # print(f"Result: {int(res_str)}")

            int_res = int(res_str, 2)
            # print(f"Int result: {int_res}")
            # print()

            memory[memory_address] = int_res

    total = sum(memory.values())
    return total


def apply_new_mask(value, mask):
    if mask == "0":
        return value
    if mask == "1":
        return "1"
    if mask == "X":
        return "X"


def find_permutations(masked_address):
    s = masked_address
    positions = [pos for pos, char in enumerate(s) if char == "X"]
    n_positions = len(positions)
    combinations = [bin(x).split('b')[1].zfill(n_positions) for x in range(2**n_positions)]

    permutations = []
    for comb in combinations:
        permutation = list(masked_address)
        for i, pos in enumerate(positions):
            c = comb[i]
            permutation[pos] = comb[i]
        permutations.append("".join(permutation))

    return permutations

def read_program_floating(input_data):
    memory = {}

    for line in input_data:
        command, value = line.split(' = ')
        if command[:3] == "mas":
            current_mask = value            
            # print(f"New mask: {current_mask}")
        elif command[:3] == "mem":
            memory_address = int(command[4:-1])
            new_value = int(value)
            print(f"new_value: {new_value}")

            b_memory_address = bin(memory_address).split('b')[1].zfill(36)
            print(f"Addr: {b_memory_address}")
            print(f"Mask: {current_mask}")

            
            masked_address = "".join(map(apply_new_mask, b_memory_address, current_mask))
            print(f"m_ad: {masked_address}")

            permutations = find_permutations(masked_address)
            for p in permutations:
                address = int(p, 2)
                print(address)
                memory[address] = new_value

    total = sum(memory.values())
    return total


def solution_part_1():
    return read_program(data)


def solution_part_2():
    return read_program_floating(data)


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())
