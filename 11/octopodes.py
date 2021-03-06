from collections import defaultdict
from rich import print

def get_puzzle_input():
    puzzle_input = defaultdict(lambda: -1000000)
    with open("input.txt") as input_txt:
        i = 0
        for i,line in enumerate(input_txt):
            for j, c in enumerate(line.strip()):
                puzzle_input[(i,j)] = int(c)
    return puzzle_input

def increment(coords,state):
    state[coords] += 1
    flashes = 0
    if state[coords] == 10:
        i,j = coords
        flashes = 1
        flashes += increment((i+1, j  ), state)
        flashes += increment((i+1, j+1), state)
        flashes += increment((i+1, j-1), state)
        flashes += increment((i-1, j  ), state)
        flashes += increment((i-1, j+1), state)
        flashes += increment((i-1, j-1), state)
        flashes += increment((i,   j+1), state)
        flashes += increment((i,   j-1), state)

    return flashes


def progress(state):
    flashes = 0
    for coords in list(state.keys()):
        flashes += increment(coords, state)

    for coords in list(state.keys()):
        if state[coords] >= 10:
            state[coords] = 0
    return flashes

def solve_part_1(puzzle_input):
    state = puzzle_input.copy()
    flashes = 0
    for turn in range(100):
        #print(turn)
        flashes += progress(state)
        #print_state(state, turn)
    return flashes

def solve_part_2(puzzle_input):
    state = puzzle_input.copy()
    turn = 1
    while True:
        flashes_this_turn = progress(state)
        if flashes_this_turn == 100:
            return turn
        #print_state(state, turn)
        turn += 1

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")