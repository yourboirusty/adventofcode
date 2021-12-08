from typing import List, Set, Dict
from dataclasses import dataclass


def find_unique(pattern):
    if len(pattern) == 2:
        return 1
    elif len(pattern) == 3:
        return 7
    elif len(pattern) == 4:
        return 4
    elif len(pattern) == 7:
        return 8


def get_unique(signal_patterns: List[Set[str]]) -> Dict[int, Set[str]]:
    unique_values = {}
    while pattern := signal_patterns.pop(0):
        if number := find_unique(pattern):
            unique_values[number] = pattern
        else:
            signal_patterns.append(pattern)
        if len(unique_values) == 4:
            break
    unique_values['L'] = {x for x in unique_values[4] if x not in unique_values[7]}
    unique_values['-'] = {x for x in unique_values['L'] if x not in unique_values[1]}
    return unique_values


def find_pattern(patterns: Dict[int,set], pattern: set) -> int:
    if len(pattern) == 5:
        if patterns[1].issubset(pattern):
            return 3
        elif patterns['L'].issubset(pattern):
            return 5
        else:
            return 2    
    if len(pattern) == 6:
        if patterns['L'].issubset(pattern) and not patterns[4].issubset(pattern):
            return 6
        if patterns[1].issubset(pattern) and patterns['-'].issubset(pattern):
            return 9
        if not patterns['-'].issubset(pattern):
            return 0
    raise ValueError     


def decode(signal_patterns: List[Set[str]], unique_patterns: Dict[int, Set[str]]) -> Dict[Set[str], int]:
    """
    Decodes a list of signal patterns into a dict of signal values.
    """
    patterns = unique_patterns

    while signal_patterns:
        pattern = signal_patterns.pop(0)
        try:
            patterns[find_pattern(patterns, pattern)] = pattern
        except ValueError:
            signal_patterns.append(pattern)

    return {"".join(sorted(v)): k for k, v in patterns.items()}


if __name__ == "__main__":
    with open("8/input") as f:
        signal = [ line.strip() for line in f.readlines() ]
    signal_patterns = [ pattern.split(" | ")[0].split(" ") for pattern in signal ]
    output_data = [ pattern.split(" | ")[1].split(" ") for pattern in signal ]

    basic_digits = 0
    output_values = 0
    for signal, output in zip(signal_patterns, output_data):
        
        signal = list(map(set, signal))

        unique = get_unique(signal)
        patterns = decode(signal, unique)

        output_value = []
        for idx, digit in enumerate(output):
            output_values += patterns["".join(sorted(digit))] * 10 ** (len(output) - (idx + 1))
            if set(digit) in list(unique.values()):
                basic_digits += 1
    print(output_values)
