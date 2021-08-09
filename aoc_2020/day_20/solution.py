import time
import numpy as np
import math
import copy

def parse(data):
    tiles = {}
    current_title = None
    current_tile = np.zeros((10,10), np.int8)
    current_row = 0
    for line in data:
        if line == "":
            tiles[current_title] = current_tile
            
            current_title = None
            current_tile = np.zeros((10,10), np.int8)
            current_row = 0
            continue
        elif line[0] == 'T':
            _, t_id = line.split(" ")
            current_title = int(t_id[:-1])
        else:
            current_line = np.array([1 if x=='#' else 0 for x in line])
            current_tile[current_row] = current_line
            current_row += 1

    return tiles


def get_rot(self_dir, other_dir):
    diff = other_dir - self_dir
    if diff == 0:
        return 2, 2
    elif diff in [-2, 2]:
        return 0, 0
    elif diff in [-1, 3]:
        return 1, 3
    elif diff in [-3, 1]:
        return 3, 1


test_tile = np.array([
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,1,1,1,0,0,0],
    [0,0,0,1,1,1,1,0,0,0],
    [0,0,0,1,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
])

class Tile():
    def __init__(self, id, tile_image, edges, flipped_edges):
        self.id = id
        self.tile_image = tile_image
        self.edges = edges
        self.flipped_edges = flipped_edges
        self.n_adjacent_tiles = 0
        self.rotation = None # 0: 0*, 1: 90*, 2: 180*, 3: 270*
        self.flipped_horizontally = False
        self.flipped_vertically = False
        self.to_be_flipped_horizontally = False
        self.to_be_flipped_vertically = False
        self.rotated = False
        self.is_fixed = False
        self.neighbours = [None, None, None, None] # Above, left, below, right
        self.true_edges = copy.deepcopy(edges)

    def flip_horizontally(self):
        self.tile_image = np.fliplr(self.tile_image)

    def flip_vertically(self):
        self.tile_image = np.flipud(self.tile_image)

    def rotate_n_times(self, n):
        self.tile_image = np.rot90(self.tile_image, n)
        for _ in range(n):
            self.true_edges.insert(0, self.true_edges.pop())


    def align(self, other):
        for edge in self.edges + self.flipped_edges:
            if edge in other.edges + other.flipped_edges:
                # Alignment found
                print(f"Align self ({self.id}) and other ({other.id})")
                self.n_adjacent_tiles += 1
                other.n_adjacent_tiles += 1

                self_dir = (self.edges + self.flipped_edges).index(edge) % 4
                other_dir = (other.edges + other.flipped_edges).index(edge) % 4

                other_edge_flipped = True if edge in other.flipped_edges else False

                # if not other_edge_flipped:
                if other_dir in [1, 3]: # Left or right side must be flipped -> vertical flip
                    if not other.flipped_vertically:
                        other.flipped_vertically = True
                        other.to_be_flipped_vertically = True
                        print("Will flip", other.id, "vertically")
                    else:
                        if self_dir in [1, 3]: # Self must be flipped vertically
                            assert not self.flipped_vertically
                            self.flipped_vertically = True
                            self.to_be_flipped_vertically = True
                            print("Will flip", self.id, "vertically")
                        elif self_dir in [0, 2]: # Self must be flipped horizontally
                            assert not self.flipped_horizontally
                            self.flipped_horizontally = True
                            self.to_be_flipped_horizontally = True
                            print("Will flip", self.id, "horizontally")
                        else:
                            raise ValueError
                elif other_dir in [0, 2]: # Top or bottom must be flipped -> horizontal flip
                    if not other.flipped_horizontally:
                        other.flipped_horizontally = True
                        other.to_be_flipped_horizontally = True
                        print("Will flip", other.id, "horizontally")
                    else:
                        if self_dir in [1, 3]: # Self must be flipped vertically
                            assert not self.flipped_vertically
                            self.flipped_vertically = True
                            self.to_be_flipped_vertically = True
                            print("Will flip", self.id, "vertically")
                        elif self_dir in [0, 2]: # Self must be flipped horizontally
                            assert not self.flipped_horizontally
                            self.flipped_horizontally = True
                            self.to_be_flipped_horizontally = True
                            print("Will flip", self.id, "horizontally")
                        else:
                            raise ValueError
                # else:
                #     raise ValueError
                break


    def rotate(self, other):
        for edge in self.edges + self.flipped_edges:
            if edge in other.edges + other.flipped_edges:

                self_dir = (self.edges + self.flipped_edges).index(edge) % 4
                other_dir = (other.edges + other.flipped_edges).index(edge) % 4

                self_mapping = [0, 1, 2, 3]
                if not self.is_fixed:
                    if self.to_be_flipped_horizontally and self.to_be_flipped_vertically:
                        self.true_edges[0] = self.flipped_edges[2]
                        self.true_edges[1] = self.flipped_edges[3]
                        self.true_edges[2] = self.flipped_edges[0]
                        self.true_edges[3] = self.flipped_edges[1]
                        self_mapping = [2, 3, 0, 1]
                        self.flip_horizontally()
                        self.flip_vertically()
                    elif self.to_be_flipped_horizontally:
                        self.true_edges[0] = self.flipped_edges[0]
                        self.true_edges[1] = self.edges[3]
                        self.true_edges[2] = self.flipped_edges[2]
                        self.true_edges[3] = self.edges[1]
                        self_mapping = [0, 3, 2, 1]
                        self.flip_horizontally()
                    elif self.to_be_flipped_vertically:
                        self.true_edges[0] = self.edges[2]
                        self.true_edges[1] = self.flipped_edges[1]
                        self.true_edges[2] = self.edges[0]
                        self.true_edges[3] = self.flipped_edges[3]
                        self_mapping = [2, 1, 0, 2]
                        self.flip_vertically()
                    else:
                        self.true_edges[0] = self.edges[0]
                        self.true_edges[1] = self.edges[1]
                        self.true_edges[2] = self.edges[2]
                        self.true_edges[3] = self.edges[3]

                other_mapping = [0, 1, 2, 3]
                if not other.is_fixed:
                    if other.to_be_flipped_horizontally and other.to_be_flipped_vertically:
                        other.true_edges[0] = other.flipped_edges[2]
                        other.true_edges[1] = other.flipped_edges[3]
                        other.true_edges[2] = other.flipped_edges[0]
                        other.true_edges[3] = other.flipped_edges[1]
                        other.flip_horizontally()
                        other.flip_vertically()
                        other_mapping = [2, 3, 0, 1]
                    elif other.to_be_flipped_horizontally:
                        other.true_edges[0] = other.flipped_edges[0]
                        other.true_edges[1] = other.edges[3]
                        other.true_edges[2] = other.flipped_edges[2]
                        other.true_edges[3] = other.edges[1]
                        other_mapping = [0, 3, 2, 1]
                        other.flip_horizontally()
                    elif other.to_be_flipped_vertically:
                        other.true_edges[0] = other.edges[2]
                        other.true_edges[1] = other.flipped_edges[1]
                        other.true_edges[2] = other.edges[0]
                        other.true_edges[3] = other.flipped_edges[3]
                        other_mapping = [2, 1, 0, 3]
                        other.flip_vertically()
                    else:
                        other.true_edges[0] = other.edges[0]
                        other.true_edges[1] = other.edges[1]
                        other.true_edges[2] = other.edges[2]
                        other.true_edges[3] = other.edges[3]

                self_dir = self_mapping[self_dir]
                other_dir = other_mapping[other_dir]

                self_rot, other_rot = get_rot(self_dir, other_dir)

                if other_rot != 0:
                    if not other.is_fixed:
                        # print(f"Rotated other ({other.id})")
                        other.rotate_n_times(other_rot)
                        other_dir = (other_dir + other_rot) % 4
                    elif not self.is_fixed:
                        # print(f"Self other ({self.id})")
                        self.rotate_n_times(self_rot)
                        self_dir = (self_dir + self_rot) % 4
                    # else:
                        # print("Both was already fixed")
                # else:
                    # print("No need to rotate")

                self.neighbours[self_dir] = other
                other.neighbours[other_dir] = self

                self.is_fixed = True
                other.is_fixed = True

                break


