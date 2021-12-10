from statistics import median

AUTOCOMPLETE_SCORES = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

ERROR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

CLOSE_MAPPING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def get_data(path = '10/input'):
    with open(path) as f:
        data = f.readlines()
    return data




def add_autocomplete_points(point_stack, open_stack, points):
    for char in reversed(open_stack):
        points *= 5
        points += AUTOCOMPLETE_SCORES[char]
    point_stack.append(points)


def solve(data):
    point_stack = []
    error_points = 0
    for line in data:
        open_stack = []
        for char in line.strip():
            if char in CLOSE_MAPPING:
                open_stack.append(char)
            elif CLOSE_MAPPING[open_stack[-1]] != char:
                error_points += ERROR_SCORES[char]
                open_stack = []
                break
            else:
                open_stack.pop()
        points = 0
        if open_stack:
            add_autocomplete_points(point_stack, open_stack, points)
            
    return error_points, int(median(point_stack))

def main():
    data = get_data()
    solved = solve(data)
    print(f'Part 1: {solved[0]}\t Part 2: {solved[1]}')


if __name__ == '__main__':
    main()
