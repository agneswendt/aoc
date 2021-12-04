def part1(data):
    nums, boards = data
    score_boards = []
    bingo, bingo_num, winning_board = False, 0, 0

    for _ in range(len(boards)):
        score_boards.append([[0 for _ in range(5)] for _ in range(5)])

    for num_called in nums:
        for i, board in enumerate(boards):
            for y in range(5):
                for x in range(5):
                    if board[y][x] == num_called:
                        score_boards[i][y][x] = 1
        for i, board in enumerate(score_boards):
            for line in board + list(zip(*board)):
                if sum(line) == 5:
                    bingo = True
                    bingo_num = num_called
                    winning_board = i
                    break
        if bingo:
            break

    unmarked_sum = 0
    for y in range(5):
        for x in range(5):
            if score_boards[winning_board][y][x] == 0:
                unmarked_sum += boards[winning_board][y][x]
    return unmarked_sum * bingo_num


def part2(data):
    nums, boards = data
    score_boards = []
    bingoed = []
    bingoed_set = set()
    for _ in range(len(boards)):
        score_boards.append([[0 for _ in range(5)] for _ in range(5)])

    for num_called in nums:
        for i, board in enumerate(boards):
            if i not in bingoed_set:
                for y in range(5):
                    for x in range(5):
                        if board[y][x] == num_called:
                            score_boards[i][y][x] = 1
        for i, board in enumerate(score_boards):
            if i not in bingoed_set:
                for line in board + list(zip(*board)):
                    if sum(line) == 5:
                        bingoed.append((i, num_called))
                        bingoed_set.add(i)
                        break
        if len(bingoed) == len(boards):
            break

    last, bingo_num = bingoed[-1]
    unmarked_sum = 0
    for y in range(5):
        for x in range(5):
            if score_boards[last][y][x] == 0:
                unmarked_sum += boards[last][y][x]
    return unmarked_sum * bingo_num


def get_input():
    with open('input/4.txt', 'r') as f:
        lines = f.readlines()
    boards = []
    curr_board = []
    for line in lines:
        if line != '\n':
            if ',' in line:
                drawn = list(map(int, line.split(',')))
            else:
                inner = []

                for char in line.split(' '):
                    if char:
                        inner.append(int(char))
                curr_board.append(inner)
        else:
            if curr_board:
                boards.append(curr_board)
            curr_board = []
    if curr_board:
        boards.append(curr_board)
    return drawn, boards


if __name__ == '__main__':
    data = get_input()
    print(f'Part 1: {part1(data)}\nPart 2: {part2(data)}')
