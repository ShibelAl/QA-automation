import unittest
from math_function import modulo_func
from math_function import is_even
from math_function import is_odd
from math_function import sum_function
from math_function import sub_function
from math_function import mul_function
from math_function import div_function

class TestMathFunction(unittest.TestCase):
    def test_is_even_true(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(1), "test failed!")
        self.assertFalse(is_even(3), "test failed")
        self.assertRaises(TypeError, is_even('a'))

    def test_sum_function_correct(self):
        self.assertEqual(1, sum_function(0, 1), "test failed!")
        self.assertEqual(-8, sum_function(-10, 2), "test failed!")

    def test_sum_function_wrong(self):
        self.assertNotEqual(0, sum_function(0, 1), "test failed!")
        self.assertNotEqual(8, sum_function(-10, 2), "test failed!")

    # def test_mul_function_correct(self):


    # def test_mul_function_correct(self):
