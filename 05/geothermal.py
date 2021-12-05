from collections import defaultdict

from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            source_str, dest_str = line.split("->")
            source = tuple(map(int, source_str.split(",")))
            dest = tuple(map(int, dest_str.split(",")))
            puzzle_input.append((source, dest))
    return puzzle_input

def solve(puzzle_input, include_diagonals):
    grid = defaultdict(int)
    for source, dest in puzzle_input:
        if not include_diagonals and source[0] != dest[0] and source[1] != dest[1]:
            continue # Skip diagonal

        x_distance = dest[0] - source[0]
        dx = x_distance // abs(x_distance) if x_distance != 0 else 0

        y_distance = dest[1] - source[1]
        dy = y_distance // abs(y_distance) if y_distance != 0 else 0

        last_point = source
        grid[source] += 1
        #print(source, dest, dx, dy)
        while last_point != dest:
            next_point = (last_point[0] + dx, last_point[1] + dy)
            grid[next_point] += 1
            #print(next_point)
            last_point = next_point
    return len([v for v in grid.values() if v > 1])

def solve_part_1(puzzle_input):
    return solve(puzzle_input, include_diagonals=False)

def solve_part_2(puzzle_input):
    return solve(puzzle_input, include_diagonals=True)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")