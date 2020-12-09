import numpy as np
import matplotlib.pyplot as plt

def read_comma_separated_line():
    with open("input.txt", 'r') as f:
        data = []
        for line in f:
            currentline = line.split(',')
            tmp = []
            for element in currentline:
                tmp.append(element.strip('\n'))
            data.append(tmp)
    return data

data = read_comma_separated_line()


class PrintableMap:
    def __init__(self, width=1, height=1):
        self.array = np.zeros((width, height))
        self.wire_counter = 1

    def set_array(self, array):
        self.array = array

    def plot(self):
        print_array = np.rot90(self.array, 1)
        width = print_array.shape[1]

        top_line = "+" + "-"*width + "+"
        print(top_line)
        for row in print_array:
            print("|", end="")
            for el in row:
                if el > 0:
                    text = "+"
                elif el == -1:
                    text = "o"
                else:
                    text = "."
                print(text, end="")
            print("|")
        print(top_line)

    def place_wire(self, x, y):
        if self.array[x][y] == 0:
            self.array[x][y] = self.wire_counter
        self.wire_counter += 1

    def place_start(self, x, y):
        self.array[x][y] = -1

    def bitwise_and(self, other):
        logic_self = (self.array > 0).astype(int)
        logic_other = (other.array > 0).astype(int)

        return np.bitwise_and(logic_self, logic_other)


class WireMap:
    def __init__(self, wire):
        current_position = {"R": 0, "U": 0}
        max_direction = {"R": 0, "L": 0, "U": 0, "D": 0}

        for segment in wire:
            direction = segment[0]
            distance = int(segment[1:])

            if direction == "R":
                current_position["R"] += distance
                if current_position["R"] > max_direction["R"]:
                    max_direction["R"] = current_position["R"]
            elif direction == "L":
                current_position["R"] -= distance
                if current_position["R"] < max_direction["L"]:
                    max_direction["L"] = current_position["R"]

            elif direction == "U":
                current_position["U"] += distance
                if current_position["U"] > max_direction["U"]:
                    max_direction["U"] = current_position["U"]
            elif direction == "D":
                current_position["U"] -= distance
                if current_position["U"] < max_direction["D"]:
                    max_direction["D"] = current_position["U"]

        width = max_direction["R"] - max_direction["L"] + 1
        height = max_direction["U"] - max_direction["D"] + 1

        self.center_r = abs(max_direction["L"])
        self.center_u = abs(max_direction["D"])
        self.max_direction = max_direction

        self.wire_map = PrintableMap(width, height)
        self.wire_map.place_start(self.center_r, self.center_u)

        # Populate the map
        coord_x = self.center_r
        coord_y = self.center_u
        for segment in wire:
            direction = segment[0]
            distance = int(segment[1:])

            for i in range(distance):
                if direction == "R":
                    coord_x += 1
                elif direction == "L":
                    coord_x -= 1
                elif direction == "U":
                    coord_y += 1
                elif direction == "D":
                    coord_y -= 1
                else:
                    raise ValueError("Invalid direction")
                self.wire_map.place_wire(coord_x, coord_y)

    def plot(self):
        self.wire_map.plot()


    def get_crop(self, common_left, common_right, common_down, common_up):
        min_r = self.center_r + common_left
        max_r = self.center_r + common_right + 1

        min_u = self.center_u + common_down
        max_u = self.center_u + common_up + 1

        new_map = PrintableMap()
        new_map.set_array(self.wire_map.array[min_r:max_r, min_u:max_u])
        return new_map

    def crosses(self, other):
        # self.plot()
        # other.plot()

        common_right = min(self.max_direction["R"], other.max_direction["R"])
        common_left = max(self.max_direction["L"], other.max_direction["L"])
        common_up = min(self.max_direction["U"], other.max_direction["U"])
        common_down = max(self.max_direction["D"], other.max_direction["D"])

        cropped_self = self.get_crop(common_left, common_right, common_down, common_up)
        cropped_other = other.get_crop(common_left, common_right, common_down, common_up)

        # cropped_self.plot()
        # cropped_other.plot()

        array_and = cropped_self.bitwise_and(cropped_other)
        new_map = PrintableMap()
        new_map.set_array(array_and)
        # new_map.plot()

        crossed_array = array_and
        crossings = np.where(crossed_array == 1)
        pairs = np.asarray(crossings).T
        
        num_pairs = pairs.shape[0]
        center = np.array([[abs(common_left), abs(common_down)]]*num_pairs)

        dist_vector = np.subtract(pairs, center)

        distances = np.linalg.norm(dist_vector, ord=1, axis=1)
        smallest_distance = np.min(distances)

        return smallest_distance, dist_vector


def find_closest_cross_location(first_wire, second_wire):
    map_1 = WireMap(first_wire)
    map_2 = WireMap(second_wire)
    result = map_1.crosses(map_2)
    return result[0]


def find_fewest_steps_to_intersection(first_wire, second_wire):
    map_1 = WireMap(first_wire)
    map_2 = WireMap(second_wire)
    intersections = map_1.crosses(map_2)[1]
    # print(f"{intersections=}")

    steps_array = []
    for intersection in intersections:
        r_1 = intersection[0] + map_1.center_r
        r_2 = intersection[0] + map_2.center_r
        u_1 = intersection[1] + map_1.center_u
        u_2 = intersection[1] + map_2.center_u
        x = map_1.wire_map.array[r_1][u_1]
        y = map_2.wire_map.array[r_2][u_2]

        # print("Intersection map 1: ({},{})".format(r_1, u_1))
        # print("Intersection map 2: ({},{})".format(r_2, u_2))

        # print("Steps: {} + {} = {}".format(x, y, x+y))
        steps_array.append(x+y)

    return np.min(np.array(steps_array))


def solution_part_1():
    first_wire = data[0]
    second_wire = data[1]
    print(first_wire)
    print(second_wire)
    return find_closest_cross_location(first_wire, second_wire)


def solution_part_2():
    first_wire = data[0]
    second_wire = data[1]
    return find_fewest_steps_to_intersection(first_wire, second_wire)


# print("Answer Part 1:", solution_part_1())
print("Answer Part 2:", solution_part_2())