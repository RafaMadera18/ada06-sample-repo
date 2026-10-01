import unittest
from src.calculator import calculate_subtotal, apply_tax


class TestCalculator(unittest.TestCase):
    def test_calculate_subtotal_valid(self):
        self.assertEqual(calculate_subtotal([10.5, 20.0, 5.25]), 35.75)
        self.assertEqual(calculate_subtotal([]), 0.0)

    def test_calculate_subtotal_negative(self):
        with self.assertRaises(ValueError):
            calculate_subtotal([10.0, -5.0])

    def test_apply_tax_valid(self):
        self.assertEqual(apply_tax(100.0, 0.16), 116.0)

    def test_apply_tax_negative_amount(self):
        with self.assertRaises(ValueError):
            apply_tax(-100.0, 0.16)

    def test_apply_tax_negative_rate(self):
        with self.assertRaises(ValueError):
            apply_tax(100.0, -0.16)


if __name__ == "__main__":
    unittest.main()
