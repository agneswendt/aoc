def get_input():
    with open('input/1.txt', 'r') as f:
        lines = f.readlines()
    return [int(num) for num in lines]


def solve(data):
    def inc_sequence(seq):
        res = 0
        for i in range(len(seq) - 1):
            if seq[i] < seq[i + 1]:
                res += 1
        return res

    # part 1
    part1 = inc_sequence(data)

    # part 2
    new_seq = [sum(data[i:i+3]) for i in range(len(data) - 2)]

    part2 = inc_sequence(new_seq)
    return part1, part2


if __name__ == '__main__':
    part1, part2 = solve(get_input())
    print(f'Part 1: {part1}\nPart 2: {part2}')
