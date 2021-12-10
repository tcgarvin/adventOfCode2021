from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line.strip())
    return puzzle_input

scores = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

def solve_part_1(puzzle_input):
    score = 0
    for line in puzzle_input:
        open_chunks = []
        for c in line:
            closable = open_chunks[-1] if len(open_chunks) > 0 else None
            if c in '[{(<':
                open_chunks.append(c)
            elif closable == "<" and c == ">":
                open_chunks.pop()
            elif closable == "{" and c == "}":
                open_chunks.pop()
            elif closable == "(" and c == ")":
                open_chunks.pop()
            elif closable == "[" and c == "]":
                open_chunks.pop()
            else:
                score += scores[c]
                break

    return score

completion_scores = {
    "(":1,
    "[":2,
    "{":3,
    "<":4
}

def solve_part_2(puzzle_input):
    line_scores = []
    for line in puzzle_input:
        corrupt = False
        open_chunks = []
        for c in line:
            closable = open_chunks[-1] if len(open_chunks) > 0 else None
            if c in '[{(<':
                open_chunks.append(c)
            elif closable == "<" and c == ">":
                open_chunks.pop()
            elif closable == "{" and c == "}":
                open_chunks.pop()
            elif closable == "(" and c == ")":
                open_chunks.pop()
            elif closable == "[" and c == "]":
                open_chunks.pop()
            else:
                corrupt = True
                break

        if corrupt:
            continue

        score = 0
        for chunk_symbol in reversed(open_chunks):
            score = score * 5 + completion_scores[chunk_symbol]

        line_scores.append(score)

    line_scores.sort()
    middle_score = line_scores[len(line_scores) // 2]
    return middle_score

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")