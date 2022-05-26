import collections
from BottleWebProject_C921_1_RRC.modules.utils import print_matrix


def bfs(matrix_in: list[list[int]], start: int) -> list[list[int]]:
    matrix_out = matrix_in.copy()
    for i in range(len(matrix_out)):
        for j in range(len(matrix_in[0])):
            matrix_out[i][j] = 0

    to_visit: collections.deque = collections.deque()
    visited: set[int] = set[int]()

    to_visit.append(start)
    while not len(to_visit) == 0:
        print("vis :" + str(visited))
        print("to :" + str(to_visit))

        node = to_visit.popleft()
        visited.add(node)
        print(node)
        for connid, conn in enumerate(matrix_in[node]):
            if connid not in visited and conn > 0:
                to_visit.append(connid)
                visited.add(connid)
                matrix_out[node][connid] = conn
                matrix_out[connid][node] = conn
        print_matrix(matrix_out)
    return matrix_out
