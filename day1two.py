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
    score = 0

    for line in lines:
        # print(line)
        a, b = line.split("   ")
        lefts.append(int(a))
        rights.append(int(b))

    lefts.sort()
    rights.sort()
    length = len(lefts) - 1
    index = 0
    old_left = -1

    for left in lefts:
        if left == old_left:
            pass
        else:
            mag = 0
            while left > rights[index]:
                if index < length:
                    index += 1
                else:
                    break
            while left == rights[index]:
                mag += 1
                if index < length:
                    index += 1
                else:
                    break

        score += left * mag
        old_left = left

    print("Score is: " + str(score))


if __name__ == "__main__":
    main()
