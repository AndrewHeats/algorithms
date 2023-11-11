import unittest
import os

from fifth_lab.GAMSRV import read_input_file, GAMSRV, write_output_file


class TestGAMSRV(unittest.TestCase):

    def test_example_1(self):
        input_file_path = 'example_1.in'
        output_file_path = 'example_1.out'

        with open(input_file_path, 'w') as file:
            file.write("6 6\n1 2 6\n1 3 10\n3 4 80\n4 5 50\n5 6 20\n2 3 40\n2 4 100\n")

        expected_output = "100"

        self.run_and_check(input_file_path, output_file_path, expected_output)

    def test_example_2(self):
        input_file_path = 'example_2.in'
        output_file_path = 'example_2.out'

        with open(input_file_path, 'w') as file:
            file.write("9 12\n2 4 6\n1 2 20\n2 3 20\n3 6 20\n6 9 20\n9 8 20\n8 7 20\n7 4 20\n4 1 20\n5 2 10\n5 4 10\n5 6 10\n5 8 10\n")

        expected_output = "10"

        self.run_and_check(input_file_path, output_file_path, expected_output)

    def test_example_3(self):
        input_file_path = 'example_3.in'
        output_file_path = 'example_3.out'

        with open(input_file_path, 'w') as file:
            file.write("3 2\n1 3\n1 2 50\n2 3 1000000000\n")

        expected_output = "1000000000"

        self.run_and_check(input_file_path, output_file_path, expected_output)

    def run_and_check(self, input_file_path, output_file_path, expected_output):
        graph, client_list = read_input_file(input_file_path)
        result = GAMSRV(graph, client_list)
        write_output_file(output_file_path, result)

        with open(output_file_path, 'r') as file:
            actual_output = file.read().strip()

        self.assertEqual(actual_output, expected_output)

        # Clean up generated files
        os.remove(input_file_path)
        os.remove(output_file_path)

if __name__ == '__main__':
    unittest.main()
