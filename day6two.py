from itertools import cycle

raw_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# answer 1976
# i: 43  j: 52 inital staring position, pointed North
STARTING = [44, 53]
#STARTING = [7, 5]
DIRECTIONS = ["North", "East", "South", "West"]


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    direct = cycle(DIRECTIONS)

    board = [["B" for _ in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = lines[i][j]

    cdir = next(direct)
    body = STARTING
    head = [STARTING[0] - 1, STARTING[1]]

    while board[head[0]][head[1]] != "B":
        board[body[0]][body[1]] = "X"
        if board[head[0]][head[1]] == "." or board[head[0]][head[1]] == "X":
            body = next_body(body, cdir)
            head = next_body(head, cdir)
        elif board[head[0]][head[1]] == "#":
            cdir = next(direct)
            match cdir:
                case "North":
                    head = [head[0] - 1, head[1] + 1]
                case "East":
                    head = [head[0] + 1, head[1] + 1]
                case "South":
                    head = [head[0] + 1, head[1] - 1]
                case "West":
                    head = [head[0] - 1, head[1] - 1]

    # for b in board:
    #     print(b)

    print(f"Count is {count_x(board) + 1}")

    obstructs = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                board[i][j] = "#"
                obstructs += run_course(board)
                board[i][j] = "X"

    print(f"Obstructs is {obstructs} ")



# run the course
def run_course(board):
    direct2 = cycle(DIRECTIONS)
    cdir = next(direct2)
    body = STARTING
    head = [STARTING[0] - 1, STARTING[1]]
    visited = []

    while board[head[0]][head[1]] != "B":
        if (body, cdir) in visited:
            print(f"Obstruct at {body}")
            return 1
        visited.append((body, cdir))
        if board[head[0]][head[1]] == "." or board[head[0]][head[1]] == "X":
            body = next_body(body, cdir)
            head = next_body(head, cdir)
        elif board[head[0]][head[1]] == "#":
            cdir = next(direct2)
            match cdir:
                case "North":
                    head = [head[0] - 1, head[1] + 1]
                case "East":
                    head = [head[0] + 1, head[1] + 1]
                case "South":
                    head = [head[0] + 1, head[1] - 1]
                case "West":
                    head = [head[0] - 1, head[1] - 1]

        
    return 0


# takes a [x, y] cord, direction and return next [x, y]
def next_body(cursor, dir):
    match dir:
        case "North":
            return [cursor[0] - 1, cursor[1]]
        case "East":
            return [cursor[0], cursor[1] + 1]
        case "South":
            return [cursor[0] + 1, cursor[1]]
        case "West":
            return [cursor[0], cursor[1] - 1]

    print("Error, no valid direction")
    return None


def count_x(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "X":
                count += 1
    return count


if __name__ == "__main__":
    main()
