from bottle import route, view, redirect, request, post
from datetime import datetime
from modules import bfs, dfs, kruskal


@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )


@route('/contact')
@view('contact')
def contact():
    return dict(
        title='Команда #1',
        year=datetime.now().year
    )


@route('/calculate', method='post')
def calculate_request():
    from json import dumps as json_dumps, loads as json_loads
    from BottleWebProject_C921_1_RRC.modules.requestHandler import handle_request

    try:
        decoded_request = request.body.getvalue().decode('utf-8')
        data: dict = json_loads(decoded_request)

        response: dict = handle_request(data)

        response["Status"] = 200
        return json_dumps(response)
    finally:
        return json_dumps({"Status": 400})


@post('/bfs', method='post')
@post('/dfs', method='post')
@post('/kruskal', method='post')
def result_page():
    return redirect('/result')


@route('/bfs')
@view('algorithms/bfs')
def bfs_page():
    return dict(
        title='bfs',
        year=datetime.now().year
    )


@route('/dfs')
@view('algorithms/dfs')
def dfs_page():
    return dict(
        title='dfs',
        year=datetime.now().year
    )


@route('/kruskal')
@view('algorithms/kruskal')
def kruskal_page():
    return dict(
        title='kruskal',
        year=datetime.now().year
    )
