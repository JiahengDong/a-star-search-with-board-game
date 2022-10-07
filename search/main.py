"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.a_star import *


def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).

    # Read in the input file and extract useful information
    size = data["n"]
    occupation = data["board"]
    start = tuple(data["start"])
    goal = tuple(data["goal"])

    # Create an array to record all blocked cells
    occupation_coordinate = []
    for i in occupation:
        if i[0] == "b":
            occupation_coordinate.append(tuple(i[1:]))

    # The cost is the number of cells that form a continuous path from start to goal
    # Potentially cells are all blocked -- not valid solution
    # If there is a tie, any path is acceptable

    # The tests will run with python3.6 on student unix machines and TIME LIMITS -- 30s
    a_star_algorithm(start, goal, occupation_coordinate, size)
