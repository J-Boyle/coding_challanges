from typing import List, Tuple
from math import sqrt
from itertools import product


def get_columns(guess) -> List[List[int]]:
    return [[row[i] for row in guess] for i in range(len(guess))]


def get_box_coordinates(puzzle) -> List[Tuple[int, int]]:
    """
    coordinates are for top left corner of each "box" with 0,0 being on the top left corner
    """
    coords_numbers = [i for i in range(0, len(puzzle), int(sqrt(len(puzzle))))]
    return list(product(coords_numbers, coords_numbers[::-1]))


def get_box(grid_coords: Tuple[int, int], guess) -> List[List[int]]:
    number_of_rows = int(sqrt(len(guess)))
    x1_coord = grid_coords[0]
    x2_coord = x1_coord + number_of_rows
    y_coord = grid_coords[1]

    result = [guess[y][x1_coord:x2_coord] for y in [i for i in range(y_coord + number_of_rows)][-number_of_rows:]]

    return [item for sublist in result for item in sublist]


def get_all_boxes(guess) -> List[List[int]]:
    return [get_box(coord, guess) for coord in get_box_coordinates(guess)]


def guess_is_correct(guess: List[List[int]]) -> bool:
    cols = get_columns(guess)
    boxes = get_all_boxes(guess)

    return all([is_satisfied(guess), is_satisfied(cols), is_satisfied(boxes)])


def is_satisfied(target: List[List[int]]) -> bool:
    # target = row, col or box
    # remove 0's to stop produces false results when comparing set lengths
    result = [[number for number in row if number != 0] for row in target]

    return all([len(set(attempt)) == len(attempt) for attempt in result])


def find_empty(puzzle) -> Tuple[int, int]:
    for index_row, row in enumerate(puzzle):
        for index_number, number in enumerate(puzzle):
            if puzzle[index_row][index_number] == 0:
                return index_row, index_number

    return None


def solve(puzzle)-> bool:
    """Back tracking algorithm"""

    # Base case of recursion
    empty_position = find_empty(puzzle)
    print(empty_position)
    if not empty_position:
        # If there are no more empty positions puzzle is solved
        return True
    else:
        row, col = empty_position

    for guess in range(1, 10):  # todo make this dynamic
        puzzle[row][col] = guess
        if guess_is_correct(puzzle):
            print('correct guess')
            print(puzzle)
            if solve(puzzle):
                return True

            puzzle[row][col] = 0
            print('backtracking...')

    return False


def print_result(result: List[List[int]]) -> None:
    print(*[row for row in result], sep='\n')
    print('------')


if __name__ == '__main__':
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
        print_result(sudoku_puzzle)
    else:
        print('No Solution Found')
        print_result(sudoku_puzzle)
