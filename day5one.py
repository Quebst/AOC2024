import pprint

raw_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    a, b = raw_data.split("\n\n")
    pairs = a.splitlines()
    orders = b.splitlines()
    score = 0

    # rules is a dictionary, key is 2 digit number, values are (before, after)
    rules = {}
    for i in range(100):
        rules[i] = ([], [])

    for pair in pairs:
        first, second = map(int, pair.split("|"))
        rules[first][1].append(second)
        rules[second][0].append(first)

    for order in orders:
        score += check_order(order, rules)

    print(f"Score total is {score}")


def check_order(order, rules):
    pages = list(map(int, order.split(",")))
    length = len(pages)

    # i will be index of current page, j will be page to compare to
    for i in range(length):
        cursor = pages[i]
        for j in range(length):
            if i < j:
                if pages[j] not in rules[cursor][1]:
                    return 0
            if j < i:
                if pages[j] not in rules[cursor][0]:
                    return 0

    return pages[length // 2]


if __name__ == "__main__":
    main()
