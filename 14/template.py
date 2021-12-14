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

def solve_part_1(template, rules):
    state = list(template)
    #print(state)
    for turn in range(10):
        next_state = []
        for i in range(len(state) - 1):
            pair = tuple(state[i:i+2])
            next_state.append(state[i])
            if pair in rules:
                next_state.append(rules[pair])
        
        next_state.append(state[-1])
        state = next_state
        #print(turn, state)

    most_common_count = 0
    least_common_count = 100000000000
    for c in set(state):
        count = state.count(c)
        if count > most_common_count:
            most_common_count = count
        elif count < least_common_count:
            least_common_count = count

    return most_common_count - least_common_count

def solve_part_2(initial_state, rules):
    pairs = defaultdict(int)
    for i in range(len(initial_state)-1):
        pair = tuple(initial_state[i:i+2])
        pairs[pair] += 1

    for turn in range(40):
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
    letter_counts[initial_state[-1]] += 1

    most_common_count = 0
    least_common_count = 100000000000000000
    for count in letter_counts.values():
        if count > most_common_count:
            most_common_count = count
        elif count < least_common_count:
            least_common_count = count

    return most_common_count - least_common_count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: {answer_2}")