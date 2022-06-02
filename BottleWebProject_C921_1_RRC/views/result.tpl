% rebase('layout.tpl', title=title, year=year)

<title> {{ title }}</title>
<link rel="stylesheet" type="text/css" href="../static/css/nodes.css"/>

<script type="text/javascript" src="../static/scripts/vis-network.min.js"></script>
<script type="text/javascript" src="../static/scripts/nodes.js"></script>

<input class="btn-norma" type="button" id="import_button" onclick="return importNetwork(false)" value="Показать входной граф!"/>
<input class="btn-norma" type="button" id="export_button" onclick="return importNetwork(true)" value="Показать результат!"/>

<body onload="importNetwork(true);">
    <div id="mynetwork" data-result="{{result}}" data-input="{{input}}" data-alg-type="{{algType}}"></div>
</body>