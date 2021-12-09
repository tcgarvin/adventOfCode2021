from heapq import nlargest

from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append([int(c) for c in line.strip()])
    return puzzle_input

def solve_part_1(heightmap):
    #print(heightmap)
    risk_level = 0
    for i in range(len(heightmap)):
        row = heightmap[i]
        for j in range(len(heightmap[0])):
            height = heightmap[i][j]
            if i > 0 and heightmap[i-1][j] <= height:
                continue
            if i < len(heightmap)-1 and heightmap[i+1][j] <= height:
                continue
            if j > 0 and heightmap[i][j-1] <= height:
                continue
            if j < len(row)-1 and row[j+1] <= height:
                continue

            #print(i,j,height)
            risk_level += height + 1

    return risk_level

def solve_part_2(heightmap):
    basin_sizes = []
    basin_membership = set()
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            #print("-", i,j)
            candidates = [(i,j)]
            basin_size = 0
            while len(candidates) > 0:
                candidate = candidates.pop()
                ci, cj = candidate
                #print(candidate)
                if ci < 0 or ci >= len(heightmap):
                    #print("ibounds")
                    continue
                if cj < 0 or cj >= len(heightmap[0]):
                    #print("jbounds")
                    continue
                if heightmap[ci][cj] >= 9:
                    #print("height")
                    continue
                if candidate in basin_membership:
                    #print("spoken for")
                    continue

                #print("check")
                basin_size += 1
                basin_membership.add(candidate)
                candidates.append((ci+1,cj))
                candidates.append((ci-1,cj))
                candidates.append((ci,cj+1))
                candidates.append((ci,cj-1))

            if basin_size > 0:
                basin_sizes.append(basin_size)

    #print(basin_sizes)
    largest = list(nlargest(3, basin_sizes))
    #print(largest)

    return largest[0] * largest[1] * largest[2]

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")