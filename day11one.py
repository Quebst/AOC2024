raw_data = """0 1 10 99 999"""
raw2_data = """125 17"""


"""Initial arrangement:
125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2
"""


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    # lines = read_data.splitlines()

    stones = read_data.split(" ")
    print(stones)
    cycles = 25

    for i in range(cycles):
        print(f"BLINK {i}!!!!")
        new_stones = []
        for stone in stones:
            new_stones.extend(blink(stone))

        stones = new_stones

    print(f"After {cycles} cycles, stones are now {len(stones)}")


def blink(stone):
    if stone == "0":
        return "1"
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        return stone[:mid], str(int(stone[mid:]))
    else:
        new_stone = str(int(stone) * 2024)
        return [new_stone]


if __name__ == "__main__":
    main()
