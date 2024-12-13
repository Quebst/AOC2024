import time
import examples


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


# Corners?  3 nears equals + 2, 2 nears equal + 1, 1 near


def find_zone(char, cords, board):
    area = 0
    fencing = 0
    zone = []
    zone.append(cords)
    board[cords[0]][cords[1]] = ord(char)
    visited = {}

    while zone:
        x, y = current = zone.pop()
        area += 1
        nears = nearby([x, y])
        outedge = 0
        dirs = []
        for near in nears:
            direction = near[2]
            if board[near[0]][near[1]] == char:
                zone.append([near[0], near[1]])
                board[near[0]][near[1]] = ord(char)
            elif board[near[0]][near[1]] == ord(char):
                pass
            elif board[near[0]][near[1]] != ord(char):
                fencing += 1
                outedge += 1
                dirs.append(direction)

        visit = (x, y)
        visited[visit] = [outedge, dirs]

    # print(visited)

    borders = find_edges(visited)
    print(f"For area of char {char}, area is {area} and borders are {borders}")

    return borders * area


def find_edges(visited):
    borders = 0
    keys = list(visited.keys())
    for visit in keys:
        value = visited.pop(visit)

        cords = visit
        outedges = value[0]
        directs = value[1]

        nears = nearby(cords)

        for near in nears:
            comp = (near[0], near[1])
            location = near[2]
            if comp in visited:
                if location == "N" or location == "S":
                    if "E" in visited[comp][1] and "E" in directs:
                        outedges -= 1
                    if "W" in visited[comp][1] and "W" in directs:
                        outedges -= 1
                elif location == "E" or location == "W":
                    if "N" in visited[comp][1] and "N" in directs:
                        outedges -= 1
                    if "S" in visited[comp][1] and "S" in directs:
                        outedges -= 1

        borders += outedges

        # print(f" {visit} has {visited[visit][0]} borders on directions of {visited[visit][1]}")
    return borders


# x, y :  in Order N E S W
def nearby(cords):
    nears = [
        [cords[0] - 1, cords[1], "N"],
        [cords[0], cords[1] + 1, "E"],
        [cords[0] + 1, cords[1], "S"],
        [cords[0], cords[1] - 1, "W"],
    ]

    return nears


if __name__ == "__main__":
    main()
