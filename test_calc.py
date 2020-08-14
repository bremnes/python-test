import unittest
import calc

class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(6, calc.add(2, 4))

    def test_sum2(self):
        self.assertEqual(89, calc.add(80,9))

# if __name__ == '__main__':
#     unittest.main()
