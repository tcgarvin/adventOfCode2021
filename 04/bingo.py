from rich import print

class Board:
    def __init__(self):
        self._numbers = []
        self._hits = [[0] * 5 for _ in range(5)]
        self._membership = set()


    def add_row(self, numbers):
        self._numbers.append(numbers)
        self._membership.update(numbers)


    def is_bingo(self):
        for i in range(5):
            row_qualifies = True
            column_qualifies = True
            for j in range(5):
                row_qualifies = row_qualifies and self._hits[i][j] == 1
                column_qualifies = column_qualifies and self._hits[j][i] == 1

            if row_qualifies or column_qualifies:
                return True

        return False


    def mark(self, number):
        if number in self._membership:
            for i in range(5):
                for j in range(5):
                    if self._numbers[i][j] == number:
                        self._hits[i][j] = 1
                        break
            return True
        return False


    def score(self, winning_number):
        total = 0
        for i in range(5):
            for j in range(5):
                if self._hits[i][j] == 0:
                    total += self._numbers[i][j]

        return total * winning_number


def get_puzzle_input():
    with open("input.txt") as input_txt:
        numbers = []
        boards = []
        first_line = True
        for line in input_txt:
            if first_line:
                numbers = [int(x) for x in line.split(",")]
                first_line = False
                continue

            if line.strip() == "":
                board = None
            elif board is None:
                board = Board()
                boards.append(board)
                board.add_row([int(x) for x in line.split()])
            else:
                board.add_row([int(x) for x in line.split()])

    return numbers, boards


def solve_part_1(numbers, boards):
    for number in numbers:
        for board in boards:
            has_number = board.mark(number)
            if has_number and board.is_bingo():
                return board.score(number)
    return "No winner"


def solve_part_2(numbers, boards):
    for number in numbers:
        for board in boards:
            has_number = board.mark(number)
            if has_number and len(boards) == 1 and board.is_bingo():
                return board.score(number)

        boards = [board for board in boards if not board.is_bingo()]
    return "No last board"

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(*puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(*puzzle_input)
    print(f"Part 2: {answer_2}")