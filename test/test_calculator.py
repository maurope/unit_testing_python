import unittest
from src.calculator import sum, subtract

class CalculatorTest(unittest.TestCase):

    def test_sum(self):
        assert sum(2 , 3) == 6

    def test_substract(self):
        assert subtract(10, 5) == 5
