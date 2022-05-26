import unittest

from BottleWebProject_C921_1_RRC.modules.fileConverter import json_to_matrix, matrix_to_json


class TestFileConverter(unittest.TestCase):
    def test_converting_both_ways(self):
        with open("json.txt") as f:
            json_in = f.read()

        matrix = json_to_matrix(json_in)
        for idx, line in enumerate(matrix):
            print(line)

        json_out = matrix_to_json(matrix)

        self.assertEqual(json_out, json_in)


if __name__ == '__main__':
    unittest.main()
