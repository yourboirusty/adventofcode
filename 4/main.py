from pprint import pprint
from dataclasses import dataclass
from typing import List

@dataclass
class Board:
    numbers: List[List[int]]
    matches: List[List[bool]]
    last_number: int
    won: bool = False

    def __init__(self, numbers: List[List[int]]):
        self.numbers = numbers
        self.matches = [[False for _ in range(len(numbers))] for _ in range(len(numbers))]

    def cross_matches(self, new_number: int):
        #Check if the new numbers are a match
        if self.won:
            return
        self.last_number = new_number
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i][j] == new_number:
                    self.matches[i][j] = True

    def check_diagonal(self):
        #Check if there is a match in the diagonals
        for i in range(len(self.numbers)):
            if not self.matches[i][i] and not self.matches[i][len(self.numbers) - 1 - i]:
                return False
        return True

    def check_rows(self):
        #Check if there is a match in the rows
        for row in self.matches:
            if all(row):
                return True
        return False

    def check_columns(self):
        #Check if there is a match in the columns
        transposed = map(list, zip(*self.matches))
        for column in transposed:
            if all(column):
                return True
        return False

    def check_match(self):
        #Check if there is a match in the board
        if self.won:
            return False
        if self.check_rows() or self.check_columns():
            self.won = True
            return True
        return False

    def get_score(self):
        correct  = 0
        incorrect = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.matches[i][j]:
                    correct += self.numbers[i][j]
                else:
                    incorrect += self.numbers[i][j]
        print(f"Correct: {correct} Incorrect: {incorrect}")
        return self.last_number * incorrect

    def print_numbers(self):
        for row in self.numbers:
            print(row)

    def print_matches(self):
        for row in self.matches:
            print(list(map(lambda x: "X" if x else "O", row)))

def get_input():
    with open('input') as f:
        numbers = f.readline().strip('\n').split(',')
        numbers = list(map(int, numbers))
        boards_lines = [board for board in f.readlines()]

    boards = []
    for line in boards_lines:
        if line == '\n':
            boards.append([])
            continue
        boards[-1].append([int(item) for item in line.split(' ') if not item in ['', '\n']])

    return numbers, boards


def part1():
    numbers, boards = get_input()
    board_objs = []
    for board in boards:
        board_objs.append(Board(board))

    for number in numbers:
        for board in board_objs:
            board.cross_matches(number)
            if board.check_match():
                board.print_matches()
                return board.get_score()

def part2():
    numbers, boards = get_input()
    board_objs = []
    for board in boards:
        board_objs.append(Board(board))

    last_good_board = None
    for number in numbers:
        for board in board_objs:
            board.cross_matches(number)
            if board.check_match():
                last_good_board = board
    last_good_board.print_matches()
    return last_good_board.get_score()
    
def main():
    print(f'{part1()=}')
    print(f'{part2()=}')

if __name__ == '__main__':
    main()