class Image():
    def __init__(self, tiles):
        size = int(math.sqrt(len(tiles)))*10
        image = np.zeros((size, size), np.int8)
        corner = tiles[0]
        while not corner.neighbours[0] is None:
            corner = corner.neighbours[0]
        while not corner.neighbours[1] is None:
            corner = corner.neighbours[1]
        print("Corner:", corner.id)

        row = 0
        col = 0
        image[row*10:row*10+10, col*10:col*10+10] = corner.tile_image

        all_ids = [[0]*3]*3

        # current_tile = corner
        # current_tile = current_tile.neighbours[3]
        # while not current_tile is None:
        #     all_tiles.append([current_tile])
        #     # print(current_tile.id)
        #     # col += 1
        #     # image[row*10:row*10+10, col*10:col*10+10] = current_tile.tile_image
        #     current_tile = current_tile.neighbours[3]

        # # for col, top_tile in enumerate(all_tiles):
        # #     current_tile = top_tile[col].neighbours[2]
        # #     while not current_tile is None:
        # #         all_tiles[col].append(current_tile)
        # #         current_tile = current_tile.neighbours[2]


        print("IDs")
        print("------------------")
        for row in all_ids:
            for element in row:
                print(element, end=" ")
            print()
        print("\n------------------")

        # print(corner.neighbours)
        one_down = corner.neighbours[2]
        image[10:20, :10] = one_down.tile_image

        two_down = one_down.neighbours[2]
        image[20:30, :10] = two_down.tile_image

        self.image = image


    def print(self):
        print(self.image)


