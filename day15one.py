import time

raw_data = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    # lines = read_data.splitlines()
    a, moves = read_data.split("\n\n")
    floors = a.splitlines()

    start = []
    ware = [["B" for _ in range(len(floors))] for j in range(len(floors[0]))]
    for i in range(len(floors)):
        for j in range(len(floors[0])):
            ware[i][j] = floors[i][j]
            if ware[i][j] == "@":
                start = [i, j]

    robot = start
    iterable = get_direction(moves)
    for move in iterable:
        robot = find_empty(robot, ware, move)

    print(f"GPS score total is {find_gps(ware)}")
    print(f"Time is {time.time() - start_time}")


def find_empty(robot, board, move):
    cursor = robot
    firsto = False
    while board[cursor[0]][cursor[1]] != "#":
        cursor = [cursor[0] + move[0], cursor[1] + move[1]]
        if board[cursor[0]][cursor[1]] == "O" and not firsto:
            firsto = cursor
        elif board[cursor[0]][cursor[1]] == ".":
            if firsto:
                board[cursor[0]][cursor[1]] = "O"
                board[firsto[0]][firsto[1]] = "."
            board[robot[0]][robot[1]] = "."
            robot = [robot[0] + move[0], robot[1] + move[1]]
            return robot
    return robot


def find_gps(board):
    gps = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                gps += i * 100 + j

    return gps


def get_direction(moves):
    for char in moves:
        if char in "^v><":
            yield directions[char]


if __name__ == "__main__":
    main()
