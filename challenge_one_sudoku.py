import itertools
from typing import List, Tuple
from math import sqrt
from random import shuffle
from itertools import permutations

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


class SudokuSolver:

    def __init__(self,
                 puzzle: List[List[int]]):
        self.puzzle = puzzle

        self.possible_rows = []
        self.possible_columns = []
        self.possible_boxes = []

    def replace_zeros(self, variables: List[int], new_numbers: List[int]) -> List[int]:
        return [new_numbers.pop() if i == 0 else i for i in variables]

    def find_missing_numbers(self, variable: List[int]) -> List[int]:
        return list(set([i for i in range(1, 11)]) - set(variable))

    def get_columns(self) -> List[List[int]]:
        return [[row[i] for row in self.puzzle] for i in range(len(self.puzzle))]

    def get_boxes(self) -> List[List[int]]:

        results = []

        t = [(0,0), (0,3), (0,6),
             (3,0), (3,3), (3,6),
             (6,0), (6,3), (6,6)]

        for i in t:
            results.extend([self.get_box(i)])

        return results


    def get_box(self, grid_coords: Tuple[int,int]):
        number_of_rows = int(sqrt(len(self.puzzle)))
        x1_coord = grid_coords[0]
        x2_coord = x1_coord + number_of_rows
        y_coord = grid_coords[1]

        result = [self.puzzle[y][x1_coord:x2_coord] for y in [i for i in range(y_coord + number_of_rows)][-number_of_rows:]]

        return [item for sublist in result for item in sublist]



    def generate_permutations(self, variable: List[List[int]]) -> List[List[int]]:
        results = []

        for target in variable:

            missing_numbers = self.find_missing_numbers(target)
            missing_numbers_permutations = permutations(missing_numbers)

            results.extend([self.replace_zeros(target, list(permutation)) for permutation in missing_numbers_permutations])

        return results

    def populate_possible_options(self):
        self.possible_rows = self.generate_permutations(self.puzzle)
        self.possible_columns = self.generate_permutations(self.get_columns())
        self.possible_boxes = self.generate_permutations(self.get_boxes())

    def solve(self):

        self.populate_possible_options()

        for row_i in self.possible_rows:
            for col_i in self.possible_columns:
                pass

    def is_satisfied(self, variables) -> bool:
        return len(set(variables)) == len(variables)


if __name__ == '__main__':
    x = SudokuSolver(sudoku_puzzle)
    x.populate_possible_options()
    print(x.possible_boxes)


