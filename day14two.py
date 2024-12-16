import time
import re
#from quickGraph import quick_graph

# 6355

raw_data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

raw2_data = """p=2,4 v=2,-3"""

#HEIGHT = 7
#WIDTH = 11

HEIGHT = 103
WIDTH = 101

def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
        lines = read_data.splitlines()
        bots = []
        pattern = r"p=([\d,-]+) v=([\d,-]+)"
        seconds = 6355

        for line in lines:
            match = re.search(pattern, line)
            if match:
                position = match.group(1).split(",")
                velocity = match.group(2).split(",")
                bot = Robot(position, velocity)
                bots.append(bot)
            else:
                raise ValueError("Match not found on input")


        potents = []
        low_score = 11111111111111111111
        for i in range(seconds):
            for bot in bots:
                bot.tick()
            current = safety(bots)
            if current < low_score:
                print(f"Seconds {i} for current {current}")
                low_score = current


        print(f"Total safety score is {safety(bots)}")

        grid = [["." for _ in range(WIDTH)] for col in range(HEIGHT)]
        for bot in bots:
            grid[bot.position[1]][bot.position[0]] = "#"

        grid_print(grid)
        print(f"Finished in {time.time() - start_time}")

def grid_print(grid):
    for row in grid:
        print(row)

def safety(bots):
    one, two, three, four = 0, 0, 0, 0
    half_height = HEIGHT // 2
    half_width = WIDTH // 2

    for bot in bots:
        if bot.position[0] == half_width or bot.position[1]  == half_height:
            continue
        elif bot.position[0] < half_width:
            if bot.position[1] < half_height:
                one += 1
            else:
                two += 1
        else:
            if bot.position[1] < half_height:
                three += 1
            else:
                four +=1
    
    return one * two * three * four
    

# position 0 is row, position 1 is col (x goes right, y goes down)
class Robot:
    def __init__(self, position, velocity):
        self.position = [int(position[0]), int(position[1])]
        self.velocity = [int(velocity[0]), int(velocity[1])]

    def __str__(self):
        return f"Robot has position: {self.position} and velocity {self.velocity}"

    def tick(self):
        self.position[0] = (self.position[0] + self.velocity[0]) % WIDTH
        self.position[1] = (self.position[1] + self.velocity[1]) % HEIGHT
        



if __name__ == "__main__":
    main()
