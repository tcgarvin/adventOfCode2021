from heapq import nlargest

from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append([int(c) for c in line.strip()])
    return puzzle_input

def solve_part_1(puzzle_input):
    #print(puzzle_input)
    risk_level = 0
    for i in range(len(puzzle_input)):
        row = puzzle_input[i]
        for j in range(len(puzzle_input[0])):
            level = puzzle_input[i][j]
            if i > 0 and puzzle_input[i-1][j] <= level:
                continue
            if i < len(puzzle_input)-1 and puzzle_input[i+1][j] <= level:
                continue
            if j > 0 and puzzle_input[i][j-1] <= level:
                continue
            if j < len(row)-1 and row[j+1] <= level:
                continue

            #print(i,j,level)
            risk_level += level + 1

    return risk_level

def solve_part_2(puzzle_input):
    basin_sizes = []
    basin_membership = {}
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[0])):
            #print("-", i,j)
            candidates = [(i,j)]
            basin_size = 0
            while len(candidates) > 0:
                candidate = candidates.pop()
                ci, cj = candidate
                #print(candidate)
                if ci < 0 or ci >= len(puzzle_input):
                    #print("ibounds")
                    continue
                if cj < 0 or cj >= len(puzzle_input[0]):
                    #print("jbounds")
                    continue
                if puzzle_input[ci][cj] >= 9:
                    #print("level")
                    continue
                if candidate in basin_membership:
                    #print("spoken for")
                    continue

                #print("check")
                basin_size += 1
                basin_membership[candidate] = True
                candidates.append((ci+1,cj))
                candidates.append((ci-1,cj))
                candidates.append((ci,cj+1))
                candidates.append((ci,cj-1))

            if basin_size > 0:
                basin_sizes.append(basin_size)

    #print(basin_sizes)
    largest = list(nlargest(3, basin_sizes))
    print(largest)

    return largest[0] * largest[1] * largest[2]

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")