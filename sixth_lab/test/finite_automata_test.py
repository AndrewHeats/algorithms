import unittest

from sixth_lab.src.finite_automata import finite_automata_search


class MyTestCase(unittest.TestCase):
    def test_1(self):
        needle = "AB"
        haystack = "AAAAAB"

        self.assertEqual([4], finite_automata_search(needle, haystack))

    def test_2(self):
        needle = " "
        haystack = "AAAAAB"

        self.assertEqual([], finite_automata_search(needle, haystack))

    def test_3(self):
        needle = "AAA"
        haystack = "AB"

        self.assertEqual([], finite_automata_search(needle, haystack))

    def test_3(self):
        needle = "ADAD"
        haystack = "ADADADADADAD"

        self.assertEqual([0, 2, 4, 6, 8], finite_automata_search(needle, haystack))


if __name__ == '__main__':
    unittest.main()
