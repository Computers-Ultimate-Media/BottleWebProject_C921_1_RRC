import json
import numpy as np


# Конвертер графа из json формата библиотеки vis.js в матрицу смежности
def json_to_matrix(graph: dict) -> list[list[int]]:
    nodes = json.loads(graph["Nodes"])
    has_edges = "Edges" in graph.keys()
    if has_edges:
        edges = json.loads(graph["Edges"])

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
            to_id: int = int(edge["toId"])
            from_id: int = int(edge["fromId"])
            weight: int = int(edge["weight"])
            matrix[to_id][from_id] = weight
            matrix[from_id][to_id] = weight

    matrix.tolist()
    # noinspection PyTypeChecker
    return matrix


# Конвертер графа из матрицы смежности в json формат библиотеки vis.js
def matrix_to_json(matrix: list[list[int]]) -> str:
    nodes = list()
    for idnode, node in enumerate(matrix):
        conns = list()

        for idval, value in enumerate(node):
            if value > 0:
                conns.append(value)

        nodes.append(dict(
            id=str(idnode),
            connections=conns
        ))
    return json.dumps(nodes, indent=2)
