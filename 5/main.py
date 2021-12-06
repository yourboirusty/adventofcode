from dataclasses import dataclass
from typing import List, Tuple, overload
import itertools

@dataclass
class VentLine:
    x1: int
    y1: int
    x2: int
    y2: int
    diag: bool = False

    def __init__(self, point1, point2, *, diag=False):
        self.x1 = point1[0]
        self.x2 = point2[0]
        self.y1 = point1[1]
        self.y2 = point2[1]
        self.diag = diag

    def yield_line_points(self) -> Tuple[int, int]:
        """
        Yields each point in line from p1 to p2, vertical, horizontal or diagonal
        """
        if self.x1 == self.x2:
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                yield (self.x1, y)
        elif self.y1 == self.y2:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                yield (x, self.y1)
        elif self.diag:
            x_dir = 1 if self.x1 < self.x2 else -1
            y_dir = 1 if self.y1 < self.y2 else -1
            for x, y in zip(
                            range(self.x1, self.x2 + x_dir, x_dir),
                            range(self.y1, self.y2 + y_dir, y_dir)
                        ):
                yield (x, y)

    def line_points(self) -> List[Tuple[int, int]]:
        """
        Returns a list of all points in line from p1 to p2, vertical, horizontal or diagonal
        """
        return list(self.yield_line_points())
        
    def get_intersection(self, other) -> Tuple[int, int]:
        """
        Returns the intersection point between two lines
        """
        return list(
            set(self.line_points()).intersection(set(other.line_points()))
        )
        
        
def get_input(diag = False) -> List[VentLine]:
    with open('5/input') as file:
        lines = file.readlines()
    ventlines = []
    for line in lines:
        points = line.strip('\n').split(' -> ')
        points = [p.split(',') for p in points]
        ventlines.append(
            VentLine(
                (
                    int(points[0][0]),
                    int(points[0][1])
                ),
                (
                    int(points[1][0]),
                    int(points[1][1])
                ),
                diag = diag
            )
        )
    return ventlines


def part1():
    ventlines = get_input()
    overlaps = set()
    for v1, v2 in itertools.combinations(ventlines, 2):
        for intersections in v1.get_intersection(v2):
            overlaps.add(intersections)

    return len(overlaps)


def part2():
    ventlines = get_input(diag = True)
    overlaps = set()
    for v1, v2 in itertools.combinations(ventlines, 2):
        for intersections in v1.get_intersection(v2):
            overlaps.add(intersections)

    return len(overlaps)

def main():
    # print(f'{part1()=}')
    print(f'{part2()=}')

if __name__ == '__main__':
    main()