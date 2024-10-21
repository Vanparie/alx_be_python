import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, -7), 7)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-4, -4), 1)

        # Test dividing by zero
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_edge_cases(self):
        """Additional tests for edge cases in division."""
        # Test with very small numbers
        self.assertAlmostEqual(self.calc.divide(1, 3), 1 / 3)
        self.assertAlmostEqual(self.calc.divide(1, -3), -1 / 3)


if __name__ == "__main__":
    unittest.main()
