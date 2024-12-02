raw_data = """3   4
4   3
2   5
1   3
3   9
3   3"""


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    lefts = []
    rights = []
    difference = 0

    for line in lines:
        # print(line)
        a, b = line.split("   ")
        lefts.append(int(a))
        rights.append(int(b))

    lefts.sort()
    rights.sort()

    for i in range(len(lefts)):
        difference = difference + abs(lefts[i] - rights[i])

    print("Difference is: " + str(difference))


if __name__ == "__main__":
    main()
