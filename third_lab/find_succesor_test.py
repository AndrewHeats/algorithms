import unittest

from third_lab.find_succesor import BinaryTree, find_successor

root = BinaryTree(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(20)
root.insert(12)


class MyTestCase(unittest.TestCase):
    def test_case1(self):
        succesor = find_successor(root, BinaryTree(7))
        self.assertEqual(succesor.value, 10)  # add assertion here

    def test_case2(self):
        succesor = find_successor(root, BinaryTree(20))
        self.assertEqual(succesor, None)  # add assertion here

    def test_case3(self):
        succesor = find_successor(root, BinaryTree(5))
        self.assertEqual(succesor.value, 7)  # add assertion here

    def test_case4(self):
        succesor = find_successor(root, BinaryTree(500))
        self.assertEqual(succesor, None)  # add assertion here

    def test_case5(self):
        succesor = find_successor(None, BinaryTree(500))
        self.assertEqual(succesor, None)  # add assertion here

    def test_case6(self):
        succesor = find_successor(None, None)
        self.assertEqual(succesor, None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
