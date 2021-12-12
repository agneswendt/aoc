from collections import defaultdict


def part1(data, current="start", visited=set()):
    if current == "end":
        return 1
    count = 0
    visited = visited | {current} if current.islower() else visited

    for neighbor in data[current]:
        if neighbor not in visited:
            count += part1(data, neighbor, visited)
    return count


def part2(data, current="start", visited=set(), used_twice=False):
    if current == "end":
        return {("end",)}
    paths = set()

    for neighbor in data[current]:
        if neighbor not in visited:
            if not used_twice and current != "start" and current.islower():
                paths |= part2(data, neighbor, visited, True) | \
                    part2(data, neighbor, visited | {current}, used_twice)
            elif not current.islower():
                paths |= part2(data, neighbor, visited, used_twice)
            else:
                paths |= part2(data, neighbor, visited | {current}, used_twice)

    return {(current, ) + p for p in paths if p}


def get_input():
    with open('input/12.txt', 'r') as f:
        lines = f.readlines()
    res = defaultdict(list)
    for line in lines:
        n1, n2 = line[:-1].split('-')
        res[n1].append(n2)
        res[n2].append(n1)
    return res


if __name__ == '__main__':
    data = get_input()

    print(f'Part 1: {part1(data)}\nPart 2: {len(part2(data))}')
