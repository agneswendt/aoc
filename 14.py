import functools
from collections import defaultdict


def solve(data):
    expr, rules = data

    @functools.cache
    def expand(c1, c2, depth=40):
        if depth == 0:
            return defaultdict(lambda: 0, {c1: 1})

        middle = rules[c1 + c2]
        left, right = expand(c1, middle, depth-1), expand(middle, c2, depth-1)
        res = {}
        for key in left.keys() | right.keys():
            res[key] = left[key] + right[key]
        return defaultdict(lambda: 0, res)

    # part 1
    res = defaultdict(lambda: 0)
    for i in range(len(expr) - 1):
        curr = expand(expr[i], expr[i+1], 10)
        for key in curr:
            res[key] += curr[key]
    res[expr[-1]] += 1

    smallest, *_, largest = sorted(res.values())
    part1 = largest - smallest

    # part 2
    res = defaultdict(lambda: 0)
    for i in range(len(expr) - 1):
        curr = expand(expr[i], expr[i+1], 40)
        for key in curr:
            res[key] += curr[key]
    res[expr[-1]] += 1

    smallest, *_, largest = sorted(res.values())
    part2 = largest - smallest
    return part1, part2


def get_input():
    with open('input/14.txt', 'r') as f:
        lines = f.readlines()
    rules = {}
    for line in lines:
        if ' -> ' in line:
            pair, res = line[:-1].split(' -> ')
            rules[pair] = res
    return lines[0][:-1], rules


if __name__ == '__main__':
    data = get_input()
    part1, part2 = solve(data)
    print(f'Part 1: {part1}\nPart 2: {part2}')
