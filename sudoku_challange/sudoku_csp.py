from csp import Constaint
from typing import List, Dict, Tuple
from math import sqrt
from itertools import product

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

variables: List[List[int]] = sudoku_puzzle

domains: Dict[List[int], List[int]] = {}

for variable in variables:
    domains[variable] = [i for i in range(0,11)]

class SudokuConstraint(Constaint):

    def get_columns(self) -> List[List[int]]:
        return [[row[i] for row in self.variables] for i in range(len(self.variables))]

    def get_box_coordinates(self) -> List[Tuple[int, int]]:
        """
        coordinates are for top left corner of each "box" with 0,0 being on the top left corner
        """
        coords_numbers = [i for i in range(0, len(self.variables), int(sqrt(len(self.variables))))]
        return list(product(coords_numbers, coords_numbers[::-1]))

    def get_box(self, grid_coords: Tuple[int, int], guess) -> List[List[int]]:
        number_of_rows = int(sqrt(len(self.variables)))
        x1_coord = grid_coords[0]
        x2_coord = x1_coord + number_of_rows
        y_coord = grid_coords[1]

        result = [guess[y][x1_coord:x2_coord] for y in [i for i in range(y_coord + number_of_rows)][-number_of_rows:]]

        return [item for sublist in result for item in sublist]

    def get_boxes(self, guess) -> List[List[int]]:
        return [self.get_box(coord, guess) for coord in self.get_box_coordinates()]

    def satisfied(self, assignment: Dict[V, D]) -> bool:
        pass
