import re
from rich import print

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            match = re.search("x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)", line)
            xrange = (int(match.group(1)), int(match.group(2)))
            yrange = (int(match.group(3)), int(match.group(4)))
            return xrange, yrange
    return puzzle_input

def solve_part_1(xrange, yrange):
    # Assuming we get X far enough to the left, which is an independant problem,
    # we just need velocity when the probe shoots past us downwards to be -107,
    # which will be one more than the launch velocity.  So the launch velocity
    # should be 106.  All we have to do is calculate how high that initial
    # launch velocity will take us.
    return sum(range(abs(yrange[0])))

def is_valid_velocity(vx, vy, xrange, yrange):
    x = 0
    y = 0
    while x <= xrange[1] and y >= yrange[0]:
        x += vx
        y += vy
        vx = max(vx - 1, 0)
        vy -= 1
        if x >= xrange[0] and x <= xrange[1] and y >= yrange[0] and y <= yrange[1]:
            return True

    return False
    

def solve_part_2(xrange, yrange):
    # Let's just find the bounds of all the shots that _could_ get us there, and
    # then simulate each one.  Could be more efficient, but this should be fine.

    # vX needs to be large enough to get there
    x_min = 0
    x_min_total_distance = 0
    while x_min_total_distance < xrange[0]:
        x_min += 1
        x_min_total_distance += x_min

    # vX needs to be small enough not to shoot past the range on the first shot
    x_max = xrange[1]

    # vY needs to be upwards enough that we don't shoot past the bottom of the
    # range on the first shot
    y_min = yrange[0]

    # vY needs to be downwards enough that we're not going too fast on the way
    # down (See solve_part_1)
    y_max = abs(yrange[0])-1

    print(f"Scanning from {(x_min, y_max)} to {(x_max, y_min)}, {(x_max - x_min + 1) * (y_max - y_min + 1)} initial velocities")

    valid_velocities = set()
    for vx in range(x_min, x_max+1):
        for vy in range(y_min, y_max+1):
            if is_valid_velocity(vx, vy, xrange, yrange):
                valid_velocities.add((vx,vy))
    return len(valid_velocities)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: {answer_2}")