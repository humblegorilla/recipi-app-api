"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test adding numbers together."""
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)
        
    def test_subtract_numbers(self):
        res = calc.subtract(6, 5)
        self.assertEqual(res, 1)
        
    def test_multiply_numbers(self):
        res = calc.multiply(3, 4)
        self.assertEqual(res, 12)
        
    def test_divide_numbers(self):
        res = calc.divide(4, 2)
        self.assertEqual(res, 2)
        
    def test_divide_by_zero(self):
        res = calc.divide(4, 0)
        self.assertEqual(res, 0)
