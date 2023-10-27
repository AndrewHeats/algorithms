import unittest

from fourth_lab.ostrivtsi import get_count_of_islands


class MyTestCase(unittest.TestCase):
    def test_something(self):
        matrix = [[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                  [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
                  [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                  [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
                  [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                  [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]
        self.assertEqual(5, get_count_of_islands(matrix))  # add assertion here

    def test_something2(self):
        matrix = []
        self.assertEqual(0, get_count_of_islands(matrix))  # add assertion here

    def test_something3(self):
        matrix = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
        self.assertEqual(1, get_count_of_islands(matrix))  # add assertion here


if __name__ == '__main__':
    unittest.main()
