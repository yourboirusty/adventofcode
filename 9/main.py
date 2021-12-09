from typing import List, Tuple, Set
from math import prod
def get_data(file = '9/input') -> List[List[int]]:
    with open(file) as f:
        data = f.readlines()
    height_map = [ [] for _ in range(len(data)) ]    
    for idx, char in enumerate(data):
        height_map[idx] += list(map(int, char.strip()))
    return height_map


def check_low_point(height_map: List[List[int]], x: int, y: int) -> bool:
    comparisons = []
    if x > 0:
        comparisons.append(height_map[y][x-1])
    if y < len(height_map) - 1:
        comparisons.append(height_map[y+1][x])    
    if x < len(height_map[y]) - 1:
        comparisons.append(height_map[y][x+1])
    if y > 0:
        comparisons.append(height_map[y-1][x])
        
    for comparison in comparisons:
        if comparison <= height_map[y][x]:
            return False
    return True

def check_basin(height_map: List[List[int]], x: int, y: int, basins: List[Set[Tuple[int, int]]]):
    if x < 0 or y < 0 or x >= len(height_map[0]) or y >= len(height_map):
        return False
    if height_map[y][x] == 9:
        return False
    if any(map(lambda basin: (x, y) in basin, basins)):
        return False
    basins[-1].add((x, y))
    check_basin(height_map, x-1, y, basins)
    check_basin(height_map, x, y-1, basins)
    check_basin(height_map, x+1, y, basins)
    check_basin(height_map, x, y+1, basins)
    return True

def part1(height_map: List[List[int]]):
    risk_level = 0
    for y, row in enumerate(height_map):
        for x, height in enumerate(row):
            if check_low_point(height_map, x, y):
                risk_level += 1+height
    return risk_level            
    
def part2(height_map: List[List[int]]):
    basins = [set()]
    for y, row in enumerate(height_map):
        for x, height in enumerate(row):
            if check_basin(height_map, x, y, basins):
                basins.append(set())

    basin_lens = [len(basin) for basin in basins]
    basin_lens.sort()
    return prod(basin_lens[-3:])

if __name__ == '__main__':
    height_map = get_data()
    print(part1(height_map))
    print(part2(height_map))