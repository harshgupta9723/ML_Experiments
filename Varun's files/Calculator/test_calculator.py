from logging import error
import unittest
from calculator import CalcFunctions

calF = CalcFunctions()

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertAlmostEqual(calF.add(2,4), 6)
        self.assertAlmostEqual(calF.add(2.8,-7), -4.2)
        self.assertAlmostEqual(calF.add(0, 0), 0)
        self.assertRaises(TypeError, lambda : calF.add(12, None))
        self.assertRaises(TypeError, lambda : calF.add(2,'4a'))
        self.assertRaises(TypeError, lambda : calF.add('@','*'))

    def test_diff(self):
        self.assertAlmostEqual(calF.diff(2,4), -2)
        self.assertAlmostEqual(calF.diff(2.8,-7), 9.8)
        self.assertAlmostEqual(calF.diff(0, 0), 0)
        self.assertRaises(TypeError, lambda : calF.diff(12, None))
        self.assertRaises(TypeError, lambda : calF.diff(2,'4a'))
        self.assertRaises(TypeError, lambda : calF.diff('@','*'))

    def test_multiply(self):
        self.assertAlmostEqual(calF.multiply(2,4), 8)
        self.assertAlmostEqual(calF.multiply(2.8,-7), -19.6)
        self.assertAlmostEqual(calF.multiply(0, 0), 0)
        self.assertRaises(TypeError, lambda : calF.multiply(12, None))
        self.assertRaises(TypeError, lambda : calF.multiply(2,'4a'))
        self.assertRaises(TypeError, lambda : calF.multiply('@','*'))

    def test_div(self):
        self.assertAlmostEqual(calF.div(2,4), 0.5)
        self.assertAlmostEqual(calF.div(7,2.8), 2.5)
        self.assertAlmostEqual(calF.div(0, 23), 0)
        self.assertRaises(TypeError, lambda : calF.div(12, None))
        self.assertRaises(TypeError, lambda : calF.div(2,'4a'))
        self.assertRaises(TypeError, lambda : calF.div('@','*'))
        self.assertRaises(TypeError, lambda : calF.div(12, 0)  )
        self.assertRaises(TypeError, lambda : calF.div(-14, -7))
        self.assertRaises(TypeError, lambda : calF.div(-2, 8))

if __name__ == '__main__':
    unittest.main()        

