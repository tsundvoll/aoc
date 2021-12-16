import argparse
import importlib
from datetime import datetime


def main():

    today = datetime.now()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--year',
        help='Specify Advent of Code event year',
        dest='year',
        default=today.year
    )
    parser.add_argument(
        '--day',
        help='Specify which day to automate',
        dest='day',
        default=today.day
    )

    args = parser.parse_args()

    day = args.day
    year = args.year

    print('#############')
    print(f'Solving challenge from {year}-12-{day}')

    if year == 2021:
        day_solution = importlib.import_module('day_' + str(day) + '.solution')
    else:
        day_solution = importlib.import_module(
            f'year_{year}_day_{day}.solution')

    day_solution.run_day()
