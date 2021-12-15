from collections import defaultdict
from heapq import heappush, heappop, heappushpop
from rich import print

def get_puzzle_input():
    puzzle_input = {}
    with open("input.txt") as input_txt:
        for j, line in enumerate(input_txt):
            for i, c in enumerate(line.strip()):
                puzzle_input[(i,j)] = int(c)
    return puzzle_input

def solve_part_1(puzzle_input):
    heap = [(0,(0,0))]
    location_costs = defaultdict(lambda: float('inf'))
    while len(heap) > 0:
        current_cost, coords = heappop(heap)
        i,j = coords
        for neighbor in ((i,j+1), (i, j-1), (i+1, j), (i-1, j)):
            if neighbor not in puzzle_input:
                continue

            neighbor_cost = current_cost + puzzle_input[neighbor]
            if neighbor_cost < location_costs[neighbor]:
                location_costs[neighbor] = neighbor_cost
                heappush(heap, (neighbor_cost, neighbor))

    return location_costs[max(location_costs.keys())]
            

def solve_part_2(puzzle_input):
    puzzle_input_width, puzzle_input_height = max(puzzle_input.keys())
    puzzle_input_height += 1
    puzzle_input_width += 1

    print(puzzle_input_width, puzzle_input_height)

    whole_map = puzzle_input.copy()
    for dj in range(5):
        for di in range(5):
            addition = dj + di
            if addition == 0:
                continue

            for (i,j), cost in puzzle_input.items():
                new_cost = cost + addition
                if new_cost > 9:
                    new_cost -= 9
                whole_map[(i+(di*puzzle_input_width), j+(dj*puzzle_input_height))] = new_cost

    print(max(whole_map.keys()))

    heap = [(0,(0,0))]
    location_costs = defaultdict(lambda: float('inf'))
    while len(heap) > 0:
        current_cost, coords = heappop(heap)
        i,j = coords
        for neighbor in ((i,j+1), (i, j-1), (i+1, j), (i-1, j)):
            if neighbor not in whole_map:
                continue

            neighbor_cost = current_cost + whole_map[neighbor]
            if neighbor_cost < location_costs[neighbor]:
                location_costs[neighbor] = neighbor_cost
                heappush(heap, (neighbor_cost, neighbor))

    return location_costs[max(location_costs.keys())]

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")