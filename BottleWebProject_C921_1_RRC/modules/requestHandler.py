import json

from BottleWebProject_C921_1_RRC.database import insert, select_one
from BottleWebProject_C921_1_RRC.modules.algorithms.bfs import bfs
from BottleWebProject_C921_1_RRC.modules.algorithms.dfs import dfs
from BottleWebProject_C921_1_RRC.modules.algorithms.kruskal import kruskal
from BottleWebProject_C921_1_RRC.modules.formatConverter import data_to_matrix, matrix_to_data


# обработчик поступающих запросов на вычисление
# возвращает id записи в БД после сохранения в ней
def handle_request(data: dict) -> int:
    alg_type = data.get("AlgType")
    alg_type = int(alg_type)
    graph_in = data["Graph"]

    matrix_in: list[list[int]] = data_to_matrix(graph_in)
    matrix_out: list[list[int]] = list[list[int]]()
    start = -1

    if alg_type == 1:
        start = int(data["StartNode"])
        matrix_out = bfs(matrix_in, start)

    elif alg_type == 2:
        start = int(data["StartNode"])
        matrix_out = dfs(matrix_in, start)

    elif alg_type == 3:
        connections = data["Graph"]["Edges"]
        connections = kruskal(connections)
    else:
        raise Exception("Unknown type of algorith")

    graph_out = matrix_to_data(matrix_out)

    if not start == -1:
        graph_out = mark_start_node(graph_out, start)

    if alg_type == 3:
        graph_out = copy(graph_in)
        graph_out["Edges"] = connections
        graph_out = json.dumps(graph_out)

    request_id = save_to_database(alg_type, json.dumps(graph_in), json.dumps(graph_out))
    return request_id


# сохранение результата обработки в БД
# возвращает id записи в БД
def save_to_database(alg_type: int, input: str, output: str) -> int:
    sql = "insert into bottle_db.requests (alg_type, input, output) values (%s, %s, %s);"
    val = (alg_type, input, output)
    insert(sql, val)

    sql = "select last_insert_id()"
    res = select_one(sql)
    return res[0]


# изменение стиля начальной вершины графа
# помечает ее красным и возвращает измененный граф
def mark_start_node(json_graph: str, start: int) -> str:
    data: list[dict] = json.loads(json_graph)

    start_node_id = -1
    for idnode, node in enumerate(data):
        if int(node["id"]) == start:
            start_node_id = idnode
            break

    if start_node_id == -1:
        raise Exception("Start node not found")

    data[start_node_id]["color"] = {"background": "#fb7e81"}

    return json.dumps(data, indent=2)
