def read_line_separated_integers(path):
    file_path = str(path) + "/input.txt"

    with open(file_path, 'r') as f:
        data = f.readlines()

    for i in range(len(data)):
        data[i] = int(data[i].strip('\n'))
    return data