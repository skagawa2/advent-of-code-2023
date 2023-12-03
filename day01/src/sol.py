from typing import List
import re


def get_inputs() -> List[str]:
    with open("inputs/input.txt") as f:
        lines = f.readlines()
    return lines


def solution_part1_singleline(line: str, debug: bool = False) -> int:
    first_digit_str = re.search("^[a-z]*([0-9])", line).groups(1)[0]
    last_digit_str = re.search("([0-9])[a-z]*$", line).groups(1)[0]
    if debug:
        print(f"{line=} {first_digit_str=} {last_digit_str=}")
    number = int(first_digit_str + last_digit_str)
    return number


def solution_part1(singleline_values: List[str]) -> int:
    return sum([solution_part1_singleline(line) for line in singleline_values])


def number_str_to_int_str(number_str: str) -> str:
    match number_str:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9':
            return number_str
    return ""


def solution_part2_singleline(line: str, debug: bool = False) -> int:
    digits = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"
    all_digits = re.findall(digits, line)
    if debug:
        print(f"{line=} {all_digits=}")
    first_digit_number_str = all_digits[0]
    last_digit_number_str = all_digits[-1]
    first_digit_int_str = number_str_to_int_str(first_digit_number_str)
    last_digit_int_str = number_str_to_int_str(last_digit_number_str)
    number = int(first_digit_int_str + last_digit_int_str)
    return number


def solution_part2(singleline_values: List[str]) -> int:
    return sum([solution_part2_singleline(line) for line in singleline_values])


def main() -> None:
    input = get_inputs()
    print(f"{solution_part1(input)=}")
    print(f"{solution_part2(input)=}")


if __name__ == "__main__":
    main()
