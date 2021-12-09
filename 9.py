import math


def part1(data):
    risk_levels = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            # check neighbours
            low_point = True
            for j in range(max(0, y-1), min(len(data), y + 2)):
                for i in range(max(0, x-1), min(len(data[0]), x + 2)):
                    if (j != y) or (i != x):
                        if data[j][i] <= data[y][x]:
                            low_point = False
            if low_point:
                risk_levels.append(data[y][x] + 1)

    return sum(risk_levels)


def part2(data):
    low_points = []
    # get lowest point of basins
    for y in range(len(data)):
        for x in range(len(data[0])):
            low = True
            for j in range(max(0, y-1), min(len(data), y + 2)):
                for i in range(max(0, x-1), min(len(data[0]), x + 2)):
                    if (j != y) or (i != x):
                        if data[j][i] <= data[y][x]:
                            low = False
            if low:
                low_points.append((x, y))

    def traverse(data, x, y, visited):
        if data[y][x] == 9 or (x, y) in visited:
            return 0

        tot_sum = 0
        visited.add((x, y))
        for j in range(max(0, y-1), min(len(data), y + 2)):
            for i in range(max(0, x-1), min(len(data[0]), x + 2)):
                if j == y or i == x:  # do not check diagonals
                    if (i, j) not in visited:
                        tot_sum += traverse(data, i, j, visited)
        return tot_sum + 1

    # traverse from lowest point until high points are found
    basins = [traverse(data, x, y, set()) for x, y in low_points]

    # return product of three largest basins
    return math.prod(sorted(basins, reverse=True)[:3])


def get_input():
    with open('input/9.txt', 'r') as f:
        lines = f.readlines()
    return [list(map(int, line[:-1])) for line in lines]


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
