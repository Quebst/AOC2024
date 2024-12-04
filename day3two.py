import re

raw_data = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    # lines = read_data.splitlines()

    lines = re.split("don't\(\)", read_data)

    lines[0] = "do()" + lines[0]

    total = 0

    for line in lines:
        print(line)
        temp = re.split("do\(\)", line, maxsplit=1)
        if len(temp) == 2:
            trash, good = temp
            total += find_muls(good)

    print(f"The total is {total}")


def find_muls(instructs):
    matches = re.findall("mul\(\d+,\d+\)", instructs)
    total = 0

    for match in matches:
        m = re.findall("\d+.\d+", match)
        a, b = m[0].split(",")
        total = total + (int(a) * int(b))

    return total


if __name__ == "__main__":
    main()
