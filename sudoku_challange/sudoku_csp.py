from csp import Constaint
from typing import List, Dict, Tuple, TypeVar
from math import sqrt
from itertools import product, permutations, chain

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

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type



class SudokuUtility:

    def __init__(self,
                 puzzle: List[List[int]]):
        self.puzzle = puzzle
        self.possible_numbers = [i for i in range(1,10)]

    def get_columns(self, guess) -> List[List[int]]:
        return [[row[i] for row in guess] for i in range(len(guess))]

    def get_box_coordinates(self) -> List[Tuple[int, int]]:
        """
        coordinates are for top left corner of each "box" with 0,0 being on the top left corner
        """
        coords_numbers = [i for i in range(0, len(self.puzzle), int(sqrt(len(self.puzzle))))]
        return list(product(coords_numbers, coords_numbers[::-1]))

    def get_box(self, grid_coords: Tuple[int, int], guess) -> List[List[int]]:
        number_of_rows = int(sqrt(len(self.puzzle)))
        x1_coord = grid_coords[0]
        x2_coord = x1_coord + number_of_rows
        y_coord = grid_coords[1]

        result = [guess[y][x1_coord:x2_coord] for y in [i for i in range(y_coord + number_of_rows)][-number_of_rows:]]

        return [item for sublist in result for item in sublist]

    def get_boxes(self, guess) -> List[List[int]]:
        return [self.get_box(coord, guess) for coord in self.get_box_coordinates()]

    def guess_is_correct(self, guess: List[List[int]]) -> bool:
        cols = self.get_columns(guess)
        boxes = self.get_boxes(guess)

        return all([self.is_satisfied(guess), self.is_satisfied(cols), self.is_satisfied(boxes)])

    def is_satisfied(self, variables: List[List[int]]) -> bool:

        result = [[number for number in row if number!=0] for row in variables]

        return all([len(set(attempt)) == len(attempt) for attempt in result])

    def solve(self, puzzle: List[List[int]] = None):
        local_puzzle = puzzle.copy()
        for index_row, row in enumerate(local_puzzle):
            for index_number, number in enumerate(local_puzzle):
                if local_puzzle[index_row][index_number] == 0:
                    for guess in self.possible_numbers:
                        local_puzzle[index_row][index_number] = guess
                        if self.guess_is_correct(local_puzzle):
                            print('guess is correct')
                            result = self.solve(local_puzzle)
                            self.print_result(local_puzzle)
                            if result is not None:
                                return result
                        else:
                            print('guess is incorrect')
        return None


    def print_result(self, result: List[List[int]]) -> None:
        print(*[row for row in result], sep='\n')
        print('------')


if __name__ == '__main__':
    test = SudokuUtility(sudoku_puzzle)
    x = test.solve(sudoku_puzzle)
    if x is None:
        print('No Solution Found')
    else:
        x.print_result()

