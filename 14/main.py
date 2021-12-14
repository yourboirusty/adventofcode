from typing import Tuple, List, Dict, DefaultDict
from itertools import pairwise
from collections import Counter
from time import perf_counter

def get_data(file_name: str) -> Tuple[str, List[Tuple[str,str]]]:
    with open(file_name) as f:
        lines = f.readlines()

    template = lines.pop(0).strip()
    lines.pop(0)
    pairs = [(line.split('->')[0].strip(), line.split('->')[1].strip()) for line in lines]
    return template, pairs


class Polymer:
    pairs: Dict[str, int] = DefaultDict(int)
    rules: Dict[str,str]
    outcomes: Dict[str, Tuple[str,str]]
    elements_counter: Dict[str, int] = DefaultDict(int)

    def __init__(self, template: str, pairs: List[Tuple[str,str]]) -> None:
        for pair in pairwise(template):
            self.pairs["".join(pair)] += 1
        self.rules = { pair[0]: pair[1] for pair in pairs }
        self.outcomes = {}
        for char in list(template):
            self.elements_counter[char] += 1
        for pair, result in self.rules.items():
            self.outcomes[pair] = (pair[0] + result, result + pair[1])    

    def insert_elements(self):
        new_elements = []
        for pair in pairwise(self.elements):
            pair_list = list(pair)
            pair_sign = self.rules["".join(pair_list)]
            pair_list.insert(1, pair_sign)
            if new_elements:
                pair_list = pair_list[1:]
            new_elements += pair_list
        self.elements = new_elements


    def increment_elements(self):
        pairs = self.pairs.copy()
        for pair, value in pairs.items():
            self.pairs[pair] -= value
            self.elements_counter[self.rules[pair]] += value
            for outcome in self.outcomes[pair]:
                self.pairs[outcome] += value
        del pairs

    def count_characters(self) -> Counter:
        char_counter = Counter()
        for pair, value in self.pairs.items():
            char_counter.update(pair*value)
        return char_counter            

    def get_score(self):
        char_count = list(self.elements_counter.values())
        char_count.sort()
        return char_count[-1] - char_count[0]

    def solve_part1(self) -> int:
        for _ in range(10):
            self.increment_elements()
        return self.get_score()

    def solve_part2(self) -> int:
        start = perf_counter()
        for i in range(40):
            self.increment_elements()
        count = list(self.elements_counter.values())
        count.sort()
        print(f"{perf_counter() - start:.10f}s")
        return count[-1] - count[0]

if __name__ == '__main__':
    data = get_data('14/input')
    polymer = Polymer(*data)
    print(polymer.solve_part2())