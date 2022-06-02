% rebase('layout.tpl', title=title, year=year)

<title> {{ title }}}</title>
<link rel="stylesheet" type="text/css" href="../../static/css/nodes.css"/>
<script type="text/javascript" src="../../static/scripts/vis-network.min.js"></script>
<script type="text/javascript" src="../../static/scripts/nodes.js"></script>

<body onload="init();">

<div class="text-dec t-l">{{ title }}.</div>
<div class="text-dec t-n">
    Данный раздел предназначен для вычисления графа алгоритмом Краскала. Вы можете построить неориентированный
    граф, используя инструементы "Добавить узел" и "Добавить ребро" с указанием ВЕСА между ними. После выполнить
    алгоритм, нажав на кнопку "Выполнить".
</div>
<div id="edge-popUp">
    <span id="edge-operation">edge</span> <br/>
    <table style="margin: auto">
        <tr>
            <td class="text-dec">Вес</td>
            <td><input type="number" min="1" oninput="validity.valid||(value='');" id="edge-label" value="1"/></td>
        </tr>
    </table>
    <input type="button" value="Сохранить" id="edge-saveButton"/>
    <input type="button" value="Отменить" id="edge-cancelButton"/>
</div>
<br/>
<div id="mynetwork" data-alg-type="3"></div>

<input class="btn-norma" type="button" id="export_button" onclick="return exportNetwork()" value="Выполнить!"/>
</body>