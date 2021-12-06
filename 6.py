import functools


@functools.cache
def sum_branch(days, depth):
    if depth == 0:
        return 1
    if days == 0:
        return sum_branch(6, depth - 1) + sum_branch(8, depth - 1)
    else:
        return sum_branch(days - 1, depth - 1)


def part1(data):
    return sum(sum_branch(fish, 80) for fish in data)


def part2(data):
    return sum(sum_branch(fish, 256) for fish in data)


def get_input():
    with open('input/6.txt', 'r') as f:
        lines = f.readlines()
    return list(map(int, lines[0].split(',')))


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
