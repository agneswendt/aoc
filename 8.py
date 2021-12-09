def part1(data):
    table = {2, 4, 3, 7}
    res = 0
    for _, output in data:
        for case in output:
            if len(case) in table:
                res += 1
    return res


def part2(data):
    tot_sum = 0
    for case, output in data:
        visited = set()
        res = {}
        unique = {2: 1, 4: 4, 3: 7, 7: 8}
        for digit in case:
            if len(digit) in unique:
                res[unique[len(digit)]] = frozenset(digit)
                visited.add(digit)

        for digit in case:
            if digit not in visited:
                segments = frozenset(digit)
                # determine the type of digit
                if len(segments) == 5:
                    # case for numbers 5, 3, 2
                    if res[1] <= segments:
                        res[3] = segments
                    elif len(res[4] & segments) == 3:
                        res[5] = segments
                    else:
                        res[2] = segments
                elif len(segments) == 6:
                    # case for numbers 6, 9, 2 with 6 segments
                    if res[1] <= segments:
                        if res[4] <= segments:
                            res[9] = segments
                        else:
                            res[0] = segments
                    else:
                        res[6] = segments
        number_res = ""
        for digit in output:
            for num in res:
                if res[num] == frozenset(digit):
                    number_res += str(num)
        tot_sum += int(number_res)
    return tot_sum


def get_input():
    with open('input/8.txt', 'r') as f:
        lines = f.readlines()
    res = []
    for line in lines:
        first, second = line.split(' | ')
        res.append((first.split(' '), second[:-1].split(' ')))
    return res


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
