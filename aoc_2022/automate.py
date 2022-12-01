import argparse
import os
import time
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv
from requests.exceptions import ConnectionError


def give_intel_on_input(input_data):
    n_lines = len(input_data)
    min_line_length = len(input_data[0])
    max_line_length = len(input_data[0])
    n_digit_lines = 0
    n_alphabetic_lines = 0
    for line in input_data:
        length = len(line)
        if length < min_line_length:
            min_line_length = length
        if length > max_line_length:
            max_line_length = length

        if line.isdigit():
            n_digit_lines += 1

        if line.isalpha():
            n_alphabetic_lines += 1

    if n_lines == n_digit_lines:
        line_type = 'digits'
    elif n_lines == n_alphabetic_lines:
        line_type = 'alphabetic'
    else:
        line_type = 'mix'

    L_COL = 30
    R_COL = 30

    example_lines = [
        (input_data[i] if len(input_data) > i else '').rjust(R_COL)
        for i in range(4)
    ]

    EXAMPLE_LINE_LENGTH = 40
    example_lines = [
        (line[:EXAMPLE_LINE_LENGTH] + '..') if len(line) > EXAMPLE_LINE_LENGTH else line
        for line in example_lines
    ]


    print('##############')
    print('Intel on input')
    print('##############')
    print(f'Number of lines: {n_lines}'.ljust(L_COL),example_lines[0])
    print(f'Min line length: {min_line_length}'.ljust(L_COL), example_lines[1])
    print(f'Max line length: {max_line_length}'.ljust(L_COL),example_lines[2])
    print(f'Line type: {line_type}'.ljust(L_COL), example_lines[3])



def setup_day(year, day):
    # Create today's directory
    dirname = os.path.join(os.path.dirname(__file__), 'src/')
    day_name = f'{year}_day_{day}'
    day_directory = os.path.join(dirname, day_name)
    if not os.path.isdir(day_directory):
        os.mkdir(day_directory)

    # Create today's init file
    filename = os.path.join(day_directory, '__init__.py')
    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            f.write('')

    template_directory = os.path.join(os.path.dirname(__file__), 'template/')
    # Create today's solution file
    filename = os.path.join(day_directory, 'solution.py')
    if not os.path.isfile(filename):
        template_solution = os.path.join(template_directory, 'solution.py')
        with open(template_solution, 'r') as template:
            with open(filename, 'w') as file:
                for line in template:
                    file.write(line)

    # Create today's test file
    filename = os.path.join(day_directory, 'tests.py')
    if not os.path.isfile(filename):
        template_tests = os.path.join(template_directory, 'tests.py')
        with open(template_tests, 'r') as template:
            with open(filename, 'w') as file:
                for line in template:
                    file.write(line)


def download_input(year, day):
    print(f'Downloading input for {year}-12-{day}')

    dirname = os.path.join(os.path.dirname(__file__), 'src/')
    day_name = f'{year}_day_{day}'
    day_directory = os.path.join(dirname, day_name)

    # Download today's input data
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    session = requests.Session()
    cookie = os.getenv('AOC_SESSION_COOKIE')
    headers = {'session': cookie}
    try:
        # Create today's input txt file
        filename = os.path.join(day_directory, 'input.txt')
        if os.path.isfile(filename):
            raise RuntimeError(f'File {filename} already exists')
        result = session.get(url, cookies=headers)
        with open(filename, 'w') as file:
            file.write(result.text)
        input_data = list(map(lambda line: line.strip(), open(filename, 'r')))
        give_intel_on_input(input_data)
        print(f'Input for {year}-12-{day} downloaded')
    except ConnectionError:
        print(f'Could not download input data')


if __name__ == '__main__':
    load_dotenv()

    time_now = datetime.now()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-y', '--year',
        help='Specify Advent of Code event year',
        dest='year',
        default=time_now.year
    )
    parser.add_argument(
        '-d', '--day',
        help='Specify which day to automate',
        dest='day',
        default=time_now.day
    )

    args = parser.parse_args()
    year = int(args.year)
    day = int(args.day)

    # Create the folder and files without requesting the input endpoint
    setup_day(year, day)

    start_time = datetime(year, 12, day, 6, 0, 0, 0)

    fastest_count_time = start_time - timedelta(minutes=1)
    faster_count_time = start_time - timedelta(minutes=5)
    fast_count_time = start_time - timedelta(hours=1)

    while time_now < start_time:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Waiting for challenge to be released at {start_time}')
        time_now = datetime.now()
        print('Time:', time_now)
        if time_now >= start_time - timedelta(minutes=1):
            sleep_time = 0.1   # Every tenths of a second
        elif time_now >= faster_count_time:
            sleep_time = 1     # Every second
        elif time_now >= fast_count_time:
            sleep_time = 10    # Every 10 seconds
        else:
            sleep_time = 60    # Every minute

        time.sleep(sleep_time)

    download_input(year, day)
