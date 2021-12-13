def part1(data):
    dots, instructions = data
    axis, num = instructions[0]
    new_dots = set()
    for x, y in dots:
        if axis == 'x' and x >= num:
            new_dots.add((num - (x - num), y))
        elif axis == 'y' and y >= num:
            new_dots.add((x, num - (y - num)))
        else:
            new_dots.add((x, y))
    dots = new_dots
    return len(dots)


def part2(data):
    dots, instructions = data
    for axis, num in instructions:
        new_dots = set()
        for x, y in dots:
            if axis == 'x' and x >= num:
                new_dots.add((num - (x - num), y))
            elif axis == 'y' and y >= num:
                new_dots.add((x, num - (y - num)))
            else:
                new_dots.add((x, y))
        dots = new_dots
    res = []
    for y in range(max(dots, key=lambda a: a[1])[1] + 1):
        row = []
        for x in range(max(dots, key=lambda a: a[0])[0] + 1):
            if (x, y) in dots:
                row.append('#')
            else:
                row.append('.')
        res.append("".join(row))
    return "\n".join(res)


def get_input():
    with open('input/13.txt', 'r') as f:
        lines = f.readlines()
    dots, axis = set(), []
    for line in lines:
        if ',' in line:
            dots.add(tuple(map(int, line.split(','))))
        elif '=' in line:
            coord = line.split(' ')[2].split('=')[0]
            num = int(line.split(' ')[2].split('=')[1])
            axis.append((coord, num))
    return dots, axis


if __name__ == '__main__':
    data = get_input()

    print(f'Part 1: {part1(data)}\nPart 2: \n{part2(data)}')
