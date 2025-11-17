import unittest
from .utils import  add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10, -5), 15)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-2, -4), 8)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-8, 4), -2.0)

    def test_divide_by_zero(self):
        # This test ensures that the correct exception is raised
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()