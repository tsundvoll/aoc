from solution import *
import pytest



def test_part_1():
    tiles = parse([x for x in open('test.txt').read().splitlines()])

    assert get_image_ids(tiles)[0] == 20899048083289


def test_part_2():
    assert get_rot(0,0) == (2, 2)
    assert get_rot(0,1) == (3, 1)
    assert get_rot(0,2) == (0, 0)
    assert get_rot(0,3) == (1, 3)

    assert get_rot(1,0) == (1, 3)
    assert get_rot(1,1) == (2, 2)
    assert get_rot(1,2) == (3, 1)
    assert get_rot(1,3) == (0, 0)

    assert get_rot(2,0) == (0, 0)
    assert get_rot(2,1) == (1, 3)
    assert get_rot(2,2) == (2, 2)
    assert get_rot(2,3) == (3, 1)

    assert get_rot(3,0) == (3, 1)
    assert get_rot(3,1) == (0, 0)
    assert get_rot(3,2) == (1, 3)
    assert get_rot(3,3) == (2, 2)



    tiles = parse([x for x in open('test.txt').read().splitlines()])
    assert find_water_roughness(tiles) == 273


if __name__ == "__main__":
    tic = time.perf_counter()
    test_part_1()
    toc = time.perf_counter()
    print(f"Ran first tests in {toc - tic:0.4f} seconds\n")
    

    tic = time.perf_counter()
    test_part_2()
    toc = time.perf_counter()

    print(f"Ran second tests in {toc - tic:0.4f} seconds")