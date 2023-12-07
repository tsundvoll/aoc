import math
import os
import time

import pyperclip


class Mapping(dict):
    def __init__(self, mappings: list[tuple[int, int, int]]):
        self.mappings = mappings

    def __missing__(self, key: int) -> int:
        for mapping in self.mappings:
            dest_start, source_start, range_length = mapping
            if key in range(source_start, source_start + range_length):
                step = key - source_start
                return dest_start + step
        return key


def first_task(input_data: list[str]):
    seeds = set(map(int, input_data[0].strip("seeds: ").split()))

    mappings: list[Mapping] = []
    current_mapping = []
    for i in range(2, len(input_data)):
        value = input_data[i]
        if value == "":
            mappings.append(Mapping(current_mapping))
            current_mapping = []
        elif value[0].isdigit():
            dest_range_start, source_range_start, range_length = map(int, value.split())
            current_mapping.append((dest_range_start, source_range_start, range_length))
    mappings.append(Mapping(current_mapping))

    locations = []
    for seed in seeds:
        soil = mappings[0][seed]
        fertilizer = mappings[1][soil]
        water = mappings[2][fertilizer]
        light = mappings[3][water]
        temperature = mappings[4][light]
        humidity = mappings[5][temperature]
        location = mappings[6][humidity]
        locations.append(location)
    return min(locations)


def second_task(input_data: list[str]):
    mappings: list[tuple[dict, int, int]] = []

    global_min = math.inf
    global_max = -math.inf

    current_min = math.inf
    current_max = -math.inf

    current_mappings = {}
    for i in range(2, len(input_data)):
        value = input_data[i]
        if value == "":
            mappings.append((current_mappings, current_min, current_max))
            current_mappings = {}
            if current_min < global_min:
                global_min = current_min
            if current_max > global_max:
                global_max = current_max
            current_min = math.inf
            current_max = -math.inf
        elif value[0].isdigit():
            dest_range_start, source_range_start, range_length = map(int, value.split())
            source_range = range(source_range_start, source_range_start + range_length)
            dest_range = range(dest_range_start, dest_range_start + range_length)
            if source_range_start < current_min:
                current_min = source_range_start
            if source_range_start + range_length > current_max:
                current_max = source_range_start + range_length
            diff = dest_range_start - source_range_start
            current_mappings[source_range] = dest_range

    mappings.append((current_mappings, current_min, current_max))
    if current_min < global_min:
        global_min = current_min
    if current_max > global_max:
        global_max = current_max

    padded_mappings: list[dict] = []
    for mapping in mappings:
        current_padded_mappings = mapping[0]
        map_min = mapping[1]
        map_max = mapping[2]
        min_range = range(global_min, map_min)
        max_range = range(map_max, global_max)
        if min_range:
            current_padded_mappings[min_range] = min_range
        if max_range:
            current_padded_mappings[max_range] = max_range
        padded_mappings.append(current_padded_mappings)

    # Keys: source_range
    # Values: dest_range
    squashed_mapping: dict[range, range] = padded_mappings[0]
    for map_id in range(len(padded_mappings) - 1):
        first_map: dict[range, range] = squashed_mapping
        next_map: dict[range, range] = padded_mappings[map_id + 1]

        squashed_mapping: dict[range, range] = {}
        for first_source, first_dest in first_map.items():
            for next_source, next_dest in next_map.items():
                x = first_dest
                y = next_source
                overlap = range(max(x.start, y.start), min(x.stop, y.stop))

                if overlap:
                    # Find corresponding range in the first source
                    first_diff = first_dest[0] - first_source[0]
                    first_corresponding = range(
                        overlap[0] - first_diff, overlap[-1] - first_diff + 1
                    )

                    # Find the corresponding range in the next dest
                    next_diff = next_dest[0] - next_source[0]
                    next_corresponding = range(
                        overlap[0] + next_diff, overlap[-1] + next_diff + 1
                    )
                    squashed_mapping[first_corresponding] = next_corresponding

    seeds = list(map(int, input_data[0].strip("seeds: ").split()))
    seed_ranges: list[range] = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))

    inverted_squashed_mapping: dict[range, range] = {}
    for source_range, dest_range in squashed_mapping.items():
        inverted_squashed_mapping[dest_range] = source_range

    dest_ranges = inverted_squashed_mapping.keys()

    # Sorting list of ranges based on start value
    sorted_dest_ranges = sorted(dest_ranges, key=lambda r: r.start)

    for dest_range in sorted_dest_ranges:
        source_range = inverted_squashed_mapping[dest_range]

        for seed_range in seed_ranges:
            x = source_range
            y = seed_range
            overlap = range(max(x.start, y.start), min(x.stop, y.stop))
            if len(overlap):
                diff = dest_range.start - source_range.start
                return source_range.start + diff

    return None


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
