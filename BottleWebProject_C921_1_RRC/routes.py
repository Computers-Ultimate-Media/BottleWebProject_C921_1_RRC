from datetime import datetime

from bottle import route, view, request, HTTPResponse

from BottleWebProject_C921_1_RRC.database import select_one


# обработчик главной страницы сайта
@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )


# обработчик страницы о разработчиках
@route('/contact')
@view('contact')
def contact():
    return dict(
        title='Команда разработчиков',
        year=datetime.now().year
    )


# обработчик post запроса для обработки графа
# возвращает либо статус 200 Ok и id результата
# либо статус 400 с ошибкой
@route('/calculate', method='post')
def calculate_request():
    from json import dumps as json_dumps, loads as json_loads
    from BottleWebProject_C921_1_RRC.modules.requestHandler import handle_request

    try:

        decoded_request = request.body.getvalue().decode('utf-8')
        data: dict = json_loads(decoded_request)

        response: dict = dict()
        response["RequestId"] = handle_request(data)

        return HTTPResponse(body=json_dumps(response), status=200)
    except Exception as error:
        print(error)
        return HTTPResponse(status=400)


# обработчик get запроса для результирующей страницы
# принимает в качестве аргумента id записи
# возвращает данные в соответствии с id
@route('/result')
@view('result')
def result_page():
    db_id = request.query.id
    sql = select_one(
        f"select input, output, alg_type, alg_name_ru from bottle_db.requests r inner join bottle_db.alg_type a on a.id = r.alg_type  where r.id={db_id}")

    return dict(
        title='Результат алгоритма',
        year=datetime.now().year,
        input=sql[0],
        result=sql[1],
        algType=sql[2],
        algName=sql[3]
    )


# страница для графа BFS
@route('/bfs')
@view('algorithms/bfs')
def bfs_page():
    return dict(
        title='Алгоритм BFS',
        year=datetime.now().year
    )


# страница для графа DFS
@route('/dfs')
@view('algorithms/dfs')
def dfs_page():
    return dict(
        title='Алгоритм DFS',
        year=datetime.now().year
    )


# страница для графа Kruskal
@route('/kruskal')
@view('algorithms/kruskal')
def kruskal_page():
    return dict(
        title='Алгоритм Краскала',
        year=datetime.now().year
    )
