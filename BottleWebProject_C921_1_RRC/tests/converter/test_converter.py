import unittest

from BottleWebProject_C921_1_RRC.modules.formatConverter import data_to_matrix, matrix_to_data


class TestFileConverter(unittest.TestCase):
    def test_no_errors(self):
        matrix_correct = [[0, 1, 1, 1, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0],
                          [1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1],
                          [0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0]]
        json = matrix_to_data(matrix_correct)
        self.assertIsNotNone(json)

    def test_converting_both_ways(self):
        data = {'Nodes': [{'x': -53, 'y': -98, 'id': '0', 'connections': ['2', '1', '3', '4']},
                          {'x': 80, 'y': -30, 'id': '1', 'connections': ['0', '2', '3', '4', '7']},
                          {'x': -82, 'y': 22, 'id': '2', 'connections': ['0', '4', '1', '3', '5']},
                          {'x': -3, 'y': -110, 'id': '3', 'connections': ['0', '4', '1', '2']},
                          {'x': 49, 'y': 31, 'id': '4', 'connections': ['0', '3', '2', '1', '6']},
                          {'x': -69, 'y': 179, 'id': '5', 'connections': ['2', '6', '7']},
                          {'x': 65, 'y': 201, 'id': '6', 'connections': ['4', '5']},
                          {'x': 43, 'y': 111, 'id': '7', 'connections': ['1', '5']}]}
        matrix_correct = [[0, 1, 1, 1, 1, 0, 0, 0], [1, 0, 1, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1, 0, 0],
                          [1, 1, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1, 1],
                          [0, 0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0]]
        matrix = data_to_matrix(data)

        for idx, x in enumerate(matrix_correct):
            for idj, j in enumerate(x):
                val = matrix[idx][idj]
                self.assertEqual(j, val)


if __name__ == '__main__':
    unittest.main()
