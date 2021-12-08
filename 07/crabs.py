from rich import print
from statistics import mean

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.extend(list(map(int,line.split(","))))
    return puzzle_input

def cost_to_target(locations, target):
    return sum((abs(location - target) for location in locations))

def solve_part_1(puzzle_input):
    # The cheapest route is probably the average, right?
    target = int(mean(puzzle_input))

    best_cost = 100000000000
    for i in range(target * 10):
        cost = cost_to_target(puzzle_input, i)
        best_cost = min(cost, best_cost)

    return best_cost

def solve_part_2(puzzle_input):
    # The cheapest route is probably the average, right?
    target = int(mean(puzzle_input))

    best_cost = 100000000000
    for i in range(target * 10):
        cost = sum(((abs(location - target) + 1) * abs(location - target) // 2 for location in puzzle_input))
        best_cost = min(cost, best_cost)

    return best_cost

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")