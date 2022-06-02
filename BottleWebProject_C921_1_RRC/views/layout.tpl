<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Bottle Application</title>
    <link rel="stylesheet" type="text/css" href="../static/css/bootstrap.min.css"/>
    <link rel="stylesheet" type="text/css" href="../static/css/site.css"/>
    <script src="../static/scripts/generated/modernizr-2.6.2.js"></script>
</head>

<body>
<div class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a href="/" class="navbar-brand">Остовные деревья</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/home">Главная</a></li>
                <li><a href="/bfs">Алгоритм BFS</a></li>
                <li><a href="/dfs">Алгоритм DFS</a></li>
                <li><a href="/kruskal">Алгоритм Краскала</a></li>
                <li><a href="/contact">Разработчики</a></li>
            </ul>
        </div>
    </div>
</div>

<div class="container body-content">
    {{!base}}
    <hr/>
    <footer>
        <p>&copy; {{ year }} - Spanning tree by <a href="/contact">team #1</a></p>
    </footer>
</div>

<script src="../static/scripts/generated/jquery-1.10.2.js"></script>
<script src="../static/scripts/generated/bootstrap.js"></script>
<script src="../static/scripts/generated/respond.js"></script>

</body>
</html>
