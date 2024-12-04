from itertools import pairwise
from copy import copy

raw_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

raw2_data = """48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7
7 10 8 10 11
29 28 27 25 26 25 22 20
"""

# 348 too low
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
        length = len(report)
        ups, up_poss = up_count(report)
        downs, down_poss = down_count(report)

        #print(f"Ups is {ups}, {len(up_poss)} and downs is {downs}, {len(down_poss)} out of {length}")

        if ups == length - 1:
            safe += 1
            #print(report)
        elif downs == length - 1:
            safe += 1
            #print(report)
        else:
            creport = copy(report)
            if ups > downs:
                for i in range(len(creport)):
                    creport.pop(i)
                    cup, cposs = up_count(creport)
                    if cup == length - 2:
                        safe += 1
                        #print(report)
                        break
                    else:
                        creport = copy(report)

            elif downs > ups:
                for i in range(len(creport)):
                    creport.pop(i)
                    cdown, cposs = down_count(creport)
                    if cdown == length - 2:
                        safe += 1
                        #print(report)
                        break
                    else:
                        creport = copy(report)
        
    print(f"There are {safe} safe reports.")



def down_count(report):
    count = 0
    possibles = []
    for a, b in pairwise(report):
        if a > b and 1 <= (a - b) <= 3:
            count += 1
        else:
            possibles.append(a)
            possibles.append(b)

    return count, possibles

def up_count(report):
    count = 0
    possibles = []
    for a, b in pairwise(report):
        if a < b and 1 <= (b - a) <= 3:
            count += 1
        else:
            possibles.append(a)
            possibles.append(b)

    return count, possibles


if __name__ == "__main__":
    main()
