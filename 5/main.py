from dataclasses import dataclass
from typing import List, Tuple, overload
import itertools

@dataclass
class Point:
    x: int
    y: int
    
    def __key(self):
        return (self.x, self.y)
    
    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__key() == other.__key()
        return NotImplemented


@dataclass
class VentLine:
    point1: Point
    point2: Point
    vertical: bool = False

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.vertical = point1.x == point2.x
        if (self.vertical and point1.y > point2.y) \
            or (not self.vertical and point1.x > point2.x):
            self.point2 = point1
            self.point1 = point2


    def crossing_point(self, other) -> Point:
        """
        Returns point where two lines cross.
        """
        if self.vertical == other.vertical:
            return None
        if self.vertical:
            if other.point1.y >= self.point1.y and other.point2.y <= self.point2.y:
                return Point(self.point1.x, other.point1.y)
            else:
                return None
        elif not self.vertical:
            if self.point1.x <= other.point1.x and self.point2.x >= other.point2.x:
                return Point(other.point1.x, self.point1.y)
            else:
                return None

    def overlap_point(self, other) -> Point:
        """
        Returns the point where the two lines overlap.
        """
        if self.vertical == other.vertical:
            return None
        if self.vertical:
            if other.point1.y >= self.point1.y and other.point2.y <= self.point2.y:
                return Point(self.point1.x, other.point1.y)
            else:
                return None
        elif not self.vertical:
            if self.point1.x <= other.point1.x and self.point2.x >= other.point2.x:
                return Point(other.point1.x, self.point1.y)
            else:
                return None

def get_input() -> List[VentLine]:
    with open('5/input') as file:
        lines = file.readlines()
    ventlines = []
    for line in lines:
        points = line.strip('\n').split(' -> ')
        points = [p.split(',') for p in points]
        ventlines.append(
            VentLine(
                Point(
                    int(points[0][0]),
                    int(points[0][1])
                ),
                Point(
                    int(points[1][0]),
                    int(points[1][1])
                )
            )
        )
    return ventlines


def part1():
    ventlines = get_input()
    overlaps = set()
    for v1, v2 in itertools.pairwise(ventlines):
        if overlap_point := v1.crossing_point(v2):
            overlaps.add(overlap_point)
    return len(overlaps)

def main():
    print(f'{part1()=}')

if __name__ == '__main__':
    main()