from collections import defaultdict


def part1(data):
    vent_map = defaultdict(lambda: 0)
    for coords1, coords2 in data:
        x1, y1 = coords1
        x2, y2 = coords2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1+1, y2+1)):
                vent_map[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1+1, x2+1)):
                vent_map[(x, y1)] += 1

    overlapping = 0
    for key in vent_map:
        if vent_map[key] > 1:
            overlapping += 1
    return overlapping


def part2(data):
    vent_map = defaultdict(lambda: 0)
    for coords1, coords2 in data:
        x1, y1 = coords1
        x2, y2 = coords2
        while (x1, y1) != (x2, y2):
            vent_map[(x1, y1)] += 1
            if x1 > x2:
                x1 -= 1
            elif x1 < x2:
                x1 += 1

            if y1 > y2:
                y1 -= 1
            elif y1 < y2:
                y1 += 1
        vent_map[(x2, y2)] += 1

    overlapping = 0
    for key in vent_map:
        if vent_map[key] > 1:
            overlapping += 1
    return overlapping


def get_input():
    with open('input/5.txt', 'r') as f:
        lines = f.readlines()
    res = []
    for line in lines:
        coords1, coords2 = line.split(' -> ')
        res.append((tuple(map(int, coords1.split(','))),
                    tuple(map(int, coords2.split(',')))))
    return res


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
