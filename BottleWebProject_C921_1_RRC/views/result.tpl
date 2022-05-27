% rebase('layout.tpl', title=title, year=year)

<title> {{ title }}</title>

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
</style>

<script type="text/javascript" src="../static/scripts/vis-network.min.js"></script>
<script type="text/javascript" src="../static/scripts/nodes.js"></script>

<body onload="importNetwork();">
    <div id="mynetwork" data-graph="{{graph}}"></div>
</body>