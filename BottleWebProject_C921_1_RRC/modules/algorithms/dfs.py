import collections

from BottleWebProject_C921_1_RRC.modules.formatConverter import matrix_to_data, data_to_matrix


def dfs(matrix_in: list[list[int]], start: int) -> list[list[int]]:
    matrix_out = matrix_in.copy()
    for i in range(len(matrix_out)):
        for j in range(len(matrix_in[0])):
            matrix_out[i][j] = 0

    to_visit = [start]
    visited: set[int] = set[int]()

    to_visit.append(start)
    while not len(to_visit) == 0:
        node = to_visit.popleft()
        visited.add(node)
        for connid, conn in enumerate(matrix_in[node]):
            if connid not in visited and conn > 0:
                to_visit.appendleft(connid)
                visited.add(connid)
                matrix_out[node][connid] = conn
                matrix_out[connid][node] = conn
    return matrix_out


# with open("json.txt") as f:
#     lol = json_to_matrix(f.read())
#     print( matrix_to_json(dfs(lol, 2)))

