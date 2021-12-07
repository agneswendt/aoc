def part1(data):
    res = {}
    for n in range(max(data)):
        res[n] = sum(abs(crab - n) for crab in data)
    return res[min(res, key=res.get)]


def part2(data):
    res = {}
    for n in range(max(data)):
        res[n] = sum(sum(range(abs(crab-n) + 1)) for crab in data)
    return res[min(res, key=res.get)]


def get_input():
    with open('input/7.txt', 'r') as f:
        lines = f.readlines()
    return list(map(int, lines[0].split(',')))


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
