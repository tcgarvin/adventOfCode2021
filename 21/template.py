from functools import lru_cache
from itertools import product
from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(int(line.strip().split(" ")[-1]))
    return puzzle_input

def solve_part_1(puzzle_input):
    player1_score = 0
    player2_score = 0
    player1_position = puzzle_input[0] - 1   #Zero index
    player2_position = puzzle_input[1] - 1   #Zero index
    die_rolls = 0
    while True:
        player1_position = (player1_position + (die_rolls % 100 + 1) * 3 + 3) % 10
        player1_score += player1_position + 1  # Back to one-indexed
        die_rolls += 3
        if player1_score >= 1000:
            break

        player2_position = (player2_position + (die_rolls % 100 + 1) * 3 + 3) % 10
        player2_score += player2_position + 1  # Back to one-indexed
        die_rolls += 3
        if player1_score >= 1000:
            break

    return min(player1_score, player2_score) * die_rolls

@lru_cache(maxsize=None)
def count_universes(player1_score, player2_score, player1_position, player2_position):
    if player2_score >= 21:
        return 0,1

    # It's always player 1's turn. To see player 2's turn, flip the arguments
    player1_wins = 0
    player2_wins = 0
    for rolls in product((1,2,3), repeat=3):
        q_roll_total = sum(rolls)
        q_player1_position = (player1_position + q_roll_total) % 10
        q_player1_score = player1_score + q_player1_position + 1
        # We flip player 1 and 2 in the arguments here so player2 can take their turn
        q_player2_wins, q_player1_wins = count_universes(player2_score, q_player1_score, player2_position, q_player1_position)
        player1_wins += q_player1_wins
        player2_wins += q_player2_wins

    return player1_wins, player2_wins

def solve_part_2(puzzle_input):
    player1_wins, player2_wins = count_universes(0,0,puzzle_input[0]-1, puzzle_input[1]-1)
    return max(player1_wins, player2_wins)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")