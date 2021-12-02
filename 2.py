def part1(data):
    horizontal, depth = 0, 0
    for instr, val in data:
        match instr:
            case 'forward':
                horizontal += val
            case 'down':
                depth += val
            case 'up':
                depth -= val
    return horizontal * depth


def part2(data):
    horizontal, depth, aim = 0, 0, 0
    for instr, val in data:
        match instr:
            case 'forward':
                horizontal += val
                depth += val * aim
            case 'down':
                aim += val
            case 'up':
                aim -= val
    return horizontal * depth


def get_input():
    with open('input/2.txt', 'r') as f:
        lines = f.readlines()
    res = []
    for line in lines:
        instr, val = line.split(' ')
        res.append((instr, int(val)))
    return res


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
