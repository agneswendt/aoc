import math
from queue import PriorityQueue
from collections import defaultdict


def min_cost(G, target):
    dist = defaultdict(lambda: math.inf, {(0, 0): 0})
    prev = defaultdict()
    queue = PriorityQueue()
    queue.put((0, (0, 0)))

    while not queue.empty():
        cost, current = queue.get()

        if current == target:
            return cost

        x, y = current
        for nx, ny in ((x + 1, y), (x, y + 1),
                       (x - 1, y), (x, y - 1)):
            length = G(nx, ny)
            if length is not None:
                alt = cost + length
                if alt < dist[(nx, ny)]:
                    dist[(nx, ny)] = alt
                    prev[(nx, ny)] = current
                    queue.put((alt, (nx, ny)))


def solve(G):
    def part1_graph(x, y):
        if 0 <= x < len(G[0]) and 0 <= y < len(G):
            return G[y][x]

    def part2_graph(x, y):
        if 0 <= x < 5 * len(G[0]) and 0 <= y < 5 * len(G):
            val = (G[y % len(G)][x % len(G[0])] + x // len(G[0]) + y // len(G))
            if val == 9:
                return 9
            return val % 9

    return min_cost(part1_graph, (len(G[0]) - 1, len(G) - 1)), \
        min_cost(part2_graph, (5 * len(G[0]) - 1, 5 * len(G) - 1))


def get_input():
    with open('input/15.txt', 'r') as f:
        lines = f.readlines()
    return [list(map(int, line[:-1])) for line in lines]


if __name__ == '__main__':
    data = get_input()
    part1, part2 = solve(data)
    print(f'Part 1: {part1}\nPart 2: {part2}')
