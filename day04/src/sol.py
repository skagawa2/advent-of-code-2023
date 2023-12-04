def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def parse_input_single_line(line: str) -> tuple[list[str], list[str]]:
    _, after_card_num = line.split(":")
    winning_numbers_str, your_numbers_str = after_card_num.split("|")
    winning_numbers = winning_numbers_str.strip().split()
    your_numbers = your_numbers_str.strip().split()
    return winning_numbers, your_numbers


def get_winning_numbers(winning_numbers: set[str], your_numbers: set[str]) -> \
        set[str]:
    your_winning_numbers = set(winning_numbers).intersection(set(your_numbers))
    return your_winning_numbers


def solution_part1(lines: list[str]) -> int:
    score = 0
    for line in lines:
        winning_numbers, your_numbers = parse_input_single_line(line)
        your_winning_numbers = \
            get_winning_numbers(winning_numbers, your_numbers)
        num_winning_numbers = len(your_winning_numbers)
        if num_winning_numbers > 0:
            score += 2 ** (num_winning_numbers - 1)
    return score


def solution_part2(lines: list[str]) -> int:
    num_cards = [1 for _ in lines]
    for curr_card, line in enumerate(lines):
        winning_numbers, your_numbers = parse_input_single_line(line)
        your_winning_numbers = \
            get_winning_numbers(winning_numbers, your_numbers)
        for card in range(curr_card + 1,
                          curr_card + 1 + len(your_winning_numbers)):
            num_cards[card] += num_cards[curr_card]
    return sum(num_cards)


if __name__ == "__main__":
    input = read_input("inputs/input.txt")
    print(f"{solution_part1(input)=}")
    print(f"{solution_part2(input)=}")
