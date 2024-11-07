import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    #add
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    #subtract
    def test_subtract_positive_result(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # multiply
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)

    #divide
    def test_divide_evenly_divisible(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_not_evenly_divisible(self):
        self.assertEqual(self.calc.divide(7, 3), 2)  # Expect integer division


    # Test case for divide by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # Test cases for modulo()
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_when_divisible(self):
        self.assertEqual(self.calc.modulo(6, 3), 0)

    # Test case for modulo by zero
    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)

if __name__ == '__main__':
    unittest.main()