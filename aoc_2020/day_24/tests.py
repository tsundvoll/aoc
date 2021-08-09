from solution import *
import pytest



def test_part_1():
    tiles = parse_tiles_to_turn([x for x in open('test.txt').read().splitlines()])
    print(tiles)
    print(f"{len(tiles)=}")

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

    assert count_black(floor) == 10


def test_part_2():
    tiles_to_turn = parse_tiles_to_turn([x for x in open('test.txt').read().splitlines()])

    floor = {}
    for tile in tiles_to_turn:
        if not tile in floor.keys():
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

        else:
            if floor[tile] == 'black':
                floor[tile] = 'white'
            elif floor[tile] == 'white':
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
            else:
                raise ValueError

    assert count_black(floor) == 10

    floor = flip_tiles(floor)
    assert count_black(floor) == 15




if __name__ == "__main__":
    # tic = time.perf_counter()
    # test_part_1()
    # toc = time.perf_counter()
    # print(f"Ran first tests in {toc - tic:0.6f} seconds")
    

    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()
    print(f"Ran second tests in {toc - tic:0.4f} seconds")