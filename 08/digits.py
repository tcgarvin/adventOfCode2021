from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            inputs, outputs = line.strip().split("|")
            inputs = inputs.split(" ")
            outputs = outputs.split(" ")
            puzzle_input.append((inputs, outputs))
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

def solve_part_2(puzzle_input):
    total = 0
    for inputs, outputs in puzzle_input:
        decoder = {}
        right_side = None
        a = None
        b = None
        c = None
        d = None
        e = None
        f = None
        while len(decoder) < 9:
            for input in inputs:
                if norm(input) in decoder:
                    continue

                if len(input) == 2:
                    right_side = set(input)
                    decoder[norm(input)] = 1

                elif len(input) == 3 and right_side is not None:
                    a = set(input).difference(right_side).pop()
                    decoder[norm(input)] = 7

                elif len(input) == 6 and right_side is not None and len(right_side.difference(input)) == 1:
                    c = right_side.difference(input).pop()
                    f = right_side.difference(set([c])).pop()
                    decoder[norm(input)] = 6

                elif len(input) == 5 and c is not None and c not in input:
                    e = set("abcdefg").difference(input).difference([c]).pop()
                    decoder[norm(input)] = 5

                elif len(input) == 5 and c is not None and c in input and e is not None and e in input and f is not None and f not in input:
                    b = set("abcdefg").difference(input).difference([f]).pop()
                    decoder[norm(input)] = 2

                elif len(input) == 7:
                    decoder[norm(input)] = 8

                elif len(input) == 5 and c is not None and c in input and f is not None and f in input and b is not None and b not in input:
                    e = set("abcdefg").difference(input).difference([b]).pop()
                    decoder[norm(input)] = 3

                elif len(input) == 6 and e is not None and e not in input:
                    decoder[norm(input)] = 9

                elif len(input) == 4:
                    decoder[norm(input)] = 4

        print(decoder)

        decoded_value = 0
        for i, output in enumerate(outputs):
            power = 4 - i
            decoded_value += decoder.get(norm(output), 0) * (10**power)
            print(output, decoded_value)

        total += decoded_value
    return total

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")