import unittest

from second_lab.hamsters import hamsters


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        S = 7
        C = 3
        hamsters_list = [[1, 2], [2, 2], [3, 1]]

        self.assertEqual(hamsters(S, C, hamsters_list), 2)  # add assertion here
    def test_case2(self):
        S = 19
        C = 4
        hamsters_list = [[5, 0], [2, 2], [1, 4], [5, 1]]

        self.assertEqual(hamsters(S, C, hamsters_list), 3)  # add assertion here
    def test_case3(self):
        S = 2
        C = 2
        hamsters_list = [[1, 50000], [1, 60000]]

        self.assertEqual(hamsters(S, C, hamsters_list), 1)  # add assertion here

if __name__ == '__main__':
    unittest.main()
