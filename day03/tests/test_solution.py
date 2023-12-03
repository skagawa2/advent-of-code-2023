import unittest
from src.sol import solution_part1, find_all_numbers, find_all_symbols, \
    solution_part2


class TestDay03(unittest.TestCase):

    def test_find_all_numbers(self):
        input = [
            "123...123...",
            "....5.5.6..."
        ]
        answer = [
            (((0, 0), (0, 2)), 123),
            (((0, 6), (0, 8)), 123),
            (((1, 4), (1, 4)), 5),
            (((1, 6), (1, 6)), 5),
            (((1, 8), (1, 8)), 6),
        ]
        self.assertEqual(find_all_numbers(input), answer)

    def test_find_all_symbols(self):
        part1_sample_input = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ]
        answer = [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)]
        self.assertEqual(find_all_symbols(part1_sample_input), answer)

    def test_one_digit_number(self):
        input = ["..1.1",
                 ".-..."]
        self.assertEqual(find_all_symbols(input), [(1, 1)])
        self.assertEqual(find_all_numbers(input),
                         [(((0, 2), (0, 2)), 1), (((0, 4), (0, 4)), 1)])
        self.assertEqual(solution_part1(input), 1)

    def test_number_at_end_of_line(self):
        input = ["...+..",
                 ".3..11"]
        self.assertEqual(find_all_symbols(input), [(0, 3)])
        self.assertEqual(find_all_numbers(input), [(((1, 1), (1, 1)), 3),
                                                   (((1, 4), (1, 5)), 11)])
        self.assertEqual(solution_part1(input), 11)

    def test_newlines_arent_symbols(self):
        input = ["...+..\n",
                 ".3..11"]
        self.assertEqual(find_all_symbols(input), [(0, 3)])
        self.assertEqual(find_all_numbers(input), [(((1, 1), (1, 1)), 3),
                                                   (((1, 4), (1, 5)), 11)])
        self.assertEqual(solution_part1(input), 11)

    def test_sample_input(self):
        part1_sample_input = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ]
        self.assertEqual(solution_part1(part1_sample_input, debug=True), 4361)

    def test_nothing_in_line(self):
        self.assertEqual(find_all_symbols([]), [])

    def test_all_periods_in_line(self):
        self.assertEqual(find_all_symbols(["........."]), [])
        self.assertEqual(find_all_numbers(["........."]), [])

    def test_all_periods_one_number(self):
        self.assertEqual(solution_part1(["......1....."]), 0)

    def test_sample_input_part2(self):
        part1_sample_input = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ]
        self.assertEqual(solution_part2(part1_sample_input, debug=True),
                         467835)


if __name__ == "__main__":
    unittest.main()
