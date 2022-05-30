import json
import unittest

from BottleWebProject_C921_1_RRC.modules.formatConverter import data_to_matrix
from BottleWebProject_C921_1_RRC.modules.algorithms.bfs import bfs


class TestBFS(unittest.TestCase):
    def test_no_error(self):
        with open("C:\\Users\\max\\PycharmProjects\\BottleWebProject_C921_1_RRC\\BottleWebProject_C921_1_RRC\\tests\\bfs\\graph_bfs_default.json") as f:
            text = f.read()
            matrix = data_to_matrix(json.loads(text))
        res = bfs(matrix, 0)
        self.assertIsNotNone(res)

    def test_find_spanning_tree(self):
        with open("C:\\Users\\max\\PycharmProjects\\BottleWebProject_C921_1_RRC\\BottleWebProject_C921_1_RRC\\tests\\bfs\\graph_bfs_default.json") as f:
            matrix = data_to_matrix(f.read())
            res = bfs(matrix, 2)
        with open("C:\\Users\\max\\PycharmProjects\\BottleWebProject_C921_1_RRC\\BottleWebProject_C921_1_RRC\\tests\\bfs\\graph_bfs_result.json") as f:
            matrix_correct = data_to_matrix(f.read())

        for idx, x in enumerate(matrix_correct):
            for idj, j in enumerate(x):
                val = res[idx][idj]
                self.assertEqual(j, val)


if __name__ == '__main__':
    unittest.main()