def get_image_ids(dict_tiles):
    tiles = []

    for tile_id, tile_image in dict_tiles.items():
        top_row = tile_image[0]
        left_col = tile_image[:,0][::-1]
        bottom_row = tile_image[9][::-1]
        right_col = tile_image[:,9]

        top_hash = int("".join(list('1' if x==1 else '0' for x in top_row)), 2)
        left_hash = int("".join(list('1' if x==1 else '0' for x in left_col)), 2)
        bottom_hash = int("".join(list('1' if x==1 else '0' for x in bottom_row)), 2)
        right_hash = int("".join(list('1' if x==1 else '0' for x in right_col)), 2)
        edges = [top_hash, left_hash, bottom_hash, right_hash]

        top_hash_flipped = int("".join(list('1' if x==1 else '0' for x in np.flip(top_row))), 2)
        left_hash_flipped = int("".join(list('1' if x==1 else '0' for x in np.flip(left_col))), 2)
        bottom_hash_flipped = int("".join(list('1' if x==1 else '0' for x in np.flip(bottom_row))), 2)
        right_hash_flipped = int("".join(list('1' if x==1 else '0' for x in np.flip(right_col))), 2)
        flipped_edges = [top_hash_flipped, left_hash_flipped, bottom_hash_flipped, right_hash_flipped]

        new_tile = Tile(tile_id, tile_image, edges, flipped_edges)
        tiles.append(new_tile)

    tiles[0].flipped_horizontally = True
    tiles[0].flipped_vertically = True
    tiles[0].rotated = True
    tiles[0].is_fixed = True

    # 36 combinations
    for i in range(len(tiles)):
        for j in range(i, len(tiles)):
            if i != j:
                tiles[i].align(tiles[j])

    prod = 1
    for tile in tiles:
        if tile.n_adjacent_tiles == 2:
            prod *= tile.id

    # 36 combinations
    for i in range(len(tiles)):
        for j in range(i, len(tiles)):
            if i != j:
                tiles[i].rotate(tiles[j])

    return prod, tiles


def find_water_roughness(dict_tiles):
    _, tiles = get_image_ids(dict_tiles)
    image = Image(tiles)
    image.print()
    return 0


def solution_part_1():
    input_data = parse([x for x in open('input.txt').read().splitlines()])
    return get_image_ids(input_data)[0]


def solution_part_2():
    return "Not solved yet"
    # input_data = parse([x for x in open('input.txt').read().splitlines()])
    # assert find_water_roughness(input_data) == 273


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



"""
        # for edge in self.true_edges:
        #     if edge in other.true_edges:
        #         self_dir = self.true_edges.index(edge) % 4
        #         other_dir = other.true_edges.index(edge) % 4

        #         print("Rotate", self.id, "and", other.id)

        #         assert self.neighbours[self_dir] in [None, other]
        #         self.neighbours[self_dir] = other
        #         assert other.neighbours[other_dir] in [None, self]
        #         other.neighbours[other_dir] = self

        #         self_rot, other_rot = get_rot(self_dir, other_dir)

        #         if other.rotation is None:
        #             print("Rotate other", other.id, "to", other_rot)
        #             other.rotation = other_rot
        #             for _ in range(other_rot):
        #                 other.true_edges.insert(0, other.true_edges.pop())
        #                 other.neighbours.insert(0, other.neighbours.pop())
        #         elif self.rotation is None:
        #             print("Rotate self", self.id, "to", self_rot)
        #             self.rotation = self_rot
        #             for _ in range(self_rot):
        #                 self.true_edges.insert(0, self.true_edges.pop())
        #                 self.neighbours.insert(0, self.neighbours.pop())
"""
