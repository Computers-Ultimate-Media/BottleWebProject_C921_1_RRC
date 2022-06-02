let nodes = null;
let edges = null;
let network = null;
let data = null;
let seed = 2;
let counter_nodes = 0;

function draw() {
    nodes = [];
    edges = [];
    let container = document.getElementById("mynetwork");
    let options = {
        layout: { randomSeed: seed },
        locale: "ru",
        manipulation: {
            addNode: function (data, callback) {
                // filling in the popup DOM elements
                editNode(data, callback);
            },
            addEdge: function (data, callback) {
                if (data.from === data.to) {
                    callback(null);
                    return;
                }
                document.getElementById("edge-operation").innerText = "Добавить связь";
                editEdgeWithoutDrag(data, callback);
            },
            editEdge: {
                editWithoutDrag: function (data, callback) {
                    document.getElementById("edge-operation").innerText = "Изменить связь";
                    editEdgeWithoutDrag(data, callback);
                },
            },
        },
    };
    network = new vis.Network(container, data, options);
}


function editNode(data, callback) {
    saveNodeData.call(this, data, callback);
}


function removeOptions() {
    const select = document.getElementById("first_node");
    let opt_len = select.options.length - 1;
    for (let i = opt_len; i >= 0; i--) {
        select.remove(i);
    }
}

function addNewNodeInList() {
    try {
        const select = document.getElementById("first_node");
        removeOptions();

        for (let index in nodes) {
            select.options[select.options.length] = new Option(nodes[index], index);
        }
    } catch (err) {

    }
}

function saveNodeData(data, callback) {
    nodes.push(counter_nodes + 1);
    counter_nodes += 1;
    addNewNodeInList();

    data.label = counter_nodes.toString();
    data.id = counter_nodes - 1;
    callback(data);
}

function editEdgeWithoutDrag(data, callback) {
    // filling in the popup DOM elements
    document.getElementById("edge-label").value = "1";
    document.getElementById("edge-saveButton").onclick = saveEdgeData.bind(
        this,
        data,
        callback
    );
    document.getElementById("edge-cancelButton").onclick =
        cancelEdgeEdit.bind(this, callback);
    document.getElementById("edge-popUp").style.display = "block";

    let l = document.getElementById("mynetwork");
    let algType = l.dataset.algType
    if (algType != 3) {
        saveEdgeData.call(this, data, callback)
    }
}

function clearEdgePopUp() {
    document.getElementById("edge-saveButton").onclick = null;
    document.getElementById("edge-cancelButton").onclick = null;
    document.getElementById("edge-popUp").style.display = "none";
}

function cancelEdgeEdit(callback) {
    clearEdgePopUp();
    callback(null);
}

function saveEdgeData(data, callback) {
    if (typeof data.to === "object") data.to = data.to.id;
    if (typeof data.from === "object") data.from = data.from.id;
    data.label = document.getElementById("edge-label").value;
    clearEdgePopUp();
    callback(data);
}

function addConnections(elem, index) {
    elem.connections = network.getConnectedNodes(index);
}

function getEdges(edges) {
    let ed = [];
    edges.forEach(function (elem, index, array) {
        ed.push({
            fromId: elem.fromId,
            toId: elem.toId,
            weight: elem.labelModule.lines[0].blocks[0].text
        });
    });
    return ed;
}

function exportNetwork() {
    let nodes = objectToArray(network.getPositions());
    nodes.forEach(addConnections);

    let l = document.getElementById("mynetwork");
    let algType = l.dataset.algType
    let calculate_request;

    if (algType == 1 || algType == 2) {
        let e = document.getElementById("first_node");
        let select_node = e.options[e.selectedIndex].value - 1;

        calculate_request = {
            "AlgType": algType,
            "Graph": {
                "Nodes": nodes
            },
            "StartNode": select_node
        };
    } else {
        let edges = getEdges(objectToArray(network.nodesHandler.body.edges));
        calculate_request = {
            "AlgType": algType,
            "Graph": {
                "Nodes": nodes,
                "Edges": edges
            }
        };
    }

    let request = new XMLHttpRequest();
    request.open("POST", "calculate", false);
    request.send(JSON.stringify(calculate_request));

    if (request.status === 200) {
        let data = JSON.parse(request.responseText);
        let id = data["RequestId"];
        window.location.replace("http://localhost:5555/result?id=" + id);
    } else {
        throw "Failed request:" + JSON.stringify(calculate_request);
    }

}

function objectToArray(obj) {
    return Object.keys(obj).map(function (key) {
        obj[key].id = key;
        return obj[key];
    });
}


function importNetwork(type) {


    let container = document.getElementById("mynetwork");
    let inputData;

    if (!type) {
        let graph = container.dataset.input;
        let algType = container.dataset.algType;

        if (algType == 3)
            inputData = JSON.parse(graph);
        else
            inputData = JSON.parse(graph).Nodes;
    } else {
        let graph = container.dataset.result;
        inputData = JSON.parse(JSON.parse(graph));
    }


    let _nodes;
    let _edges;
    try {
        if ("Nodes" in inputData) {
            _nodes = getNodeData(inputData.Nodes);
            _edges = getCustomEdgeData(inputData.Edges);
        } else {
            _nodes = getNodeData(inputData);
            _edges = getEdgeData(inputData);
        }
    } catch (e) {
    }

    let data = {
        nodes: _nodes,
        edges: _edges
    };

    network = new vis.Network(container, data, {});
}

function getNodeData(data) {
    let networkNodes = [];

    data.forEach(function (elem, index, array) {
        let nod = {
            id: elem.id,
            label: (parseInt(elem.id) + 1).toString()
        }

        if ("color" in elem) {
            nod.color = elem.color.background
        }

        networkNodes.push(nod);
    });

    return new vis.DataSet(networkNodes);
}

function getNodeById(data, id) {
    for (let n = 0; n < data.length; n++) {
        if (data[n].id == id) {
            // double equals since id can be numeric or string
            return data[n];
        }
    }
    throw "Can not find id '" + id + "' in data";
}

function getEdgeData(data) {
    let networkEdges = [];

    data.forEach(function (node) {
        // add the connection
        node.connections.forEach(function (connId, cIndex, conns) {
            networkEdges.push({ from: node.id, to: connId });
            let cNode = getNodeById(data, connId);

            let elementConnections = cNode.connections;

            // remove the connection from the other node to prevent duplicate connections
            let duplicateIndex = elementConnections.findIndex(function (
                connection
            ) {
                return connection == node.id; // double equals since id can be numeric or string
            });

            if (duplicateIndex != -1) {
                elementConnections.splice(duplicateIndex, 1);
            }
        });
    });

    return new vis.DataSet(networkEdges);
}

function getCustomEdgeData(data) {
    let networkEdges = [];

    data.forEach(function (edge) {
        networkEdges.push({
            from: edge.toId,
            to: edge.fromId,
            label: edge.weight
        });
    });
    return new vis.DataSet(networkEdges);
}

function init() {
    draw();
}