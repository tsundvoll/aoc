# Utility functions to load different kind of input data

def parse_input(filepath, sep=' ', data_type=int):
    with open(filepath, 'r') as f:
        data = f.read()

    return list(map(data_type, data.split(sep)))


def parse_characters_on_a_line(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    return data.strip()


def parse_lines(filepath):
    return list(map(lambda line: line.strip(), open(filepath, 'r')))
