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
            if c == "A":
                count += check_a(board, i, j)

    print(f"The total is {count}")


def check_a(board, x, y):
    a = board[x - 1][y - 1]
    b = board[x + 1][y + 1]

    c = board[x - 1][y + 1]
    d = board[x + 1][y - 1]

    if ord(a) + ord(b) == 160 and ord(c) + ord(d) == 160:
        return 1
    
    return 0


if __name__ == "__main__":
    main()