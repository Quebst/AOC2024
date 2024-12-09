from itertools import combinations

# 301 answer
raw_data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

raw2_data = """A.A
...
A.A"""

def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()

    antinodes = set()
    ants = {}
    height = len(lines)
    width = len(lines[0])


    for x,line in enumerate(lines):
        for y, c in enumerate(line):
            if c != ".":
                loc = [x, y]
                if c not in ants:
                    ants[c] = [loc]
                else:
                    ants[c].append(loc)


    # two - one = diff, two + diff, one - diff are antinodes
    for key in ants:
        combos = tuple(combinations(ants[key], 2))
        for com in combos:
            #cone = com[0]
            #ctwo = com[1]
            cone, ctwo = sorted(com)
            delta = [ctwo[0] - cone[0], ctwo[1] - cone[1]]
            anode_one = tuple([ctwo[0] + delta[0], ctwo[1] + delta[1]])
            anode_two = tuple([cone[0] - delta[0], cone[1] - delta[1]])

            if height > anode_one[0] >= 0 and width > anode_one[1] >= 0:
                antinodes.add(anode_one)
            if height > anode_two[0] >= 0 and width > anode_two[1] >= 0:
                antinodes.add(anode_two)

            #print(f"anode_one: {anode_one}  anode_two {anode_two}")
    
    #print(antinodes)
    print(f"Locations: {len(antinodes)}")
    
if __name__ == "__main__":
    main()