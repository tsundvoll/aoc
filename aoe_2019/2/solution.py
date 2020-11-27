def read_comma_separated_line():
    with open("input.txt", 'r') as f:
        line = f.readline().rstrip("\n")
        data = line.split(",")
        data = [int(x) for x in data]
    return data

data = read_comma_separated_line()


TERMINATE = 99
ADD = 1
MULT = 2


class Intcode:
    
    def __init__(self, program):
        self.program = program
        self.is_executed = False

    def run(self):
        ip = 0
        oc = self.program[ip]
        while oc != TERMINATE:
            first_data = self.program[self.program[ip+1]]
            second_data = self.program[self.program[ip+2]]
            store_location = self.program[ip+3]
            if oc == ADD:
                self.program[store_location] = first_data + second_data
            elif oc == MULT:
                self.program[store_location] = first_data * second_data
            else:
                raise ValueError("Invalid opcode")
            ip += 4
            oc = self.program[ip]

        self.is_executed = True

        return self.program


def solution_part_1():
    program = data.copy()
    program[1] = 12
    program[2] = 2
    
    executable = Intcode(program)
    result = executable.run()

    return result[0]


def solution_part_2():
    new_program = data.copy()

    for noun in range(100):
        for verb in range(100):
            program = new_program.copy()
            program[1] = noun
            program[2] = verb
            executable = Intcode(program)
            result = executable.run()[0]
            if result == 19690720:
                print("Found solution")
                print("Noun is:", noun)
                print("Verb is:", noun)
                return 100*noun + verb

    return "Did not find solution"


print("Answer Part 1:", solution_part_1())
print("Answer Part 2:", solution_part_2())