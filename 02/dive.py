from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            direction, amount = line.split()
            puzzle_input.append((direction, int(amount)))
    return puzzle_input

def solve_part_1(puzzle_input):
    forward = 0
    depth = 0
    for direction, amount in puzzle_input:
        if direction == "forward":
            forward += amount
        elif direction == "down":
            depth += amount
        elif direction == "up":
            depth -= amount


    return forward * depth

def solve_part_2(puzzle_input):
    forward = 0
    depth = 0
    aim = 0
    for direction, amount in puzzle_input:
        if direction == "forward":
            forward += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return forward * depth

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")