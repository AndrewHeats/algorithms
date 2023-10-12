import unittest

from zigzag_order import zigzag_order


class TestZigzagTraversal(unittest.TestCase):

    def test_case_1(self):
        array1 = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        self.assertEqual(zigzag_order(array1),
                         [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25])

    def test_case_2(self):
        array2 = [[1, 2, 3, 4],
                  [5, 6, 7, 8]]
        self.assertEqual(zigzag_order(array2), [1, 2, 5, 6, 3, 4, 7, 8])
        print(zigzag_order(array2))


    def test_case_3(self):
        self.assertEqual(zigzag_order([[1]]), [1])

    def test_case_4(self):
        self.assertEqual(zigzag_order([[1],
                                       [2],
                                       [3],
                                       [4],
                                       [5],
                                       [6]]), [1, 2, 3, 4, 5, 6])

    def test_case_5(self):
        self.assertEqual(zigzag_order([[1, 2, 3, 4, 5, 6]]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
