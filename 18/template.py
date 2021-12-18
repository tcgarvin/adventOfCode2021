from functools import reduce
from itertools import permutations
import json
from math import ceil, perm
from rich import print

def make_number(list_represenation, parent=None):
    if type(list_represenation) == int:
        return RegularNumber(list_represenation, parent)
    else:
        return SnailNumber(list_represenation, parent)

class SnailNumber():
    def __init__(self, list_representation, parent):
        self.parent = parent
        self.left = make_number(list_representation[0], self)
        self.right = make_number(list_representation[1], self)


    def is_pair(self):
        return True


    def can_explode(self):
        nested_level = 0
        curs = self
        while curs.parent is not None:
            curs = curs.parent
            nested_level += 1
        result = nested_level == 4

        #print(result, nested_level, self)
        return result


    def magnitude(self):
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()

    
    def __str__(self):
        return f"[{self.left},{self.right}]"


class RegularNumber(SnailNumber):
    def __init__(self, list_represenation, parent):
        self.parent = parent
        self.value = list_represenation

    def is_pair(self):
        return False

    def magnitude(self):
        return self.value

    def __str__(self):
        return str(self.value)


def try_explode(snail_number_root):
    leaves = []
    nodes_to_visit = [snail_number_root]
    exploding_node = None
    while len(nodes_to_visit) > 0:
        curs = nodes_to_visit.pop()

        if type(curs) == RegularNumber:
            leaves.append(curs)
            continue

        nodes_to_visit.append(curs.right)
        nodes_to_visit.append(curs.left)
        if exploding_node is None and curs.can_explode():
            exploding_node = curs
            #print("Explode", exploding_node)

    if exploding_node is not None:
        left_index = leaves.index(exploding_node.left)
        if left_index > 0:
            #print(leaves[left_index - 1].value)
            #print(exploding_node.left.value)
            leaves[left_index - 1].value += exploding_node.left.value

        right_index = left_index + 1
        if right_index < len(leaves) - 1:
            #print(leaves[right_index+1].value) 
            #print(exploding_node.right.value)
            leaves[right_index+1].value += exploding_node.right.value

        parent = exploding_node.parent
        if parent.left is exploding_node:
            parent.left = RegularNumber(0, parent)
        elif parent.right is exploding_node:
            parent.right = RegularNumber(0, parent)
        else:
            raise Exception("could not replace exploding node")

    return exploding_node is not None
        

def try_split(snail_number_root):
    nodes_to_visit = [snail_number_root]
    while len(nodes_to_visit) > 0:
        curs = nodes_to_visit.pop()

        if type(curs) == RegularNumber and curs.value >= 10:
            parent = curs.parent
            if parent.left is curs:
                parent.left = SnailNumber([curs.value // 2, ceil(curs.value / 2)], parent)
            elif parent.right is curs:
                parent.right = SnailNumber([curs.value // 2, ceil(curs.value / 2)], parent)
            return True
        elif type(curs) == RegularNumber:
            continue

        nodes_to_visit.append(curs.right)
        nodes_to_visit.append(curs.left)

    return False

def reduce_snail_number(snail_number):
    # destructive
    try_action = True
    while try_action:
        try_action = try_explode(snail_number) or try_split(snail_number)
    return snail_number

def add(a,b):
    total = SnailNumber([0,0], None)
    total.left = a
    total.right = b
    a.parent = total
    b.parent = total
    return reduce_snail_number(total)

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(json.loads(line))
    return puzzle_input

def solve_part_1(puzzle_input):
    total = reduce(add,[make_number(j) for j in puzzle_input])
    print(total)
    return total.magnitude()

def solve_part_2(puzzle_input):
    return max(add(make_number(a),make_number(b)).magnitude() for a,b in permutations(puzzle_input,2))

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    puzzle_input = get_puzzle_input()
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")