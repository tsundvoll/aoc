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


class Tile():
    def __init__(self, id, tile_image, edges, flipped_edges):
        self.id = id
        self.tile_image = tile_image
        self.edges = edges
        self.flipped_edges = flipped_edges
        self.adjacent_tiles = []
        self.adjacent_edges = []
        self.n_adjacent_tiles = 0
        self.rotation = None # 0: 0*, 1: 90*, 2: 180*, 3: 270*
        self.flipped_horizontally = False
        self.flipped_vertically = False
        self.rotated = False
        self.neighbours = [None, None, None, None] # Above, left, below, right
        self.true_edges = copy.deepcopy(edges)

    def flip_horizontally(self):
        if not self.flipped_horizontally:
            self.flipped_horizontally = True
            tmp = self.true_edges[1]
            self.true_edges[1] = self.true_edges[3]
            self.true_edges[3] = tmp
            self.true_edges[0] = self.flipped_edges[0]
            self.true_edges[2] = self.flipped_edges[2]
            self.tile_image = np.fliplr(self.tile_image)

    def flip_vertically(self):
        if not self.flipped_vertically:
            self.flipped_vertically = True
            tmp = self.true_edges[0]
            self.true_edges[0] = self.true_edges[2]
            self.true_edges[2] = tmp
            self.true_edges[1] = self.flipped_edges[1]
            self.true_edges[3] = self.flipped_edges[3]
            self.tile_image = np.flipud(self.tile_image)

    def rotate_n_times(self, n):
        self.tile_image = np.rot90(self.tile_image, n)

    def align(self, other):
        for edge in self.edges + self.flipped_edges:
            if edge in other.edges + other.flipped_edges:
                # if self.id == 1171 or other.id == 1171:
                #     print("Align", self.id, "and", other.id)
                #     if edge in self.flipped_edges:
                #         print("Edge in self.flipped_edges")
                #     if edge in self.edges:
                #         print("Edge in self.edges")
                #     if edge in other.flipped_edges:
                #         print("Edge in other.flipped_edges")
                # Alignment found
                self.adjacent_tiles.append(other)
                self.adjacent_edges.append(edge)
                other.adjacent_tiles.append(self)
                other.adjacent_edges.append(edge)
                self.n_adjacent_tiles += 1
                other.n_adjacent_tiles += 1

                self_dir = (self.edges + self.flipped_edges).index(edge) % 4
                other_dir = (other.edges + other.flipped_edges).index(edge) % 4

                if edge in self.flipped_edges:
                    flipped_idx = self.flipped_edges.index(edge)
                    if flipped_idx in [0,2]: # Top or bottom flipped -> horizontal flip
                        self.flip_horizontally()
                        if self_dir == other_dir:
                            other.flip_horizontally()
                    elif flipped_idx in [1,3]: # Left or right flipped -> vertical flip
                        self.flip_vertically()
                        if self_dir == other_dir:
                            other.flip_vertically()

                if edge in other.flipped_edges:
                    flipped_idx = other.flipped_edges.index(edge)
                    if flipped_idx in [0,2]: # Top or bottom flipped -> horizontal flip
                        other.flip_horizontally()
                        if self_dir == other_dir:
                            self.flip_horizontally()
                    elif flipped_idx in [1,3]: # Left or right flipped -> vertical flip
                        other.flip_vertically()
                        if self_dir == other_dir:
                            self.flip_vertically()
                break


    def rotate(self, other):
        for edge in self.true_edges:
            if edge in other.true_edges:
                self_dir = self.true_edges.index(edge) % 4
                other_dir = other.true_edges.index(edge) % 4

                print("Rotate", self.id, "and", other.id)

                assert self.neighbours[self_dir] in [None, other]
                self.neighbours[self_dir] = other
                assert other.neighbours[other_dir] in [None, self]
                other.neighbours[other_dir] = self

                self_rot, other_rot = get_rot(self_dir, other_dir)

                if other.rotation is None:
                    # print("Rotate", other.id, "to", other_rot)
                    other.rotation = other_rot
                    for _ in range(other_rot):
                        other.true_edges.insert(0, other.true_edges.pop())
                        other.neighbours.insert(0, other.neighbours.pop())
                elif self.rotation is None:
                    # print("Rotate", self.id, "to", self_rot)
                    self.rotation = self_rot
                    for _ in range(self_rot):
                        self.true_edges.insert(0, self.true_edges.pop())
                        self.neighbours.insert(0, self.neighbours.pop())
                break



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



class Image():
    def __init__(self, tiles):
        size = int(math.sqrt(len(tiles)))*10
        corner = tiles[0]
        while not corner.neighbours[0] is None:
            corner = corner.neighbours[0]
        while not corner.neighbours[1] is None:
            corner = corner.neighbours[1]
        print("Corner:", corner.id)

        # for tile in tiles:
        #     print()
        #     print(len(list(filter(lambda x: not x is None, tile.neighbours))))
        #     print(tile.n_adjacent_tiles)

        image = np.zeros((size, size), np.int8)
        image[:10, :10] = corner.tile_image

        print(corner.id)
        print(corner.flipped_vertically)
        print(corner.flipped_horizontally)
        print(corner.rotation)

        # print(corner.neighbours)
        one_down = corner.neighbours[2]
        image[10:20, :10] = one_down.tile_image

        print(one_down.id)
        print(one_down.flipped_vertically)
        print(one_down.flipped_horizontally)
        print(one_down.rotation)


        self.image = image
        # flipped_h = np.fliplr(test_tile) 
        # flipped_v = np.flipud(test_tile)
        # rot_1 = np.rot90(test_tile, 1)
        # rot_2 = np.rot90(test_tile, 2)
        # rot_3 = np.rot90(test_tile, 3)


        # self.image = rot_3


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

    def align(self, other):
        for edge in self.edges + self.flipped_edges:
            if edge in other.edges + other.flipped_edges:
                # Alignment found
                self.adjacent_tiles.append(other)
                self.adjacent_edges.append(edge)
                other.adjacent_tiles.append(self)
                other.adjacent_edges.append(edge)
                self.n_adjacent_tiles += 1
                other.n_adjacent_tiles += 1

                if edge in self.flipped_edges[:2]:
                    self.rotation = "flipped_rl"
                elif edge in self.flipped_edges[2:]:
                    self.rotation = "flipped_tb"
                elif edge in other.flipped_edges[:2]:
                    other.rotation = "flipped_rl"
                elif edge in other.flipped_edges[2:]:
                    other.rotation = "flipped_tb"
                

                break
"""