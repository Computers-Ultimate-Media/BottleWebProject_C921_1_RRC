from copy import deepcopy


# алгоритм прохода по графу по глубине
def dfs(matrix_in: list[list[int]], start: int) -> list[list[int]]:
    matrix_out = deepcopy(matrix_in)
    for i in range(len(matrix_out)):
        for j in range(len(matrix_in[0])):
            matrix_out[i][j] = 0

    to_visit = [start]
    visited: set[int] = set[int]()

    stack: list = list()

    to_visit.append(start)
    while not len(to_visit) == 0:
        node = to_visit.pop()

        if node not in visited and node != start:
            connected_node = stack.pop()
            visited.add(node)
            matrix_out[node][connected_node] = 1
            matrix_out[connected_node][node] = 1

        for connid, conn in enumerate(matrix_in[node]):
            if connid not in visited and conn > 0:
                to_visit.append(connid)
                stack.append(node)

    return matrix_out

# matrix = [[0, 1, 1, 1, 1, 0, 0, 0],
#           [1, 0, 1, 0, 1, 0, 0, 1],
#           [1, 1, 0, 0, 1, 1, 0, 0],
#           [1, 0, 0, 0, 0, 0, 0, 0],
#           [1, 1, 1, 0, 0, 0, 1, 0],
#           [0, 0, 1, 0, 0, 0, 1, 1],
#           [0, 0, 0, 0, 1, 1, 0, 0],
#           [0, 1, 0, 0, 0, 1, 0, 0]]
# res = dfs(matrix, 1)
# data = matrix_to_data(res)
# data2 = matrix_to_data(matrix)
# print(data)
# print(data2)
# print(res)
