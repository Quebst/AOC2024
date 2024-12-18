import time
import inspect

raw_data = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

raw2_data = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""


# 1458740

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
to_move = []

def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    # lines = read_data.splitlines()
    a, moves = read_data.split("\n\n")
    floors = a.splitlines()

    global to_move
    start = []
    ware = [] 
    for i in range(len(floors)):
        row = []
        for j in range(len(floors[0])):
            char = floors[i][j]
            if char == '#':
                row.extend("##")
            elif char == 'O':
                row.extend("[]")
            elif char == '.':
                row.extend("..")
            elif char == '@':
                start = [i, len(row)]
                row.extend("..")
                
        ware.append(row)

    # for row in ware:
    #     print(row)
    robot = start
    iterable = get_direction(moves)
    for move in iterable:
        cursor = [robot[0] + move[0], robot[1] + move[1]]

        if ware[cursor[0]][cursor[1]] == '#':
            continue
        elif ware[cursor[0]][cursor[1]] == '.':
            ware[robot[0]][robot[1]] = '.'
            robot = cursor
        # east <--> west
        elif move[0] == 0:
            if shift_side(cursor, ware, move):
                robot = cursor
        # north south
        elif move[1] == 0:
            if ware[cursor[0]][cursor[1]] == ']':
                if shift_perp([cursor[0], cursor[1] - 1], ware, move):
                    robot = cursor
                    to_move = []
                else:
                    undo_moves(ware)
            else: 
                if shift_perp(cursor, ware, move):
                    robot = cursor
                    to_move = []
                else:
                    undo_moves(ware)
        
        else:
            print("Not a valid move!")

    print(f"GPS score total is {find_gps(ware)}")
    print(f"Time is {time.time() - start_time}")


def shift_side(cursor, board, move):

    new_cursor = [cursor[0] + move[0], cursor[1] + move[1]]
    if board[new_cursor[0]][new_cursor[1]] == "#":
        return False
    
    # new spot, old
    if board[new_cursor[0]][new_cursor[1]] == ".":
        swap(cursor, new_cursor, board)
        return True
    else:
        if shift_side(new_cursor, board, move):
            swap(cursor, new_cursor, board)
            return True
    

#North South
#cursor is [ 
def shift_perp(left, board, move):
    right = [left[0], left[1] + 1]
    new_left = [left[0] + move[0], left[1] + move[1]]
    new_right = [right[0] + move[0], right[1] + move[1]]

    if board[new_left[0]][new_left[1]] == '#' or board[new_right[0]][new_right[1]] == '#':
        return False 
    elif board[new_left[0]][new_left[1]] == '.' and board[new_right[0]][new_right[1]] == '.':
        swap (left, new_left, board)
        swap (right, new_right, board)
        return True
    elif board[new_left[0]][new_left[1]] == '[' and board[new_right[0]][new_right[1]] == ']':
        if shift_perp(new_left, board, move):
            swap(left, new_left, board)
            swap(right, new_right, board)
            return True
    else:
        left_flag = False
        right_flag = False
        if board[new_left[0]][new_left[1]] == '.':
            left_flag = True
        elif board[new_left[0]][new_left[1]] == ']':
            left_flag = shift_perp([new_left[0], new_left[1] - 1], board, move)
        
        if board[new_right[0]][new_right[1]] == '.':
            right_flag = True
        elif board[new_right[0]][new_right[1]] == '[':
            right_flag = shift_perp(new_right, board, move)

        if left_flag and right_flag:
            swap(left, new_left, board)
            swap(right, new_right, board)
            return True
        
def undo_moves(board):
    global to_move
    while to_move:
        unmove = to_move.pop()
        swap(unmove[0], unmove[1], board)


def swap(one, two, board):
    temp = board[one[0]][one[1]]
    board[one[0]][one[1]] = board[two[0]][two[1]]
    board[two[0]][two[1]] = temp
    if inspect.stack()[1].function == "shift_perp":
        global to_move
        to_move.append([one, two])

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
            if board[i][j] == "[":
                gps += i * 100 + j

    return gps


def get_direction(moves):
    for char in moves:
        if char in "^v><":
            yield directions[char]


if __name__ == "__main__":
    main()
