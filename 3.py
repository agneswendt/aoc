def part1(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        ones, zeros = 0, 0
        for num in data:
            if num[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    def find_num(lst, num1, num2):
        lst = lst.copy()
        i = 0
        while len(lst) > 1:
            ones, zeros = 0, 0
            for num in lst:
                if num[i] == '1':
                    ones += 1
                else:
                    zeros += 1
            for val in lst.copy():
                if ones >= zeros:
                    if val[i] != num1 and val in lst:
                        lst.remove(val)
                else:
                    if val[i] != num2 and val in lst:
                        lst.remove(val)
            i += 1
        return lst[0]

    oxygen, scrubber = find_num(data, '1', '0'), find_num(data, '0', '1')
    return int(oxygen, 2) * int(scrubber, 2)


def get_input():
    with open('input/3.txt', 'r') as f:
        lines = f.readlines()
    return [num[:-1] if num[-1] == '\n' else num for num in lines]


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
