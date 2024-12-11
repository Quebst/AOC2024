raw_data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    trailheads = []
    board = [[-1 for _ in range(len(lines[0]) + 2)] for y in range(len(lines) + 2)]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = int(lines[i][j])
            if board[i + 1][j + 1] == 0:
                trailheads.append([i + 1, j + 1])

    total = 0
    # for b in board:
    #    print(b)

    for trailhead in trailheads:
        nines_reached = trace(board, trailhead, 0)
        nines_reached = set(nines_reached)
        # print(f"Trailhead {trailhead} has total {len(nines_reached)} at {nines_reached}")
        total += len(nines_reached)

    print(f"The total is {total}")


def trace(board, cords, index):
    nines = []
    next = index + 1
    nearby = [
        [cords[0], cords[1] + 1],
        [cords[0], cords[1] - 1],
        [cords[0] + 1, cords[1]],
        [cords[0] - 1, cords[1]],
    ]
    for near in nearby:
        if board[near[0]][near[1]] == next:
            if next == 9:
                nines.append(tuple(near))
            else:
                nines.extend(trace(board, near, next))

    return nines


if __name__ == "__main__":
    main()
