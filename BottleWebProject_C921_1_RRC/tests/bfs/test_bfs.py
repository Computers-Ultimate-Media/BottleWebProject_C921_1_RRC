import unittest

from BottleWebProject_C921_1_RRC.modules.algorithms.bfs import bfs


class TestBFS(unittest.TestCase):
    def test_no_error(self):
        matrix = [[0, 1, 1, 1, 1, 0, 0, 0],
                  [1, 0, 1, 1, 1, 0, 0, 1],
                  [1, 1, 0, 1, 1, 1, 0, 0],
                  [1, 1, 1, 0, 1, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 1, 1, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0]]
        res = bfs(matrix, 0)
        self.assertIsNotNone(res)

    def test_find_spanning_tree(self):
        matrix = [[0, 1, 1, 1, 1, 0, 0, 0],
                  [1, 0, 1, 1, 1, 0, 0, 1],
                  [1, 1, 0, 1, 1, 1, 0, 0],
                  [1, 1, 1, 0, 1, 0, 0, 0],
                  [1, 1, 1, 1, 0, 0, 1, 0],
                  [0, 0, 1, 0, 0, 0, 1, 1],
                  [0, 0, 0, 0, 1, 1, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0, 0]]

        res = bfs(matrix, 0)

        matrix_correct = [[0, 1, 1, 1, 1, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 1],
                          [1, 0, 0, 0, 0, 1, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 1, 0],
                          [0, 0, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0]]

        for idx, x in enumerate(matrix_correct):
            for idj, j in enumerate(x):
                val = res[idx][idj]
                self.assertEqual(j, val)


if __name__ == '__main__':
    unittest.main()
