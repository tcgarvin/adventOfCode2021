from functools import reduce
from rich import print

def get_puzzle_input():
    with open("input.txt") as input_txt:
        dots = set()
        folds = []
        for line in input_txt:
            if "," in line:
                coordinates = tuple(int(x) for x in line.strip().split(","))
                dots.add(coordinates)
            elif "=" in line:
                axis, coord = line.strip().split(" ")[-1].split("=")
                folds.append((axis, int(coord)))
    return (dots, folds)

def fold_paper(dots, fold):
    axis, coord = fold
    folded = set()
    for x,y in dots:
        if axis == "x" and x > coord:
            x = coord - (x - coord)
        elif axis == "y" and y > coord:
            y = coord - (y - coord)
        folded.add((x,y))
    return folded

def solve_part_1(dots, folds):
    return len(fold_paper(dots, folds[0]))

def solve_part_2(dots, folds):
    dots = reduce(fold_paper, folds, dots)
    for y in range(7):
        for x in range(40):
            dot = "#" if (x,y) in dots else " "
            print(dot, end="")
        print("")

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    print(f"Part 2:")
    solve_part_2(*puzzle_input)