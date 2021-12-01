from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(int(line))
    return puzzle_input

def solve_part_1(puzzle_input):
    count = 0
    for i, reading in enumerate(puzzle_input):
        if i == 0:
            continue

        if reading > puzzle_input[i-1]:
            count += 1
    return count

def solve_part_2(puzzle_input):
    prev = 100000000
    count = 0
    for i in range(2, len(puzzle_input)):
        total = puzzle_input[i] + puzzle_input[i-1] + puzzle_input[i-2]
        if total > prev:
            count += 1
        prev = total
    return count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")