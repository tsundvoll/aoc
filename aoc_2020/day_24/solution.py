import time



def parse_tiles_to_turn(data):
    tiles = []
    for line in data:
        idx = 0
        i = 0
        j = 0
        while idx < len(line):
            if line[idx] == 's' or line[idx] == 'n':
                direction = line[idx:idx+2]
                idx += 2
            else:
                direction = line[idx]
                idx += 1

            if direction == 'e':
                j += 1
            elif direction == 'se':
                i += 1
            elif direction == 'sw':
                i += 1
                j -= 1
            elif direction == 'w':
                j -= 1
            elif direction == 'nw':
                i -= 1
            elif direction == 'ne':
                i -= 1
                j += 1
        tiles.append((i,j))
    return tiles


def count_black(floor):
    count_black = 0
    for color in floor.values():
        if color == 'black':
            count_black += 1
    return count_black


def flip_tiles(floor):
    to_be_flipped_to_white = []
    to_be_flipped_to_black = []
    for tile, color in floor.items():
        neighbours = [
            (tile[0], tile[0]+1), # e
            (tile[0]+1, tile[0]), # se
            (tile[0]+1, tile[0]-1), # sw
            (tile[0], tile[0]-1), # w
            (tile[0]-1, tile[0]), # nw
            (tile[0]-1, tile[0]+1), # ne
        ]
        black_neighbours = 0
        for neighbour in neighbours:
            try:
                if floor[neighbour] == 'black':
                    black_neighbours += 1
            except KeyError:
                continue
        if color == 'black' and (black_neighbours == 0 or black_neighbours > 2):
            to_be_flipped_to_white.append(tile)
        elif color == 'white' and (black_neighbours == 2):
            to_be_flipped_to_black.append(tile)
    
    for tile in to_be_flipped_to_white:
        floor[tile] = 'white'
    for tile in to_be_flipped_to_black:
        floor[tile] = 'black'

        neighbours = [
            (tile[0], tile[0]+1), # e
            (tile[0]+1, tile[0]), # se
            (tile[0]+1, tile[0]-1), # sw
            (tile[0], tile[0]-1), # w
            (tile[0]-1, tile[0]), # nw
            (tile[0]-1, tile[0]+1), # ne
        ]

        for neighbour in neighbours:
            if not neighbour in floor.keys():
                floor[neighbour] = 'white'

    return floor


def solution_part_1():
    tiles = tiles_to_turn([x for x in open('input.txt').read().splitlines()])

    floor = {}
    for tile in tiles:
        if not tile in floor:
            floor[tile] = 'black'
        else:
            if floor[tile] == 'black':
                floor[tile] = 'white'
            elif floor[tile] == 'white':
                floor[tile] = 'black'
            else:
                raise ValueError

    count_black = 0
    for color in floor.values():
        if color == 'black':
            count_black += 1

    return count_black


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
