from collections import defaultdict
from rich import print

def get_puzzle_input():
    puzzle_input = defaultdict(set)
    with open("input.txt") as input_txt:
        for line in input_txt:
            nodes = line.strip().split("-")
            puzzle_input[nodes[0]].add(nodes[1])
            puzzle_input[nodes[1]].add(nodes[0])
    return puzzle_input

def traverse(neighbors, node, visited):
    if node == "end":
        return 1

    paths = 0
    next_visited = visited.copy()
    next_visited.add(node)
    for candidate_next in neighbors[node]:
        if candidate_next in visited and not candidate_next.isupper():
            continue
        paths += traverse(neighbors, candidate_next, next_visited)
    return paths

def solve_part_1(neighbors):
    return traverse(neighbors, "start", set())

def traverse_with_double(neighbors, node, lower_visited):
    if node == "end":
        return 1

    next_visited = lower_visited.copy()
    if node.islower():
        next_visited[node] = next_visited.get(node, 0) + 1

    have_done_double_already = any(visits >= 2 for visits in next_visited.values())
    paths = 0
    for candidate_next in neighbors[node]:
        if candidate_next == "start":
            continue
        elif next_visited.get(candidate_next,0) >= 1 and have_done_double_already:
            continue
        paths += traverse_with_double(neighbors, candidate_next, next_visited)
    return paths

def solve_part_2(neighbors):
    return traverse_with_double(neighbors, "start", {})

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")