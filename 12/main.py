from typing import DefaultDict, List, Tuple, Dict


def get_data(file_name: str) -> List[Tuple[str]]:
    with open(file_name) as f:
        return [ (line.split('-')[0],line.split('-')[1].strip()) for line in f.readlines() ]


class PathMap:
    def __init__(self, data: List[Tuple[str]]):
        self.map = self.generate_map(data)
        print(self.map)
        self.paths = list()

    def __str__(self):
        return '\n'.join([','.join(path) for path in self.paths])

    def generate_map(self, data: List[Tuple[str]]) -> Dict[str, List[str]]:
        map = DefaultDict(list)
        for line in data:
            if line[0] != 'end' and line[1] != 'start':
                map[line[0]].append(line[1])
            if line[1] != 'end' and line[0] != 'start':
                map[line[1]].append(line[0])
        return map
    
    def find_paths(self, start: str, path: List[str] = list()):
        path.append(start)
        if start == 'end':
            self.paths.append(path)
            return
        for node in self.map[start]:
            if node.islower() and node in path:
                continue
            self.find_paths(node, path.copy())
        del path

    def solve_part1(self):
        self.paths = list()
        self.find_paths('start')
        return len(self.paths)

    def solve_part2(self):
        self.paths = list()
        self.find_paths_part2('start')
        return len(self.paths)

    def find_paths_part2(self, start, path: List[str] = list(), visited: Dict[str, int] = DefaultDict(int)):
        path.append(start)
        if start == 'end':
            self.paths.append(path)
            return
        for node in self.map[start]:
            if node.islower() and visited[node] >= 2:
                continue
            else:
                visited[node] += 1
            self.find_paths_part2(node, path, visited.copy())

            
if __name__ == '__main__':
    data = get_data('12/input')
    path_map = PathMap(data)

    print(path_map.solve_part1())
    print(path_map.solve_part2())