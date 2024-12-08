import re


raw_data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    nums = [[int(num) for num in re.split(r":\s*| ", line) if num] for line in lines]
    total = 0

    for num in nums:
        answer = num.pop(0)
        if operate(num, answer, "add", 0, 0) or operate(num, answer, "mult", 0, 0):
            total += answer
            print(answer)

    print(f"Total is {total}")


def operate(numline, answer, op, accum, index):
    if accum > answer:
        return False
    if len(numline) == index + 1:
        if op == "add":
            accum += numline[index]
            if accum == answer:
                return True
            else:
                return False
        elif op == "mult":
            accum = numline[index] * accum
            if accum == answer:
                return True
            else:
                return False
    else:
        left = numline[index]
        if op == "add":
            accum += left
        elif op == "mult":
            accum = left * accum
        index += 1
        return operate(numline, answer, "add", accum, index) or operate(
            numline, answer, "mult", accum, index
        )


if __name__ == "__main__":
    main()
