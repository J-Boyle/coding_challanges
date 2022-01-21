import pytest
from sudoku_challange.sudoku_solver import get_columns, get_box_coordinates, get_box, get_all_boxes, guess_is_correct, \
    is_satisfied, find_empty_position


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
def wrong_answer():
    return [
        [5, 3, 7, 0, 7, 0, 0, 0, 0],
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


def test_get_columns(question):
    answer = [[5, 6, 0, 8, 4, 7, 0, 0, 0],
              [3, 0, 9, 0, 0, 0, 6, 0, 0],
              [0, 0, 8, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 8, 0, 0, 4, 0],
              [7, 9, 0, 6, 0, 2, 0, 1, 8],
              [0, 5, 0, 0, 3, 0, 0, 9, 0],
              [0, 0, 0, 0, 0, 0, 2, 0, 0],
              [0, 0, 6, 0, 0, 0, 8, 0, 7],
              [0, 0, 0, 3, 1, 6, 0, 5, 9]]
    assert get_columns(question) == answer

def test_get_box_coordinates(question):
    assert get_box_coordinates(question) == [(0, 6), (0, 3), (0, 0), (3, 6), (3, 3), (3, 0), (6, 6), (6, 3), (6, 0)]

def test_get_box(question):
    assert get_box((3,3), question) == [0, 6, 0, 8, 0, 3, 0, 2, 0]

def test_get_all_boxes(question):
    answer = [[0, 6, 0, 0, 0, 0, 0, 0, 0],
              [8, 0, 0, 4, 0, 0, 7, 0, 0],
              [5, 3, 0, 6, 0, 0, 0, 9, 8],
              [0, 0, 0, 4, 1, 9, 0, 8, 0],
              [0, 6, 0, 8, 0, 3, 0, 2, 0],
              [0, 7, 0, 1, 9, 5, 0, 0, 0],
              [2, 8, 0, 0, 0, 5, 0, 7, 9],
              [0, 0, 3, 0, 0, 1, 0, 0, 6],
              [0, 0, 0, 0, 0, 0, 0, 6, 0]]
    assert get_all_boxes(question) == answer

def test_is_not_satisfied(wrong_answer):
    assert is_satisfied(wrong_answer) == False

def test_is_satisfied(answer):
    assert is_satisfied(answer) == True

def test_guess_is_incorrect(question):
    assert guess_is_correct(3, question, 0,2) == False

def test_guess_is_correct(question):
    assert guess_is_correct(1, question, 0,2) == True

def test_find_empty(question):
    assert find_empty_position(question) == (0, 2)

def test_find_empty_complete(answer):
    assert find_empty_position(answer) == None



