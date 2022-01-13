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
        self.possible_rows: List = []

    def replace_zeros(self, variables: List[int], new_numbers: List[int]) -> List[int]:
        return [new_numbers.pop() if i == 0 else i for i in variables]

    def find_missing_numbers(self, variable: List[int]) -> List[int]:
        return list(set([i for i in range(1, 11)]) - set(variable))

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

    def generate_permutations(self, variable: List[int]) -> List[List[int]]:
        missing_numbers = self.find_missing_numbers(variable)
        missing_numbers_permutations = permutations(missing_numbers)
        return [self.replace_zeros(variable, list(permutation)) for permutation in missing_numbers_permutations]

    def populate_possible_rows(self) -> None:
        # for row_count, row in enumerate(self.puzzle):
        #     self.possible_rows[row_count] = self.generate_permutations(row)
        for row in self.puzzle:
            self.possible_rows.append(self.generate_permutations(row))


variables: List[int] = [i for row in sudoku_puzzle for i in row]
#[5, 3, 0, 0, 7, 0, 0, 0, 0, 6, 0, 0, 1, 9, 5, 0, 0, .....] all numbers in the puzzle

domains: Dict[int, List[int]] = {}

for variable in variables:
    domains[variable] = [i for i in range(1,11)] #[1,2,3,4,5,6,7,8,9,10] all possible values for each variable


class SudokuConstraint(Constaint):

    def __init__(self, variables):
        super().__init__([variables])


    def satisfied(self, assignment: Dict[V, D]) -> bool:
        if variables != 0: #we only want to target the zeros
            return True

        #add function to unflatten the list and then check rows, cols and boxes for duplicate numbers greater than 3

def nest_flat_list():
    pass





if __name__ == '__main__':
    pass