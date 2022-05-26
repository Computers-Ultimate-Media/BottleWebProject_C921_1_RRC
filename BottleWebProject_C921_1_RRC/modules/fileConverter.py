import json
import numpy as np


# Конвертер графа из json формата библиотеки vis.js в матрицу смежности
def json_to_matrix(data: str) -> list[list[int]]:
    nodes: list = json.loads(data)
    sorted(nodes, key=lambda x: x['id'])
    node_num: int = len(nodes)
    matrix: np.ndarray = np.zeros(node_num * node_num, dtype=np.int32).reshape(node_num, node_num)
    for node in nodes:
        id = int(node['id'])
        connections: list = node['connections']
        for connection in connections:
            target: int = int(connection)
            matrix[id][target] = 1

    matrix.tolist()
    # noinspection PyTypeChecker
    return matrix


# Конвертер графа из матрицы смежности в json формат библиотеки vis.js
def matrix_to_json(matrix: list[list[int]]) -> str:
    data = list()
    for idnode, node in enumerate(matrix):
        conns = list()

        for idval, value in enumerate(node):
            if value > 0:
                conns.append(idval)

        data.append(dict(
            id=str(idnode),
            connections=conns
        ))

    return json.dumps(data, indent=2)
