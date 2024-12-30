import time
from functools import lru_cache

# 302

raw_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


found = False


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
    global found

    for towel in towels:
        if check_towel(towel, patterns):
            score += 1
            # print(score)
        found = False
        check_towel.cache_clear()

    print(f"Score is {score}")
    print(f"Time is {time.time() - start_time}")


@lru_cache(maxsize=None)
def check_towel(towel, patterns):
    global found
    if len(towel) == 0 or found:
        found = True
        return True
    for pattern in patterns:
        if found:
            return True
        if towel.startswith(pattern):
            check_towel(towel[len(pattern) :], patterns)
    return False


if __name__ == "__main__":
    main()
