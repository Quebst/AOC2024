import re

raw_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    matches = re.findall("mul\(\d+,\d+\)", read_data)
    total = 0

    print(matches)

    for match in matches:
        m = re.findall("\d+.\d+", match)
        a, b = m[0].split(",")
        total = total + (int(a) * int(b))


    print(f"Total is {total}")

if __name__ == "__main__":
    main()