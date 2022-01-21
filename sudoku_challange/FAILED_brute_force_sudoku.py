from typing import List, Tuple, Iterator
from math import sqrt
from itertools import permutations, product

#####################################################
# This is a FAILED brute force attempt the iterates #
# through every permutation possible until it finds #
# one that works.                                   #
#                                                   #
# This was until I realised that there are approx   #
# 9^81 different permutations!!                     #
#####################################################


class SudokuSolver:

    def __init__(self,
                 puzzle: List[List[int]]):
        self.puzzle = puzzle

        self.possible_rows:dict = {}
        self.solution_found: bool = False

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
        for row_count, row in enumerate(self.puzzle):
            self.possible_rows[row_count] = self.generate_permutations(row)

    def generate_guesses(self) -> Iterator:
        return product(*[row for row in self.possible_rows.values()])

    def guess_is_correct(self, guess: List[List[int]]) -> None:
        cols = self.get_columns(guess)
        boxes = self.get_boxes(guess)

        self.solution_found = all([self.is_satisfied(guess), self.is_satisfied(cols), self.is_satisfied(boxes)])

    def is_satisfied(self, variables: List[List[int]]) -> bool:
        return all([len(set(attempt)) == len(attempt) for attempt in variables])

    def print_result(self, result: List[List[int]]) -> None:
        print(*[row for row in result], sep='\n')

    def solve(self) -> None:
        guess_count = 0
        guess = []
        print('----- Starting -----')
        self.populate_possible_rows()
        guesses = self.generate_guesses()
        while not self.solution_found:
            guess_count += 1
            print(f'Attempt No: {guess_count}')
            guess = guesses.__next__()
            self.guess_is_correct(guess)

        print(('----- Solutiuon Found -----'))
        self.print_result(guess)


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
    x = SudokuSolver(sudoku_puzzle)
    x.solve()
