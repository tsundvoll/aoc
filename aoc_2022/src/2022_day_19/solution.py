import os
import re
import time
from copy import copy
from enum import Enum
from functools import lru_cache

import pyperclip
from tqdm import tqdm


class Material(Enum):
    ORE = 1
    CLAY = 2
    OBSIDIAN = 3
    GEODE = 4


class Robot:
    def __init__(self, robot_type, ore_cost=0, clay_cost=0, obsidian_cost=0):
        self.type = robot_type
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost


def first_task(input_data):
    global max_geodes
    TIME_LIMIT = 24
    quality_levels = 0
    for i in tqdm(range(len(input_data))):
        (
            blueprint_id,
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost,
            obsidian_robot_clay_cost,
            geode_robot_ore_cost,
            geode_robot_obsidian_cost,
        ) = tuple(map(int, re.findall(r"\d+", input_data[i])))
        robots = (
            1,  # "ore_robots":
            0,  # "clay_robots":
            0,  # "obsidian_robots":
            0,  # "geode_robots":
        )
        material = (
            0,  # "ore":
            0,  # "clay":
            0,  # "obsidian":
            0,  # "geode":
        )

        max_geodes = 0

        @lru_cache()
        def build_robots(minute, robots, material):
            global max_geodes
            if minute >= TIME_LIMIT:
                if material[3] > max_geodes:
                    max_geodes = material[3]
                # print("Robots:", robots)
                # print("Materials:", material)
                return

            building_a_robot_is_an_option = False

            # Build geode robot if possible
            if (
                material[0] >= geode_robot_ore_cost
                and material[2] >= geode_robot_obsidian_cost
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= geode_robot_ore_cost
                new_material[2] -= geode_robot_obsidian_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[3] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))
                return

            # Build obsidian robot if possible
            if (
                material[0] >= obsidian_robot_ore_cost
                and material[1] >= obsidian_robot_clay_cost
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= obsidian_robot_ore_cost
                new_material[1] -= obsidian_robot_clay_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[2] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

            # Build ore robot if possible
            if material[0] >= ore_robot_ore_cost and robots[0] < max(
                ore_robot_ore_cost,
                clay_robot_ore_cost,
                obsidian_robot_ore_cost,
                geode_robot_ore_cost,
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= ore_robot_ore_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[0] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

            # Build clay robot if possible
            if (
                material[0] >= clay_robot_ore_cost
                and robots[1] < obsidian_robot_clay_cost
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= clay_robot_ore_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[1] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

            # Just gather more materials if not enoguh to build any robot
            if material[0] < max(
                ore_robot_ore_cost,
                clay_robot_ore_cost,
                obsidian_robot_ore_cost,
                geode_robot_ore_cost,
            ):
                new_material = list(material)

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

        build_robots(0, copy(robots), copy(material))
        quality_levels += max_geodes * blueprint_id
    return quality_levels


def second_task(input_data):
    global max_geodes
    TIME_LIMIT = 32
    product = 1
    for i in tqdm(range(3)):
        (
            blueprint_id,
            ore_robot_ore_cost,
            clay_robot_ore_cost,
            obsidian_robot_ore_cost,
            obsidian_robot_clay_cost,
            geode_robot_ore_cost,
            geode_robot_obsidian_cost,
        ) = tuple(map(int, re.findall(r"\d+", input_data[i])))
        robots = (
            1,  # "ore_robots":
            0,  # "clay_robots":
            0,  # "obsidian_robots":
            0,  # "geode_robots":
        )
        material = (
            0,  # "ore":
            0,  # "clay":
            0,  # "obsidian":
            0,  # "geode":
        )

        max_geodes = 0

        @lru_cache()
        def build_robots(minute, robots, material):
            global max_geodes
            if minute >= TIME_LIMIT:
                if material[3] > max_geodes:
                    max_geodes = material[3]
                # print("Robots:", robots)
                # print("Materials:", material)
                return

            building_a_robot_is_an_option = False

            # Build geode robot if possible
            if (
                material[0] >= geode_robot_ore_cost
                and material[2] >= geode_robot_obsidian_cost
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= geode_robot_ore_cost
                new_material[2] -= geode_robot_obsidian_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[3] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))
                return

            # Build obsidian robot if possible
            if (
                material[0] >= obsidian_robot_ore_cost
                and material[1] >= obsidian_robot_clay_cost
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= obsidian_robot_ore_cost
                new_material[1] -= obsidian_robot_clay_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[2] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

            # Build ore robot if possible
            if material[0] >= ore_robot_ore_cost and robots[0] < max(
                ore_robot_ore_cost,
                clay_robot_ore_cost,
                obsidian_robot_ore_cost,
                geode_robot_ore_cost,
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= ore_robot_ore_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[0] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

            # Build clay robot if possible
            if (
                material[0] >= clay_robot_ore_cost
                and robots[1] < obsidian_robot_clay_cost
            ):
                building_a_robot_is_an_option = True

                new_material = list(material)
                # Use material to build robot
                new_material[0] -= clay_robot_ore_cost

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                new_robots[1] += 1

                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

            # Just gather more materials if not enoguh to build any robot
            if material[0] < max(
                ore_robot_ore_cost,
                clay_robot_ore_cost,
                obsidian_robot_ore_cost,
                geode_robot_ore_cost,
            ):
                new_material = list(material)

                # Use robots to collect material
                new_material[0] += robots[0]
                new_material[1] += robots[1]
                new_material[2] += robots[2]
                new_material[3] += robots[3]

                new_robots = list(robots)
                build_robots(minute + 1, tuple(new_robots), tuple(new_material))

        build_robots(0, copy(robots), copy(material))
        product *= max_geodes
    return product


def run_day():
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = list(map(lambda line: line.strip(), open(input_file, "r")))

    t_start = time.time()
    first_answer = first_task(input_data)
    t_end = time.time()
    first_time = round(t_end - t_start, 2)
    if first_answer is not None:
        pyperclip.copy(str(first_answer))
        pyperclip.paste()

    print("#############################")
    print("The answer to the 1st task is")
    print(first_answer, f"in {first_time} seconds")

    t_start = time.time()
    second_answer = second_task(input_data)
    t_end = time.time()
    second_time = round(t_end - t_start, 3)
    if second_answer is not None:
        pyperclip.copy(str(second_answer))
        pyperclip.paste()

    print()
    print("The answer to the 2nd task is")
    print(second_answer, f"in {second_time} seconds")
    print("#############################")


if __name__ == "__main__":
    run_day()
