from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        dots = set()
        folds = []
        mode = 'dots'
        for line in input_txt:
            if "," in line:
                coordinates = tuple(int(x) for x in line.strip().split(","))
                dots.add(coordinates)
            elif "=" in line:
                axis, coord = line.strip().split(" ")[-1].split("=")
                folds.append((axis, int(coord)))
    return (dots, folds)

def solve_part_1(dots, folds):
    fold = folds[0]
    #print(fold)

    # Hack: I already know it's over the x axis
    x_coord = fold[1]
    #print(x_coord)

    new_dots = set()
    for x,y in dots:
        if x > x_coord:
            x = x_coord - (x - x_coord)

        new_dots.add((x,y))
    return len(new_dots)

def solve_part_2(dots, folds):
    for axis, coord in folds:
        next_dots = set()
        for x,y in dots:
            if axis == "x" and x > coord:
                x = coord - (x - coord)
            elif axis == "y" and y > coord:
                y = coord - (y - coord)

            next_dots.add((x,y))

        dots = next_dots

    for y in range(10):
        for x in range(50):
            if (x,y) in dots:
                print("#",end="")
            else:
                print(" ", end="")

        print("")

    return ""

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: {answer_2}")