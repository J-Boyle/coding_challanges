from typing import List
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

    def remove_zeros(self, variable: List[int]) -> List[int]:
        return [num for num in variable if num != 0]

    def replace_zeros(self, variables:List[int], new_numbers: List[int]) -> List[int]:
        pass

    def find_missing_numbers(self, variable: List[int]) -> List[int]:
        return list(set([i for i in range(1, 11)]) - set(variable))

    def get_columns(self):
        return [[row[i] for row in self.puzzle] for i in range(len(self.puzzle))]

    def get_grids(self):
        grid_size = sqrt(len(self.puzzle))







    def find_possible_solutions(self, variable):

        missing_numbers = self.find_missing_numbers(variable)

        possible_solution =


    def solve_row(self) -> List[int]:
        row =
        missing_numbers =

    def solve_column(self):
        pass

    def solve_box(self):
        pass

    def size_box(self):
        pass

    def print_answer(self):
        pass

    def is_satisfied(self, variables) -> bool:
        return len(set(variables)) == len(variables)
