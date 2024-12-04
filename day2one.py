raw_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
1 2 4 5 4
"""

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    safe = 0
    reports = []
    for line in lines:
        reports.append(list(map(int, line.split())))

    # Three situations 1.Starts with two same numbers
    # 2. Numbers decreasing 3. Numbers increasing

    for report in reports:
        a = report.pop(0)
        b = report.pop(0)

        if a == b:
            continue
        elif a < b and (b - a) <= 3:
            safe += go_up(b, report)
        elif a > b and (a - b) <= 3:
            safe += go_down(b, report)

    print(f"There are {safe} safe reports.")


# a < b and numbers must keep going up 1 to 3
def go_up(one, report):
    while report:
        two = report.pop(0)
        diff = two - one

        if diff < 1 or diff > 3:
            return 0

        one = two

    return 1


# a > b and numbers must keep going down 1 to 3
def go_down(one, report):
    while report:
        two = report.pop(0)
        diff = one - two

        if diff < 1 or diff > 3:
            return 0

        one = two

    return 1


if __name__ == "__main__":
    main()
