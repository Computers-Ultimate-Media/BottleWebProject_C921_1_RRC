import json

import numpy as np


# Конвертер графа из словаря формата библиотеки vis.js в матрицу смежности
def data_to_matrix(graph: dict) -> list[list[int]]:
    nodes = graph["Nodes"]
    has_edges = "Edges" in graph.keys()
    if has_edges:
        edges = graph["Edges"]

    sorted(nodes, key=lambda x: x['id'])
    node_num: int = len(nodes)
    matrix: np.ndarray = np.zeros(node_num * node_num, dtype=np.int32).reshape(node_num, node_num)

    if not has_edges:
        for node in nodes:
            id = int(node['id'])
            connections: list = node['connections']
            for connection in connections:
               target: int = int(connection)
               matrix[id][target] = 1
    else:
        for edge in edges:
            to_id: int = int(edge[1])
            from_id: int = int(edge[2])
            weight: int = int(edge[0])
            matrix[to_id][from_id] = weight
            matrix[from_id][to_id] = weight

    matrix = matrix.tolist()
    # noinspection PyTypeChecker
    return matrix


# Конвертер графа из матрицы смежности в словарь формата библиотеки vis.js
def matrix_to_data(matrix: list[list[int]]) -> str:
    nodes = list()
    for idnode, node in enumerate(matrix):
        conns = list()

        for idval, value in enumerate(node):
            if value > 0:
                conns.append(idval)

        nodes.append(dict(
            id=str(idnode),
            connections=conns
        ))
    return json.dumps(nodes, indent=2)