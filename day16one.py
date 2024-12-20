import time
from heapq import heappop, heappush
from copy import copy

# 123540

raw_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

raw2_data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""
## plus 1


def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    board = [list(line) for line in lines]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "S":
                start = (i, j)
                board[i][j] = "."
            if board[i][j] == "E":
                goal = (i, j)
                board[i][j] = "."

    print(f"Start is {start} and goal is {goal}")
    hubs = process_board(board)
    visited = set()
    direct = "E"

    frontier = []
    shortest_path = float("inf")

    # move is (tcost,[x, y], direction)
    move = (0, start, direct)
    heappush(frontier, move)

    while frontier:
        move = heappop(frontier)
        if move[0] > shortest_path:
            continue
        if move[1] == goal:
            if move[0] < shortest_path:
                shortest_path = move[0]
                print(f"New path tcost {shortest_path}")
        else:
            neighs = hubs[move[1]].connects
            for n in neighs:
                if (n[0][0], n[0][1], n[2]) not in visited:
                    new_cost = move[0] + n[1]
                    if move[2] != n[2]:
                        new_cost += 1000
                    new_move = (new_cost, n[0], n[2])
                    heappush(frontier, new_move)
        visited.add((move[1][0], move[1][1], move[2]))


def print_hubs(board, hubs):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) in hubs:
                print("H", end="")
            else:
                print(board[i][j], end="")
        print("")


def process_board(board):
    hubs = {}

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                if is_hub(board, i, j):
                    new_hub = Hub(i, j)
                    hubs[i, j] = new_hub

    # Find Horizontal paths
    for i in range(len(board)):
        last = False
        path = 0
        j = 0
        while j < len(board[0]):
            while board[i][j] == ".":
                if (i, j) in hubs and not last:
                    last = (i, j)
                elif (i, j) in hubs:
                    hubs[last].connects.append([(i, j), path, "E"])
                    hubs[i, j].connects.append([last, path, "W"])
                    last = (i, j)
                    path = 0
                j += 1
                path += 1
            else:
                path = 0
                last = False
            j += 1

    # Find Verticle paths
    for j in range(len(board[0])):
        last = False
        path = 0
        i = 0
        while i < len(board):
            while board[i][j] == ".":
                if (i, j) in hubs and not last:
                    last = (i, j)
                elif (i, j) in hubs:
                    hubs[last].connects.append([(i, j), path, "S"])
                    hubs[i, j].connects.append([last, path, "N"])
                    last = (i, j)
                    path = 0
                i += 1
                path += 1
            else:
                path = 0
                last = False
            i += 1

    return hubs


def is_hub(board, i, j):
    n = board[i - 1][j] == "."
    e = board[i][j + 1] == "."
    s = board[i + 1][j] == "."
    w = board[i][j - 1] == "."
    deadend = sum([n, e, s, w]) == 1

    return (n or s) and (e or w) or deadend


class Hub:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        # cost and direction
        self.connects = []

    def __str__(self):
        return f"Hub row {self.row} col {self.col} has connects {self.connects}"


if __name__ == "__main__":
    main()
