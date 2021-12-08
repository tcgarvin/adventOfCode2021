from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            patterns, outputs = line.strip().split("|")
            patterns = patterns.split(" ")
            outputs = outputs.strip().split(" ")
            puzzle_input.append((patterns, outputs))
    return puzzle_input

def solve_part_1(puzzle_input):
    count = 0
    for _, outputs in puzzle_input:
        for output in outputs:
            if len(output) in (2,3,4,7):
                #print(f'"{output}"')
                count += 1

    return count

def norm(letters):
    return "".join(sorted(letters))

ALL_SEGMENTS = set("abcdefg")
def solve_part_2(puzzle_input):
    total = 0
    for patterns, outputs in puzzle_input:
        decoder = {}
        right_side = None
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None
        while len(decoder) < 9:
            for pattern in patterns:
                # Sort the letters in the pattern so we match up well to the output later
                pattern = norm(pattern)
                if pattern in decoder:
                    continue

                if len(pattern) == 2:
                    right_side = set(pattern)
                    decoder[pattern] = 1

                elif len(pattern) == 3 and right_side is not None:
                    a = set(pattern).difference(right_side).pop()
                    decoder[pattern] = 7

                elif len(pattern) == 6 and right_side is not None and len(right_side.difference(pattern)) == 1:
                    c = right_side.difference(pattern).pop()
                    f = right_side.difference(set([c])).pop()
                    decoder[pattern] = 6

                elif len(pattern) == 5 and c is not None and c not in pattern:
                    e = ALL_SEGMENTS.difference(pattern).difference([c]).pop()
                    decoder[pattern] = 5

                elif len(pattern) == 5 and c is not None and c in pattern and e is not None and e in pattern and f is not None and f not in pattern:
                    b = ALL_SEGMENTS.difference(pattern).difference([f]).pop()
                    decoder[pattern] = 2

                elif len(pattern) == 7:
                    decoder[pattern] = 8

                elif len(pattern) == 5 and c is not None and c in pattern and f is not None and f in pattern and b is not None and b not in pattern:
                    e = ALL_SEGMENTS.difference(pattern).difference([b]).pop()
                    decoder[pattern] = 3

                elif len(pattern) == 6 and e is not None and e not in pattern:
                    decoder[pattern] = 9

                elif len(pattern) == 4:
                    decoder[pattern] = 4

        #print(decoder)

        decoded_value = 0
        for i, output in enumerate(outputs):
            power = 3 - i
            # Note we didn't capture '0' above, so that's the default (missing) case here
            decoded_value += decoder.get(norm(output), 0) * (10**power)
            #print(output, decoded_value, power)

        total += decoded_value
    return total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")