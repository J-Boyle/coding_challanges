from typing import List, Tuple, Optional
from math import sqrt
from itertools import product
from time import time


def get_columns(puzzle: List[List[int]]) -> List[List[int]]:
    return [[row[i] for row in puzzle] for i in range(len(puzzle))]


def get_box_coordinates(puzzle: List[List[int]]) -> List[Tuple[int, int]]:
    # coordinates are for top left corner of each "box" with 0,0 being on the top left corner
    coords_numbers = [i for i in range(0, len(puzzle), int(sqrt(len(puzzle))))]
    return list(product(coords_numbers, coords_numbers[::-1]))


def get_box(grid_coords: Tuple[int, int], puzzle: List[List[int]]) -> List[int]:
    number_of_rows = int(sqrt(len(puzzle)))
    x1_coord = grid_coords[0]
    x2_coord = x1_coord + number_of_rows
    y_coord = grid_coords[1]

    result = [puzzle[y][x1_coord:x2_coord] for y in [i for i in range(y_coord + number_of_rows)][-number_of_rows:]]

    return [item for sublist in result for item in sublist]


def get_all_boxes(puzzle: List[List[int]]) -> List[List[int]]:
    return [get_box(coord, puzzle) for coord in get_box_coordinates(puzzle)]


def guess_is_correct(guess: int, puzzle: List[List[int]], row: int, col: int) -> bool:
    puzzle[row][col] = guess

    cols = get_columns(puzzle)
    boxes = get_all_boxes(puzzle)

    # checking guess works will all cols, rows and boxes
    # potential speed up could be to only check row, col and box of guess position?
    return all([is_satisfied(puzzle), is_satisfied(cols), is_satisfied(boxes)])


def is_satisfied(target: List[List[int]]) -> bool:
    # target can be row, col or box

    # remove 0's to stop produces false results when comparing set lengths
    result = [[number for number in row if number != 0] for row in target]

    # if the sets of the attempt are the same length as the list of the attempt
    # there can be no duplicate numbers and must be satisfied
    return all([len(set(attempt)) == len(attempt) for attempt in result])


def find_empty_position(puzzle: List[List[int]]) -> Optional[Tuple[int, int]]:
    puzzle_range = len(puzzle)
    for row in range(0, puzzle_range):
        for col in range(0, puzzle_range):
            if puzzle[row][col] == 0:
                return row, col
    return None


def solve(puzzle: List[List[int]]) -> bool:
    # Back tracking recursive algorithm

    # Base case of recursion
    empty_position = find_empty_position(puzzle)
    if not empty_position:
        # If there are no more empty positions puzzle is solved
        return True
    else:
        row, col = empty_position

    # Loop through all possible values for position row, col
    for guess in range(1, len(puzzle) + 1):
        if guess_is_correct(guess, puzzle, row, col):
            # If guess is correct (True), then set that value and recurse
            # on the updated puzzle to solve the next empty value
            puzzle[row][col] = guess
            if solve(puzzle):
                return True
        # if NOT correct (False), reset position value to 0 and backtrack
        puzzle[row][col] = 0

    return False


def print_result(result: List[List[int]]) -> None:
    print(*[row for row in result], sep='\n')


if __name__ == '__main__':
    start = time()
    sudoku_puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve(sudoku_puzzle):
        finished = time()
        print(f'Time: {round((finished - start), 2)}s')
        print_result(sudoku_puzzle)
    else:
        print('No Solution Found')
