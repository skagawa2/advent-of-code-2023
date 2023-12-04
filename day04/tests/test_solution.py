import unittest
from src.sol import solution_part1, parse_input_single_line, \
    get_winning_numbers, solution_part2


class TestDay04(unittest.TestCase):

    def test_parse_input_single_line(self):
        input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        answer = (["41", "48", "83", "86", "17"],
                  ["83", "86", "6", "31", "17", "9", "48", "53"])
        self.assertEqual(parse_input_single_line(input), answer)

    def test_winning_numbers(self):
        winning_numbers = set(["41", "43", "53"])
        your_numbers = set(["41", "43"])
        self.assertEqual(get_winning_numbers(winning_numbers, your_numbers),
                         set(["41", "43"]))

    def test_sample_input(self):
        sample_input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        sample_answer = 13
        self.assertEqual(solution_part1(sample_input), sample_answer)

    def test_sample_input_part2(self):
        sample_input = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        sample_answer = 30
        self.assertEqual(solution_part2(sample_input), sample_answer)


if __name__ == "__main__":
    unittest.main()
