import time
import numpy as np
import operator
from scipy import ndimage




def parse(input_data):
    return np.array([[[0 if x=='.' else 1 for x in line] for line in input_data]])


def parse_4d(input_data):
    return np.array([[[[0 if x=='.' else 1 for x in line] for line in input_data]]])

data = parse([x for x in open('input.txt').read().splitlines()])
data_4d = parse_4d([x for x in open('input.txt').read().splitlines()])


def find_active_neighbors(pocket, x,y,z):
    count = 0
    for layer in [z-1, z+1]:
        for row in [x-1, x+1]:
            for col in [y-1, y+1]:
                count += pocket[z][x][y]
    return count


def run_cycles(pocket, n_cycles):
    # new_pocket_shape = tuple(map(operator.add, pocket.shape, (2,2,2)))
    k = np.ones((3,3,3), dtype=np.int8)
    for _ in range(n_cycles):
        new_pocket = np.pad(pocket, 1, 'constant')
        # print(new_pocket.shape)
        # print(new_pocket)
        # print(new_pocket)

        change_to = {0: [], 1: []}
        # img = img[:,:,None] # Add singleton dimension
        neighbours = ndimage.convolve(new_pocket, k, mode='constant', cval=0.0)
        # finalOutput = result.squeeze() # Remove singleton dimension

        for z, layer in enumerate(new_pocket):
            for x, row in enumerate(layer):
                for y, cube in enumerate(row):
                    active_neighbors = neighbours[(z,x,y)]-cube
                    if cube == 1:
                        if not (active_neighbors == 2 or active_neighbors == 3):
                            change_to[0].append((z,x,y))
                    if cube == 0:
                        if active_neighbors == 3:
                            change_to[1].append((z,x,y))

        for c_0 in change_to[0]:
            new_pocket[c_0] = 0
        for c_1 in change_to[1]:
            new_pocket[c_1] = 1

        print(new_pocket)
        pocket = new_pocket

    return np.count_nonzero(new_pocket)


def run_cycles_hyperspace(pocket, n_cycles):
    # new_pocket_shape = tuple(map(operator.add, pocket.shape, (2,2,2)))
    k = np.ones((3,3,3,3), dtype=np.int8)
    for _ in range(n_cycles):
        new_pocket = np.pad(pocket, 1, 'constant')
        # new_pocket = np.pad(new_pocket, 1, 'constant')
        # print(pocket)
        # print(new_pocket)
        # print(new_pocket.shape)
        # print(new_pocket)
        # print(new_pocket)

        change_to = {0: [], 1: []}
        # img = img[:,:,None] # Add singleton dimension
        neighbours = ndimage.convolve(new_pocket, k, mode='constant', cval=0.0)
        # finalOutput = result.squeeze() # Remove singleton dimension

        for w, hyper_layer in enumerate(new_pocket):
            for z, layer in enumerate(hyper_layer):
                for x, row in enumerate(layer):
                    for y, cube in enumerate(row):
                        active_neighbors = neighbours[(w,z,x,y)]-cube
                        if cube == 1:
                            if not (active_neighbors == 2 or active_neighbors == 3):
                                change_to[0].append((w,z,x,y))
                        if cube == 0:
                            if active_neighbors == 3:
                                change_to[1].append((w,z,x,y))

        for c_0 in change_to[0]:
            new_pocket[c_0] = 0
        for c_1 in change_to[1]:
            new_pocket[c_1] = 1

        # print(new_pocket)
        pocket = new_pocket
        # break

    return np.count_nonzero(new_pocket)


def solution_part_1():

    return run_cycles(data, 6)


def solution_part_2():
    return run_cycles_hyperspace(data_4d, 6)


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
