from main import Board, get_input
import random
from unittest.mock import mock_open, patch
import pytest

example_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_wins = [
    [1,5,9],
    [7,5,3]
]


horizontal_wins = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

vertical_wins = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

mock_file = f"""{",".join(map(str, vertical_wins[0]))}

1 2  3
4 5 6
 7 8 9
"""

def test_read_file():
    m = mock_open(read_data=mock_file)
    with patch('builtins.open', m):
        numbers, boards = get_input()
    assert numbers == vertical_wins[0]
    assert boards[0] == [[1,2,3],[4,5,6],[7,8,9]]

@pytest.mark.parametrize('diagonal_input', [
    *diagonal_wins,
    ])
def test_diagonal_win(diagonal_input):
    board = Board(example_numbers)
    random
    for number in diagonal_input:
        board.cross_matches(number)
    assert board.check_diagonal()
    # assert board.check_match()

def test_cross_matches():
    board = Board(example_numbers)
    board.cross_matches(5)
    assert board.matches[1][1] == True

@pytest.mark.parametrize('horizontal_win', [
    *horizontal_wins,
    ])
def test_horizontal_win(horizontal_win):
    board = Board(example_numbers)
    random.shuffle(horizontal_win)
    for number in horizontal_win:
        board.cross_matches(number)
    assert board.check_rows()

@pytest.mark.parametrize('vertical_win', [
    *vertical_wins,
    ])
def test_vertical_win(vertical_win):
    board = Board(example_numbers)
    random.shuffle(vertical_win)
    for number in vertical_win:
        board.cross_matches(number)
    assert board.check_columns()

@pytest.mark.parametrize('numbers', [
    *vertical_wins,
    *horizontal_wins,
])
def test_match_win(numbers):
    board = Board(example_numbers)
    random.shuffle(numbers)
    for number in numbers:
        board.cross_matches(number)
    assert board.check_match()

def test_score_win():
    board = Board(example_numbers)
    for number in horizontal_wins[0]:
        board.cross_matches(number)
    assert board.check_match()
    assert board.get_score() == (1 + 2 + 3) * (4 + 5 + 6 + 7 + 8 + 9)
