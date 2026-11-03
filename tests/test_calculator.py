import unittest

from calc import calculate


class TestCalculator(unittest.TestCase):

    def test_addition_positive_numbers(self):
        self.assertEqual(calculate(9, 3, "+"), 12)

    def test_addition_negative_numbers(self):
        self.assertEqual(calculate(6, -3, "+"), 3)

    def test_addition_positive_and_negative(self):
        self.assertEqual(calculate(-2, -6, "+"), -8)

    def test_addition_with_zero(self):
        self.assertEqual(calculate(-4, -7, "+"), -11)

if __name__ == "__main__":
    unittest.main()
