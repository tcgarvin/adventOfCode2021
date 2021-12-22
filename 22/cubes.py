from collections import defaultdict
import re
from rich import print

def get_puzzle_input():
    commands = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            match = re.search("x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)", line)
            on = line.startswith("on")
            xrange = sorted((int(match.group(1)), int(match.group(2))))
            yrange = sorted((int(match.group(3)), int(match.group(4))))
            zrange = sorted((int(match.group(5)), int(match.group(6))))
            commands.append((on, xrange, yrange, zrange))
    return commands

def solve_part_1(commands):
    cubes = defaultdict(bool)
    i = 0
    for on, xrange, yrange, zrange in commands:
        print (i)

        for x in range(xrange[0], xrange[1]+1):
            if x > 50 or x < -50:
                continue
            for y in range(yrange[0], yrange[1]+1):
                if y > 50 or y < -50:
                    continue
                for z in range(zrange[0], zrange[1]+1):
                    if z > 50 or z < -50:
                        continue
                    cubes[(x,y,z)] = on

        i += 1
    return sum(cubes.values())

def solve_part_2(puzzle_input):
    return ""

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")