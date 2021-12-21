from collections import defaultdict
from rich import print

def parse_char(c):
    return 1 if c == "#" else 0

def get_puzzle_input():
    algorithm = ""
    image = defaultdict(int)
    with open("input.txt") as input_txt:
        for line_num, line in enumerate(input_txt):
            if line_num == 0:
                algorithm = list(map(parse_char, line.strip()))

            elif line_num == 1:
                continue

            else:
                y = line_num - 2
                for x, c in enumerate(line.strip()):
                    image[(x,y)] = parse_char(c)

    return algorithm, image

def view_detail(image, coordinates):
    print(coordinates)
    x,y = coordinates
    print(image[x-1,y-1], image[x, y-1], image[x+1,y-1])
    print(image[x-1,y], image[x, y], image[x+1,y])
    print(image[x-1,y+1], image[x, y+1], image[x+1,y+1])
    

def enhance_image(image, algorithm):
    default_color = image.default_factory()
    result = defaultdict(lambda: int(not default_color))
    upper_left = min(image.keys())
    lower_right = max(image.keys())
    #print(upper_left, lower_right)
    for x in range(upper_left[0]-1, lower_right[0]+2):
        for y in range(upper_left[1]-1, lower_right[1]+2):
            #print(x,y)
            index = 0
            index += image[(x-1,y-1)] * 2 ** 8
            index += image[(x,y-1)] * 2 ** 7
            index += image[(x+1,y-1)] * 2 ** 6
            index += image[(x-1,y)] * 2 ** 5
            index += image[(x,y)] * 2 ** 4
            index += image[(x+1,y)] * 2 ** 3
            index += image[(x-1,y+1)] * 2 ** 2
            index += image[(x,y+1)] * 2 ** 1
            index += image[(x+1,y+1)] * 2 ** 0
            result[(x,y)] = algorithm[index]
        #view_detail(image, (x,y))
        #print(index, algorithm[index-1:index+2])

    
    return result

def solve_part_1(algorithm, image):
    #print(algorithm)
    #print(image)
    iteration_1 = enhance_image(image, algorithm)
    iteration_2 = enhance_image(iteration_1, algorithm)

    lit_pixels = sum(iteration_2.values())
    return lit_pixels


def solve_part_2(algorithm, image):
    for _ in range(50):
        image = enhance_image(image, algorithm)
    lit_pixels = sum(image.values())
    return lit_pixels

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: {answer_2}")