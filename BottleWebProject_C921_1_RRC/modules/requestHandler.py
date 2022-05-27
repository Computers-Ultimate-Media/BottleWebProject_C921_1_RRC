from BottleWebProject_C921_1_RRC.database import insert, select_one
from BottleWebProject_C921_1_RRC.modules.bfs import bfs
from BottleWebProject_C921_1_RRC.modules.fileConverter import json_to_matrix, matrix_to_json


def handle_request(data: dict) -> dict:
    alg_type = int(data.get("AlgType"))
    graph_in = str(data["Graph"])

    matrix_in: list[list[int]] = json_to_matrix(graph_in)
    matrix_out: list[list[int]] = list[list[int]]()

    if alg_type == 1:
        start = int(data["StartNode"])
        matrix_out = bfs(matrix_in, start)
        pass
    elif alg_type == 2:
        pass
    elif alg_type == 3:
        pass
    else:
        raise Exception("Unknown type of algorith")

    graph_out = matrix_to_json(matrix_out)

    save_to_database(alg_type, graph_in, graph_out)

    result = dict()
    result["Graph"] = graph_out
    return result


def save_to_database(alg_type: int, input: str, output: str) -> int:
    sql = "insert into bottle_db.requests (alg_type, input, output) values (%s, %s, %s);"
    val = (alg_type, input, output)
    insert(sql, val)

    sql = "select last_insert_id()"
    res = select_one(sql)
    return res[0]
