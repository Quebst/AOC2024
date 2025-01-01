import time
from collections import Counter

# 1530
raw_data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def main():
    print("Starting main...")
    start_time = time.time()
    with open("input.txt", "r") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    board = [["#" for i in range(len(lines) + 2)] for j in range(len(lines[0]) + 2)]
    start = ()
    end = ()
    shorter_paths = []

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = lines[i][j]
            if board[i + 1][j + 1] == "S":
                start = (i + 1, j + 1)
            elif board[i + 1][j + 1] == "E":
                end = (i + 1, j + 1)

    score_path(board, start, end)

    shorter_paths = find_shorts(board)

    # counts = Counter(shorter_paths)
    # print(counts)
    count = 0
    for path in shorter_paths:
        if path >= 100:
            count += 1

    print(f"Count is {count}")


def find_shorts(board):
    paths = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "#":
                current = board[i][j]
                # check 2 in each direction
                if board[i + 2][j] != "#" and board[i + 2][j] < current - 2:
                    paths.append(current - board[i + 2][j] - 2)
                if board[i - 2][j] != "#" and board[i - 2][j] < current - 2:
                    paths.append(current - board[i - 2][j] - 2)
                if board[i][j + 2] != "#" and board[i][j + 2] < current - 2:
                    paths.append(current - board[i][j + 2] - 2)
                if board[i][j - 2] != "#" and board[i][j - 2] < current - 2:
                    paths.append(current - board[i][j - 2] - 2)

    return sorted(paths)


def score_path(board, start, end):
    cursor = end
    cost = 0

    board[end[0]][end[1]] = 0
    while cursor != start:
        cost += 1

        if board[cursor[0] + 1][cursor[1]] == ".":
            cursor = (cursor[0] + 1, cursor[1])
        elif board[cursor[0] - 1][cursor[1]] == ".":
            cursor = (cursor[0] - 1, cursor[1])
        elif board[cursor[0]][cursor[1] + 1] == ".":
            cursor = (cursor[0], cursor[1] + 1)
        elif board[cursor[0]][cursor[1] - 1] == ".":
            cursor = (cursor[0], cursor[1] - 1)
        else:
            board[cursor[0]][cursor[1]] = cost
            break

        board[cursor[0]][cursor[1]] = cost
    board[start[0]][start[1]] = cost + 1

    # for b in board:
    #     print(b)


if __name__ == "__main__":
    main()
