import unittest
from src.sol import solution_part1, solution_part1_singleline, \
    solution_part2, solution_part2_singleline


class TestDay01(unittest.TestCase):

    part1_lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "trb7uchet"]

    part2_lines = ["two1nine", "eightwothree", "abcone2threexyz",
                   "xtwone3four", "4nineeightseven2", "zoneight234",
                   "7pqrstsixteen"]

    def test_part1_sample_inputs(self):
        self.assertEqual(solution_part1_singleline(self.part1_lines[0]), 12)
        self.assertEqual(solution_part1_singleline(self.part1_lines[1]), 38)
        self.assertEqual(solution_part1_singleline(self.part1_lines[2]), 15)
        self.assertEqual(solution_part1_singleline(self.part1_lines[3]), 77)

    def test_part1_integration(self):
        self.assertEqual(solution_part1(self.part1_lines), 142)

    def test_part2_sample_inputs(self):
        self.assertEqual(solution_part2_singleline(self.part2_lines[0]), 29)
        self.assertEqual(solution_part2_singleline(self.part2_lines[1]), 83)
        self.assertEqual(solution_part2_singleline(self.part2_lines[2]), 13)
        self.assertEqual(solution_part2_singleline(self.part2_lines[3]), 24)
        self.assertEqual(solution_part2_singleline(self.part2_lines[4]), 42)
        self.assertEqual(solution_part2_singleline(self.part2_lines[5]), 14)
        self.assertEqual(solution_part2_singleline(self.part2_lines[6]), 76)

    def test_part2_integration(self):
        self.assertEqual(solution_part2(self.part2_lines), 281)

    def test_other_digits(self):
        self.assertEqual(solution_part2_singleline("five"), 55)

    def test_combinednumbers(self):
        self.assertEqual(solution_part2_singleline("fiveight"), 58)
        self.assertEqual(solution_part2_singleline("oneight"), 18)
        self.assertEqual(solution_part2_singleline("eightwo"), 82)

    def test_singlelines_from_input(self):
        self.assertEqual(solution_part2_singleline("62sixone3"), 63)
        self.assertEqual(solution_part2_singleline("onethreevgrhtnpdlvnjklqjqj1"), 11)  # noqa
        self.assertEqual(solution_part2_singleline("hflhcmjjkmqn6six"), 66)


if __name__ == "__main__":
    unittest.main()
