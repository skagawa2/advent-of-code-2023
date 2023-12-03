import re
from termcolor import colored


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


def solution_part1(lines: list[str], debug: bool = False) -> int:
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
                          "has a symbol nearby at "
                          f"({symbol_row},{symbol_idx})")
                    n = 1
                    string_context = lines[number_row][
                        max(0, number_beginning-n):
                        min(len(lines[number_row]), number_end+1+n)
                    ]
                    colored_str = colored(str(number), "red")
                    new_string_context = string_context \
                        .replace(str(number), colored_str, 1)
                    line = colored_lines[number_row] \
                        .replace(string_context, new_string_context, 1)
                    colored_lines[number_row] = line
                sum_of_parts += number
    if debug:
        for line in colored_lines:
            print(line.strip())
    return sum_of_parts


def find_all_gears(lines: list[str], debug: bool = False) -> \
        list[tuple[int, int]]:
    answer = []
    for idx, single_line in enumerate(lines):
        for match in re.finditer(r"\*", single_line.strip()):
            beginning, _ = match.span()
            answer.append((idx, beginning))
    return answer


def solution_part2(lines: list[str], debug: bool = False) -> int:
    gear_positions = find_all_gears(lines)
    number_positions = find_all_numbers(lines)
    sum_of_gear_ratios = 0
    if debug:
        colored_lines = lines.copy()
        # number_chars_added = defaultdict(int)
    for (gear_row, gear_idx) in gear_positions:
        parts_nearby = []
        for ((number_row, number_beginning),
                (_, number_end)), number in number_positions:
            if abs(number_row - gear_row) <= 1 and \
                    gear_idx >= number_beginning - 1 and \
                    gear_idx <= number_end + 1:
                # this part has a gear near it
                if debug:
                    print(f"{number} at ({number_row},"
                          f"{number_beginning}-{number_end}) "
                          "has a symbol nearby at "
                          f"({gear_row},{gear_idx})")
                    n = 1
                    string_context = lines[number_row][
                        max(0, number_beginning-n):
                        min(len(lines[number_row]), number_end+1+n)
                    ]
                    colored_str = colored(str(number), "red")
                    new_string_context = string_context \
                        .replace(str(number), colored_str, 1)
                    line = colored_lines[number_row] \
                        .replace(string_context, new_string_context, 1)
                    colored_lines[number_row] = line
                parts_nearby.append(number)
        if len(parts_nearby) == 2:
            # multiply gears to get gear ratio, add to running total
            sum_of_gear_ratios += parts_nearby[0] * parts_nearby[1]
    if debug:
        for line in colored_lines:
            print(line.strip())
    return sum_of_gear_ratios


if __name__ == "__main__":
    input = get_input()
    print(f"{solution_part1(input, debug=True)=}")
    print(f"{solution_part2(input, debug=True)=}")
