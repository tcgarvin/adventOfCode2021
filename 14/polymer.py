from collections import defaultdict
from rich import print


def get_puzzle_input():
    initial_state = []
    rules = {}
    with open("input.txt") as input_txt:
        for line in input_txt:
            if len(line) > 2 and "->" not in line:
                initial_state = list(line.strip())
            if "->" in line:
                pair, insert = line.strip().split(" -> ")
                pair = tuple(pair)
                rules[pair] = insert

    return (initial_state, rules)


def polymerize(template, rules, iterations):
    pairs = defaultdict(int)
    for i in range(len(template)-1):
        pair = tuple(template[i:i+2])
        pairs[pair] += 1

    for _ in range(iterations):
        next_pairs = defaultdict(int)
        for pair, count in pairs.items():
            if pair in rules:
                insert = rules[pair]
                next_pairs[(pair[0], insert)] += count
                next_pairs[(insert, pair[1])] += count
            else:
                next_pairs[pair] += count
        pairs = next_pairs

    letter_counts = defaultdict(int)
    for pair, count in pairs.items():
        letter_counts[pair[0]] += count
    letter_counts[template[-1]] += 1

    most_common_count = 0
    least_common_count = float('inf')
    for count in letter_counts.values():
        most_common_count = max(most_common_count, count)
        least_common_count = min(least_common_count, count)
    return most_common_count - least_common_count


def solve_part_1(template, rules):
    return polymerize(template, rules, 10)


def solve_part_2(template, rules):
    return polymerize(template, rules, 40)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: {answer_2}")