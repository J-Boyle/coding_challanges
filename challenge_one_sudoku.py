from typing import List, Tuple, Iterator
from math import sqrt
from itertools import permutations, product
from pprint import pprint

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

        self.possible_rows = {}
        self.solution_found = False


    def replace_zeros(self, variables: List[int], new_numbers: List[int]) -> List[int]:
        return [new_numbers.pop() if i == 0 else i for i in variables]

    def find_missing_numbers(self, variable: List[int]) -> List[int]:
        return list(set([i for i in range(1, 11)]) - set(variable))

    def get_columns(self, guess) -> List[List[int]]:
        return [[row[i] for row in guess] for i in range(len(guess))]

    def get_boxes(self, guess) -> List[Tuple[int]]:

        results = []

        t = [(0,0), (0,3), (0,6),
             (3,0), (3,3), (3,6),
             (6,0), (6,3), (6,6)]

        for i in t:
            results.extend([self.get_box(i, guess)])

        return results


    def get_box(self, grid_coords: Tuple[int,int], guess) -> List[List[int]]:
        number_of_rows = int(sqrt(len(self.puzzle)))
        x1_coord = grid_coords[0]
        x2_coord = x1_coord + number_of_rows
        y_coord = grid_coords[1]

        result = [guess[y][x1_coord:x2_coord] for y in [i for i in range(y_coord + number_of_rows)][-number_of_rows:]]

        return [item for sublist in result for item in sublist]

    def generate_permutations(self, variable: List[int]) -> List[List[int]]:

        missing_numbers = self.find_missing_numbers(variable)
        missing_numbers_permutations = permutations(missing_numbers)

        return [self.replace_zeros(variable, list(permutation)) for permutation in missing_numbers_permutations]


    def populate_possible_rows(self)-> None:
        for row_count, row in enumerate(self.puzzle):
            self.possible_rows[row_count] = self.generate_permutations(row)

    def generate_guesses(self)-> Iterator:
        return product(row for row in self.possible_rows.values())


    def guess_is_correct(self, guess) -> None:
        cols = self.get_columns(guess)
        boxes = self.get_boxes(guess)

        self.solution_found = True if all([self.is_satisfied(guess), self.is_satisfied(cols), self.is_satisfied(boxes)]) else False


    def is_satisfied(self, variables: List[List[int]])-> bool:
        return all([len(set(attempt)) == len(attempt) for attempt in variables])

    def solve(self)-> List[List[int]]:
        guess_count = 0
        print('----- Starting -----')
        self.populate_possible_rows()
        print(self.generate_guesses().__next__())
        # while not self.solution_found:
        #     print(f'Attempt No: {guess_count}')
        #     guesses = self.generate_guesses()
        #     print(guesses.__next__())
        #     # self.guess_is_correct(guesses.__next__())
        #     guess_count += 1

        print(('----- Solutiuon Found -----'))



if __name__ == '__main__':
    x = SudokuSolver(sudoku_puzzle)
    x.solve()



