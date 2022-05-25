from bottle import route, view
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


@route('/bfs')
@view('algorithms/bfs')
def bfs():
    return dict(
        title='bfs',
        year=datetime.now().year
    )


@route('/dfs')
@view('algorithms/dfs')
def dfs():
    return dict(
        title='dfs',
        year=datetime.now().year
    )


@route('/kruskal')
@view('algorithms/kruskal')
def kruskal():
    return dict(
        title='kruskal',
        year=datetime.now().year
    )
