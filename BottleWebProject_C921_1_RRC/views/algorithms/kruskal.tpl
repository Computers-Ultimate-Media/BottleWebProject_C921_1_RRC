% rebase('layout.tpl', title=title, year=year)

<title> {{ title }}}</title>
<link rel="stylesheet" type="text/css" href="../../static/css/nodes.css"/>
<script type="text/javascript" src="../../static/scripts/vis-network.min.js"></script>
<script type="text/javascript" src="../../static/scripts/nodes.js"></script>

<body onload="init();">

<div id="node-popUp">
    <span id="node-operation">node</span> <br/>
    <table style="margin: auto">
        <tr>
            <td>id</td>
            <td><input id="node-id" value="" readonly/></td>
        </tr>
    </table>
    <input type="button" value="Сохранить" id="node-saveButton"/>
    <input type="button" value="Отменить" id="node-cancelButton"/>
</div>
<div id="edge-popUp">
    <span id="edge-operation">edge</span> <br/>
    <table style="margin: auto">
        <tr>
            <td>label</td>
            <td><input id="edge-label" value="new value"/></td>
        </tr>
    </table>
    <input type="button" value="Сохранит" id="edge-saveButton"/>
    <input type="button" value="Отменить" id="edge-cancelButton"/>
</div>
<br/>
<div id="mynetwork" data-alg-type="3"></div>

<input class="btn-norma" type="button" id="export_button" onclick="return exportNetwork()" value="Выполнить!"/>
</body>