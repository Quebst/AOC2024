import time

raw_data = """AAAA
BBCD
BBCC
EEEC
"""

raw2_data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

raw3_data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""


def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    board = [[8 for _ in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = lines[i][j]

    total_cost = 0
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if isinstance(col, str):
                total_cost += find_zone(col, [x, y], board)

    print(f"Total cost is {total_cost}   Time is {time.time() - start_time}")


def find_zone(char, cords, board):
    area = 0
    fencing = 0
    zone = []
    zone.append(cords)
    board[cords[0]][cords[1]] = ord(char)

    while zone:
        x, y = zone.pop()
        area += 1
        nears = nearby([x, y])
        for near in nears:
            if board[near[0]][near[1]] == char:
                zone.append(near)
                board[near[0]][near[1]] = ord(char)
            elif board[near[0]][near[1]] != ord(char):
                fencing += 1

    # print(f"For area of char {char}, area is {area} and fencing is {fencing}")
    return fencing * area


def nearby(cords):
    nears = [
        [cords[0], cords[1] + 1],
        [cords[0], cords[1] - 1],
        [cords[0] + 1, cords[1]],
        [cords[0] - 1, cords[1]],
    ]

    return nears


if __name__ == "__main__":
    main()
