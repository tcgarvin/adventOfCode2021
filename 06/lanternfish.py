from collections import defaultdict
from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.extend([int(n) for n in line.split(",")])
    return puzzle_input

def solve_part_1(puzzle_input):
    ages = puzzle_input
    for i in range(80):
        next_ages = []
        for age in ages:
            if age == 0:
                next_ages.append(6)
                next_ages.append(8)

            else:
                next_ages.append(age - 1)

        ages = next_ages
    return len(ages)

def solve_part_2(puzzle_input):
    age_buckets = defaultdict(int)
    for age in puzzle_input:
        age_buckets[age] += 1

    for i in range(256):
        #print(age_buckets)
        #print(i, sum(age_buckets.values()))
        next_age_buckets = defaultdict(int)
        for i in range(9):
            fish_of_age = age_buckets.get(i, 0)
            if i == 0:
                next_age_buckets[8] += fish_of_age
                next_age_buckets[6] += fish_of_age

            else:
                next_age_buckets[i - 1] += fish_of_age

        age_buckets = next_age_buckets
    return sum(age_buckets.values())

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")