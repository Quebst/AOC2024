raw_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    board = [["Z" for _ in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = lines[i][j]

    count = 0
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c == "X":
                count += check_x(board, i, j)

    print(f"The total is {count}")


# check all 8 directions
# [x][y] has an 'X'
# return number of xmas's
def check_x(board, x, y):
    count = 0
    # to right
    if board[x][y + 1] == "M":
        if board[x][y + 2] == "A":
            if board[x][y + 3] == "S":
                count += 1
    # down right
    if board[x + 1][y + 1] == "M":
        if board[x + 2][y + 2] == "A":
            if board[x + 3][y + 3] == "S":
                count += 1
    # down
    if board[x + 1][y] == "M":
        if board[x + 2][y] == "A":
            if board[x + 3][y] == "S":
                count += 1
    # down left
    if board[x + 1][y - 1] == "M":
        if board[x + 2][y - 2] == "A":
            if board[x + 3][y - 3] == "S":
                count += 1
    # left
    if board[x][y - 1] == "M":
        if board[x][y - 2] == "A":
            if board[x][y - 3] == "S":
                count += 1
    # up left
    if board[x - 1][y - 1] == "M":
        if board[x - 2][y - 2] == "A":
            if board[x - 3][y - 3] == "S":
                count += 1
    # up
    if board[x - 1][y] == "M":
        if board[x - 2][y] == "A":
            if board[x - 3][y] == "S":
                count += 1
    # up right
    if board[x - 1][y + 1] == "M":
        if board[x - 2][y + 2] == "A":
            if board[x - 3][y + 3] == "S":
                count += 1

    return count


if __name__ == "__main__":
    main()
