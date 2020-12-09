data = [x for x in open('input.txt').read().splitlines()]



def acc_before_loop(program):
    acc = 0
    pc = 0
    visited = {}
    while pc not in visited:
        visited[pc] = 1
        instruction = program[pc]
        op, arg = instruction.split()
        sign = arg[0]
        if sign == "+":
            s = 1
        elif sign == "-":
            s = -1
        num = int(arg[1:])
        if op == "nop":
            pc += 1
        elif op == "acc":
            acc += s*num
            pc += 1
        elif op == "jmp":
            pc += s*num
    return acc



def acc_after_termination(program):
    acc = 0
    pc = 0
    visited = {}
    eof = len(program)
    while pc not in visited:
        visited[pc] = 1
        instruction = program[pc]
        op, arg = instruction.split()
        sign = arg[0]
        if sign == "+":
            s = 1
        elif sign == "-":
            s = -1
        num = int(arg[1:])
        if op == "nop":
            pc += 1
        elif op == "acc":
            acc += s*num
            pc += 1
        elif op == "jmp":
            pc += s*num

        if pc == eof:
            return acc
    raise KeyError("Found loop")


def solution_part_1():
    return acc_before_loop(data)


def solution_part_2():
    changed_data = data.copy()
    for i, line in enumerate(data):
        tmp = changed_data[i]
        op, arg = line.split()
        if op == "nop":
            changed_data[i] = "".join(("jmp ", arg))
        elif op == "jmp":
            changed_data[i] = "".join(("nop ", arg))

        try:
            result = acc_after_termination(changed_data)
            break
        except KeyError as e:
            print(e)
            changed_data[i] = tmp

    return result

if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())