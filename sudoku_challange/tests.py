import pytest
from sudoku_challange.sudoku import SudokuSolver


@pytest.fixture
def question():
    return [
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


@pytest.fixture
def answer():
    return [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]


@pytest.fixture
def solver_with_question(question):
    return SudokuSolver(question)


@pytest.fixture
def solver_with_answer(answer):
    return SudokuSolver(answer)


def test_guess_is_correct(solver_with_answer, answer):
    solver_with_answer.guess_is_correct(answer)
    assert solver_with_answer.solution_found == True


def test_solver_with_answer(solver_with_answer):
    solver_with_answer.solve()


def test_solver_with_question(solver_with_question):
    solver_with_question.solve()


def test_print_result(solver_with_answer, answer):
    solver_with_answer.print_result(answer)


def test_get_box_coordinates(solver_with_answer, answer):
    answer = [(0, 6), (0, 3), (0, 0), (3, 6), (3, 3), (3, 0), (6, 6), (6, 3), (6, 0)]
    assert solver_with_answer.get_box_coordinates() == answer


def test_get_boxes(solver_with_answer, answer):
    answer = [[1, 7, 9, 2, 8, 6, 3, 4, 5],
              [6, 3, 5, 4, 1, 9, 2, 8, 7],
              [2, 8, 4, 5, 3, 7, 9, 6, 1],
              [8, 5, 6, 9, 2, 4, 7, 1, 3],
              [7, 9, 1, 8, 5, 3, 4, 2, 6],
              [4, 2, 3, 7, 6, 1, 8, 5, 9],
              [5, 6, 7, 3, 4, 2, 1, 9, 8],
              [3, 4, 8, 1, 9, 5, 6, 7, 2],
              [9, 1, 2, 6, 7, 8, 5, 3, 4]]
    assert solver_with_answer.get_boxes(answer) == answer
