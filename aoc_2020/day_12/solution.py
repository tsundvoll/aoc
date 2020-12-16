from scipy.spatial.transform import Rotation as R


def parse(input_data):
    d = []
    for line in input_data:
        action = line[0]
        value = int(line[1:])
        d.append((action, value))
    return d


data = parse([x for x in open('input.txt').read().splitlines()])


def travel(instructions):
    east = 0
    north = 0
    heading = 0 # 0 - East 1 - South 2 - West 3 - North
    for instr in instructions:
        action = instr[0]
        value = instr[1]
        if action == 'N':
            north += value
        if action == 'S':
            north -= value
        if action == 'E':
            east += value
        if action == 'W':
            east -= value
        if action == 'L':
            degree = value / 90
            heading = (heading - degree) % 4
        if action == 'R':
            degree = value / 90
            heading = (heading + degree) % 4
        if action == 'F':
            if heading == 0:
                east += value
            if heading == 1:
                north -= value
            if heading == 2:
                east -= value
            if heading == 3:
                north += value
            
    return east, north


def travel_waypoint(instructions):
    east = 0
    north = 0
    heading = 0 # 0 - East 1 - South 2 - West 3 - North
    r = R.from_euler('z', 0, degrees=True)
    waypoint = [10, 1, 0]
    for instr in instructions:
        action = instr[0]
        value = instr[1]
        if action == 'N':
            waypoint[1] += value
        if action == 'S':
            waypoint[1] -= value
        if action == 'E':
            waypoint[0] += value
        if action == 'W':
            waypoint[0] -= value
        if action == 'L' or action == 'R':

            if action == 'R':
                r = R.from_euler('z', -value, degrees=True)

            elif action == 'L':
                r = R.from_euler('z', value, degrees=True)

            waypoint = r.apply(waypoint)

        if action == 'F':
            east += waypoint[0]*value
            north += waypoint[1]*value

    return east, north


def solution_part_1():
    east, north = travel(data)
    return abs(east) + abs(north)


def solution_part_2():
    east, north = travel_waypoint(data)
    return abs(east) + abs(north)


if __name__ == "__main__":
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())