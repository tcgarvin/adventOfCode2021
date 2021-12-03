from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line.strip())
    return puzzle_input

def solve_part_1(puzzle_input):
    bit_ones_count = [0] * len(puzzle_input[0])
    for binary_string in puzzle_input:
        for i, one_or_zero in enumerate(binary_string):
            bit_ones_count[i] += int(one_or_zero)

    gamma_string = ""
    epsilon_string = ""
    for bit in bit_ones_count:
        if bit > (len(puzzle_input) / 2):
            gamma_string = gamma_string + "1"
            epsilon_string = epsilon_string + "0"
        else:
            gamma_string = gamma_string + "0"
            epsilon_string = epsilon_string + "1"

    #print(gamma_string)

    gamma = int(gamma_string, base=2)
    epsilon = int(epsilon_string, base=2)

    #print(gamma)
    #print(epsilon)

    return gamma * epsilon

def filter_numbers(numbers, use_most_common, bit=0):
    assert len(numbers) != 0
    if len(numbers) == 1:
        return numbers[0]

    ones_count = 0
    for number in numbers:
        ones_count += int(number[bit])

    # Using equality between ints and floats from division, careful.
    most_common = 1 if ones_count >= (len(numbers) / 2) else 0
    target_value = most_common if use_most_common else (most_common + 1) % 2
    target_value = str(target_value)

    #print(target_value)

    filtered = [n for n in numbers if n[bit] == target_value]
    return filter_numbers(filtered, use_most_common, bit=bit+1)

def solve_part_2(puzzle_input):
    oxygen_rating = int(filter_numbers(puzzle_input, True), base=2)
    co2_rating = int(filter_numbers(puzzle_input, False), base=2)
    return oxygen_rating * co2_rating

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")