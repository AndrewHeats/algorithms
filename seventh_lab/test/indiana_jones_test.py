import unittest

from seventh_lab.src.indiana_jones import indiana_jones


class MyTestCase(unittest.TestCase):
    def test_indiana_jones_case1(self):
        matrix = [['a', 'a', 'b'], ['a', 'a', 'a'], ['a', 'a', 'b']]
        result = indiana_jones(matrix, 3, 3)
        self.assertEqual(result, 6)

    def test_indiana_jones_case2(self):
        matrix = [['a', 'a'], ['a', 'a'], ['a', 'a'], ['a', 'a']]
        result = indiana_jones(matrix, 4, 2)
        self.assertEqual(result, 8)

    def test_indiana_jones_case3(self):
        matrix = [['a', 'b', 'c'], ['b', 'a', 'c'], ['m', 'v', 'c'], ['c', 'o', 'c']]
        result = indiana_jones(matrix, 4, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
