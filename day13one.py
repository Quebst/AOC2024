import time
from sympy import symbols, Eq, solve
import re

raw_data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    # lines = read_data.splitlines()
    games = raw_data.split("\n\n")
    total = 0

    for game in games:
        gtotal = 0
        g = Clawgame(game)
        results = solver(g)
        if results:
            gtotal = results[0] * 3 + results[1]
            total += gtotal

    print(f"Total is {total}")
    print(f"Total time is {time.time() - start_time}")


def solver(g):
    a, b = symbols("a b", integer=True)
    ax, ay, bx, by, px, py = symbols("ax ay bx by px py")
    values = {ax: g.ax, ay: g.ay, bx: g.bx, by: g.by, px: g.px, py: g.py}

    eq1 = Eq(ax * a + bx * b, px)
    eq2 = Eq(ay * a + by * b, py)

    solution = solve([eq1.subs(values), eq2.subs(values)], (a, b), dict=True)
    if solution:
        return (solution[0][a], solution[0][b])
    return None


class Clawgame:

    def __init__(self, paragraph):
        lines = paragraph.splitlines()

        pattern = r"X([+]?\d+), Y([+]?\d+)"
        mat = re.search(pattern, lines[0])
        self.ax = int(mat.group(1))
        self.ay = int(mat.group(2))
        mat = re.search(pattern, lines[1])
        self.bx = int(mat.group(1))
        self.by = int(mat.group(2))
        pattern = r"X=(\d+), Y=(\d+)"
        mat = re.search(pattern, lines[2])
        self.px = int(mat.group(1))
        self.py = int(mat.group(2))


if __name__ == "__main__":
    main()
