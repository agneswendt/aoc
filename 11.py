from copy import deepcopy


def part1(grid):
    steps = 100
    flashes = 0

    for _ in range(steps):
        for y, row in enumerate(grid):
            for x, num in enumerate(row):
                grid[y][x] += 1
        flashed = True
        flashed_coords = set()
        while flashed:
            flashed = False
            for y, row in enumerate(grid):
                for x, num in enumerate(row):
                    if num > 9 and (x, y) not in flashed_coords:
                        flashed = True
                        flashed_coords.add((x, y))
                        for j in range(max(0, y-1), min(y+2, len(grid))):
                            for i in range(max(0, x-1), min(x+2, len(grid[0]))):
                                grid[j][i] += 1
                        flashes += 1
        for x, y in flashed_coords:
            grid[y][x] = 0
    return flashes


def part2(grid):
    steps = 1
    while True:
        for y, row in enumerate(grid):
            for x, num in enumerate(row):
                grid[y][x] += 1
        flashed = True
        flashed_coords = set()
        while flashed:
            flashed = False
            for y, row in enumerate(grid):
                for x, num in enumerate(row):
                    if num > 9 and (x, y) not in flashed_coords:
                        flashed = True
                        flashed_coords.add((x, y))
                        for j in range(max(0, y-1), min(y+2, len(grid))):
                            for i in range(max(0, x-1), min(x+2, len(grid[0]))):
                                grid[j][i] += 1
        for x, y in flashed_coords:
            grid[y][x] = 0
        if len(flashed_coords) == len(grid) * len(grid[0]):
            return steps
        steps += 1


def get_input():
    with open('input/11.txt', 'r') as f:
        lines = f.readlines()
    return [list(map(int, line[:-1])) for line in lines]


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(deepcopy(data))}\nPart 2: {part2(deepcopy(data))}')