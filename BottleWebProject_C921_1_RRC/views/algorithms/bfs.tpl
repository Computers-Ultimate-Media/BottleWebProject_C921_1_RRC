% rebase('layout.tpl', title=title, year=year)

<title> {{ title }}}</title>
<style>
    body,
    select {
        font: 10pt sans;
    }

    #mynetwork {
        position: relative;
        width: auto;
        height: 600px;
        border: 1px solid lightgray;
    }

    table.legend_table {
        font-size: 11px;
        border-width: 1px;
        border-color: #d3d3d3;
        border-style: solid;
    }

    table.legend_table,
    td {
        border-width: 1px;
        border-color: #d3d3d3;
        border-style: solid;
        padding: 2px;
    }

    div.table_content {
        width: 80px;
        text-align: center;
    }

    div.table_description {
        width: 100px;
    }

    #operation {
        font-size: 28px;
    }

    #node-popUp {
        display: none;
        position: absolute;
        top: 350px;
        left: 170px;
        z-index: 299;
        width: 250px;
        height: 120px;
        background-color: #f9f9f9;
        border-style: solid;
        border-width: 3px;
        border-color: #5394ed;
        padding: 10px;
        text-align: center;
    }

    #edge-popUp {
        display: none;
        position: absolute;
        top: 350px;
        left: 170px;
        z-index: 299;
        width: 250px;
        height: 90px;
        background-color: #f9f9f9;
        border-style: solid;
        border-width: 3px;
        border-color: #5394ed;
        padding: 10px;
        text-align: center;
    }

</style>
<script type="text/javascript" src="../../static/scripts/vis-network.min.js"></script>
<script type="text/javascript" src="../../static/scripts/nodes.js"></script>

<body onload="init();">

<label style="font-size: 20px" for="first_node">Выберите начальный узел</label>
<select id="first_node" style="margin: 50px" onchange="choose_node();"></select>


<div id="node-popUp">
    <span id="node-operation">node</span> <br/>
    <table style="margin: auto">
        <tr>
            <td>id</td>
            <td><input id="node-id" value="" readonly/></td>
        </tr>
    </table>
    <input type="button" value="save" id="node-saveButton"/>
    <input type="button" value="cancel" id="node-cancelButton"/>
</div>
<div id="edge-popUp">
    <span id="edge-operation">edge</span> <br/>
    <table style="margin: auto">
        <tr>
            <td>label</td>
            <td><input id="edge-label" value="new value"/></td>
        </tr>
    </table>
    <input type="button" value="save" id="edge-saveButton"/>
    <input type="button" value="cancel" id="edge-cancelButton"/>
</div>
<br/>
<div id="mynetwork"></div>

<input type="button" id="export_button" onclick="return exportNetwork()" value="Выполнить!" />
</body>