from unittest import TestCase
from functions import divide, multiply

class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        # self.assertEqual(divide(dividend, divisor), expected_result)
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta= 0.0001)
    
    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertEqual(divide(dividend, divisor), expected_result)
    
    def test_divide_zero(self):
        dividend = 0
        divisor = 3
        expected_result= 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)
        
        #self.assertRaises(ValueError, lambda : divide(25, 0))
    
    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()
    
    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)
    
    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(0),expected)
    
    def test_multipy_multiple_values(self):
        inputs =(3,5)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)
    
    def test_multiply_result_with_zero(self):
        inputs = (3,5,0)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_negative(self):
        inputs =(3,-5,2)
        expected = -30
        self.assertEqual(multiply(*inputs),expected)
    
    def test_multiply_floats(self):
        inputs = (2.0,3.2)
        expected = 6.4
        self.assertAlmostEqual(multiply(*inputs),expected, delta =0.000000000000001)
    