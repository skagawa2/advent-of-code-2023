import re
from collections import defaultdict
from termcolor import colored, cprint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_input() -> list[str]:
    with open("inputs/input.txt", "r") as f:
        return f.readlines()


def find_all_numbers(lines: list[str], debug: bool = False) -> \
        list[tuple[tuple[int, int], tuple[int, int]], int]:
    answer = []
    for idx, single_line in enumerate(lines):
        for match in re.finditer(r"[0-9]+", single_line):
            if debug:
                print(f"{match.span()=} {match=}")
            beginning, end = match.span()
            answer.append((((idx, beginning), (idx, end - 1)),
                           int(match.group())))
    return answer


def find_all_symbols(lines: list[str], debug: bool = False) -> \
        list[tuple[int, int]]:
    answer = []
    for idx, single_line in enumerate(lines):
        for match in re.finditer(r"[^0-9\.]", single_line.strip()):
            beginning, _ = match.span()
            answer.append((idx, beginning))
    return answer


def solution_part1(lines: list[str], debug: bool = False):
    symbol_positions = find_all_symbols(lines)
    number_positions = find_all_numbers(lines)
    sum_of_parts = 0
    if debug:
        colored_lines = lines.copy()
        # number_chars_added = defaultdict(int)
    for (symbol_row, symbol_idx) in symbol_positions:
        for ((number_row, number_beginning),
                (_, number_end)), number in number_positions:
            if abs(number_row - symbol_row) <= 1 and \
                    symbol_idx >= number_beginning - 1 and \
                    symbol_idx <= number_end + 1:
                # this number has a symbol near it
                if debug:
                    print(f"{number} at ({number_row},"
                          f"{number_beginning}-{number_end}) "
                          f"has a symbol nearby at ({symbol_row},{symbol_idx})")
                    # colored_lines[number_row] = \
                    #     line[:(number_beginning+number_chars_added[row])] + \
                    #     bcolors.OKGREEN + \
                    #     line[(number_beginning+number_chars_added[row]):
                    #          (number_end+1+number_chars_added[row])] + \
                    #     bcolors.ENDC + \
                    #     line[(number_end+1+number_chars_added[row]):]
                    # number_chars_added[row] += 9
                    n = 1
                    string_context = lines[number_row][max(0, number_beginning-n):min(len(lines[number_row]), number_end+1+n)]
                    colored_str = colored(str(number), "red")
                    new_string_context = string_context.replace(str(number), colored_str, 1)
                    line = colored_lines[number_row].replace(string_context, new_string_context, 1)
                    colored_lines[number_row] = line
                sum_of_parts += number
    if debug:
        for line in colored_lines:
            print(line.strip())
    return sum_of_parts


if __name__ == "__main__":
    input = get_input()
    print(f"{solution_part1(input, debug=True)=}")
    # print(f"{solution_part2(input)=}")
