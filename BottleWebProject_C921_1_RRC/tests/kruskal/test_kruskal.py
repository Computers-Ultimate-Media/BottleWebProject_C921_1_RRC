import unittest

from BottleWebProject_C921_1_RRC.modules.algorithms.kruskal import kruskal

class TestKruskal(unittest.TestCase):
    def test_no_error(self):
        conns = [{'fromId': 0, 'toId': 1, 'weight': '1'}, {'fromId': 3, 'toId': 1, 'weight': '5'},
         {'fromId': 3, 'toId': 0, 'weight': '4'}, {'fromId': 2, 'toId': 0, 'weight': '6'}]
        res = kruskal(conns)
        correct = [{'weight': '1', 'fromId': 0, 'toId': 1}, {'weight': '4', 'fromId': 3, 'toId': 0}, {'weight': '6', 'fromId': 2, 'toId': 0}]
        self.assertEqual(res, correct)

if __name__ == '__main__':
    unittest.main()