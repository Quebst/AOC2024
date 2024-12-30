import time
from functools import lru_cache

# 771745460576799

raw_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


found = 0


def main():
    print("Starting main...")
    start_time = time.time()
    with open("input.txt", "r") as f:
        read_data = f.read()
    patterns, towels = read_data.split("\n\n")
    towels = towels.splitlines()
    patterns = tuple(
        sorted([patt.strip() for patt in patterns.split(",")], key=len, reverse=True)
    )
    # print(patterns)
    # print(towels)
    score = 0

    for towel in towels:
        score += check_towel(towel, patterns)
        check_towel.cache_clear()

    print(f"Score is {score}")
    print(f"Time is {time.time() - start_time}")


@lru_cache(maxsize=None)
def check_towel(towel, patterns):
    fnd = 0
    if len(towel) == 0:
        return 1
    for pattern in patterns:
        if towel.startswith(pattern):
            fnd += check_towel(towel[len(pattern) :], patterns)
    return fnd


if __name__ == "__main__":
    main()
