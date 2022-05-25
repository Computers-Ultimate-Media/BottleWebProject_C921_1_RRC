import json
import numpy as np


def json_to_matrix(data: str) -> list[list]:
    nodes: list = json.loads(data)
    sorted(nodes, key=lambda x: x['id'])
    node_num: int = len(nodes)
    matrix = np.zeros(node_num * node_num, dtype=np.int32).reshape(node_num, node_num)
    for node in nodes:
        id = int(node['id'])
        connections: list = node['connections']
        for connection in connections:
            target: int = int(connection)
            matrix[id][target] = 1

    matrix.toList()
    return matrix

def matrix_to_json(matrix : list[list]) -> str :
    data = list()
    for idx, node in enumerate(matrix):
        conns = list()

        for idx, value in enumerate(node):
            if(value>0):
                conns.append(idx)

        data.append(dict(
            id=idx,
            connections = conns
        ) )

    return json.dumps(data)
