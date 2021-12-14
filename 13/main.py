from typing import List, Tuple

def get_data(input_file: str = '13/input') -> Tuple[List[Tuple[int, int]], List[Tuple[str, int]]]:
    with open(input_file) as f:
        data = f.read().split('\n')

    dots = []
    folds = []
    
    while line := data.pop(0):
        if line == '':
            break
        dots.append(tuple(map(int, line.split(','))))

    for line in data:
        line = line.split('=')
        folds.append(
                (
                line[0][-1],
                int(line[1])
                )
        )    
    return dots, folds

class Sheet:
    dots: List[List[bool]]
    folds: List[Tuple[str, int]]


    def __str__(self):
        return self.board_to_str(self.dots)
    
    @staticmethod
    def board_to_str(board: List[List[bool]]):
        return '\n'.join(
                ''.join('█' if dot else '.' for dot in row)
                for row in board
            )

    def __init__(self, dots: List[Tuple[int, int]], folds: List[Tuple[int, int]]):
        x_max = max(x for x, y in dots)
        y_max = max(y for x, y in dots)

        self.dots = [[False for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in dots:
            self.dots[y][x] = True

        self.folds = folds

    def fold(self):
        fold = self.folds.pop(0)
        print(fold)
        if fold[0] == 'x':
            self.fold_x(fold[1])
        elif fold[0] == 'y':
            self.fold_y(fold[1])

    def fold_x(self, axis: int):
        """
        Transfers dots from right of the axis to the left of the axis.
        """
        right, left = self.split_by_x_axis(axis)
        for x in range(len(right[0])):
            for y in range(len(right)):
                left[y][-x-1] = left[y][-x-1] or right[y][x]

        self.dots = left

    def fold_y(self, axis: int):
        """
        Transfers dots from below the axis to the above the axis.
        """
        below, above = self.split_by_y_axis(axis)
        for x in range(len(below[0])):
            for y in range(len(below)):
                above[-y-1][x] = above[-y-1][x] or below[y][x]
        self.dots = above

    def solve_part1(self):
        self.fold()
        return sum(sum(row) for row in self.dots)

    def fold_all(self):
        while self.folds:
            self.fold()
            

    def split_by_x_axis(self, axis: int) -> Tuple[List[List[bool]], List[List[bool]]]:
        left = []
        right = []
        for row in self.dots:
            left.append(row[:axis])
            right.append(row[axis+1:])
        return right, left

    def split_by_y_axis(self, axis: int) -> Tuple[List[List[bool]], List[List[bool]]]:
        above = self.dots[:axis]
        below = self.dots[axis+1:]
        
        return below, above

    @staticmethod
    def mirror_x(board: List[List[bool]]) -> List[List[bool]]:
        return [list(reversed(row)) for row in board]

    @staticmethod
    def mirror_y(board: List[List[bool]]) -> List[List[bool]]:
        return list(reversed(board))


if __name__ == '__main__':
    dots, folds = get_data()
    sheet = Sheet(dots, folds)
    sheet.fold_all()
    print(sheet)