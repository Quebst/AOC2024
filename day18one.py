import time
from sys import exit
from heapq import heappop, heappush

# answer is 446

# goal = [7, 7]
goal = [71, 71]

# BYTES = 12
BYTES = 1024


def main():
    print("Starting main")
    start_time = time.time()
    with open("input.txt", "r") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    start = [1, 1]
    frontier = []

    board = [["#"] * (goal[1] + 2)]
    for _ in range(goal[0]):
        board.append(["#"] + ["."] * goal[0] + ["#"])
    board.append(["#"] * (goal[1] + 2))

    for i, line in enumerate(lines):
        if i < BYTES:
            col, row = map(int, line.split(","))
            board[row + 1][col + 1] = "#"

    # Moves are adjusted cost, cost, cords
    first_move = (manh(start, goal), 0, start)
    heappush(frontier, first_move)

    while frontier:
        acost, cost, cords = heappop(frontier)
        if board[cords[0]][cords[1]] != ".":
            continue
        board[cords[0]][cords[1]] = cost
        neighs = neighbors(cords, board)

        for n in neighs:
            if n == goal:
                print(f"Path found at cost of {cost + 1}")
                exit()

            n_cost = cost + 1
            n_acost = n_cost + manh(n, goal)
            heappush(frontier, [n_acost, n_cost, n])


def neighbors(cursor, board):
    neighs = []
    i = cursor[0]
    j = cursor[1]

    if board[i + 1][j] == ".":
        neighs.append([i + 1, j])
    if board[i - 1][j] == ".":
        neighs.append([i - 1, j])
    if board[i][j + 1] == ".":
        neighs.append([i, j + 1])
    if board[i][j - 1] == ".":
        neighs.append([i, j - 1])

    return neighs


def manh(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])


if __name__ == "__main__":
    main()
