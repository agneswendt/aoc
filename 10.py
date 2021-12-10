def part1(data):
    illegal_chars = []
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    for line in data:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
            '<': '>'
        }
        for char in line:
            if char in pairs:
                stack.append(char)
            else:
                # char is closing character
                closing = stack.pop()
                if not pairs[closing] == char:
                    illegal_chars.append(scores[char])
                    break
    return sum(illegal_chars)


def part2(data):
    res = []
    for line in data:
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
            '<': '>'
        }
        corrupted = False
        for char in line:
            if char in pairs:
                stack.append(char)
            else:
                # char is closing character
                closing = stack.pop()
                if not pairs[closing] == char:
                    corrupted = True

        scores = {
            ')': 1,
            ']': 2,
            '}': 3,
            '>': 4
        }
        if not corrupted:
            score = 0
            for sign in reversed(stack):
                score = score*5 + scores[pairs[sign]]
            res.append(score)

    return sorted(res)[len(res)//2]


def get_input():
    with open('input/10.txt', 'r') as f:
        lines = f.readlines()
    return [line[:-1] for line in lines]


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
