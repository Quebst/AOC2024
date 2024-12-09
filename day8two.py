from itertools import combinations

# 1019 answer
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
            cone, ctwo = sorted(com)
            delta = [ctwo[0] - cone[0], ctwo[1] - cone[1]]
            antinodes.add(tuple(cone))
            antinodes.add(tuple(ctwo))
            flagone = False 
            flagtwo = False
            while True:
                
                ctwo = tuple([ctwo[0] + delta[0], ctwo[1] + delta[1]])
                cone = tuple([cone[0] - delta[0], cone[1] - delta[1]])

                if height > cone[0] >= 0 and width > cone[1] >= 0:
                    antinodes.add(cone)
                else:
                    flagone = True
                
                if height > ctwo[0] >= 0 and width > ctwo[1] >= 0:
                    antinodes.add(ctwo)
                else:
                    flagtwo = True

                if flagone and flagtwo:
                    break

            #print(f"anode_one: {anode_one}  anode_two {anode_two}")
    
    #print(sorted(antinodes))
    print(f"Locations: {len(antinodes)}")
    
if __name__ == "__main__":
    main()