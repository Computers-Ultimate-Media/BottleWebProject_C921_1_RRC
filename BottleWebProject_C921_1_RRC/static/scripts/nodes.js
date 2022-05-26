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
        layout: {randomSeed: seed},
        locale: "ru",
        manipulation: {
            addNode: function (data, callback) {
                // filling in the popup DOM elements
                document.getElementById("node-operation").innerText = "Добавьте узел";
                editNode(data, clearNodePopUp, callback);
            },
            editNode: function (data, callback) {
                // filling in the popup DOM elements
                document.getElementById("node-operation").innerText = "Изменить узел";
                editNode(data, cancelNodeEdit, callback);
            },
            addEdge: function (data, callback) {
                if (data.from === data.to) {
                    let r = confirm("Вы действительно хотите соединить узел с самим собой?");
                    if (r !== true) {
                        callback(null);
                        return;
                    }
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


function editNode(data, cancelAction, callback) {
    document.getElementById("node-id").value = counter_nodes;
    document.getElementById("node-saveButton").onclick = saveNodeData.bind(
        this,
        data,
        callback
    );
    document.getElementById("node-cancelButton").onclick =
        cancelAction.bind(this, callback);
    document.getElementById("node-popUp").style.display = "block";
}

// Callback passed as parameter is ignored
function clearNodePopUp() {
    document.getElementById("node-saveButton").onclick = null;
    document.getElementById("node-cancelButton").onclick = null;
    document.getElementById("node-popUp").style.display = "none";
}

function cancelNodeEdit(callback) {
    clearNodePopUp();
    callback(null);
}

function removeOptions() {
    const select = document.getElementById("first_node");
    let opt_len = select.options.length - 1;
    for (let i = opt_len; i >= 0; i--) {
        select.remove(i);
    }
}

function addNewNodeInList() {
    const select = document.getElementById("first_node");
    removeOptions();

    for (let index in nodes) {
        select.options[select.options.length] = new Option(nodes[index], index);
    }
}

function saveNodeData(data, callback) {
    nodes.push(counter_nodes);
    counter_nodes += 1;
    addNewNodeInList();

    data.label = document.getElementById("node-id").value;
    clearNodePopUp();
    callback(data);
}

function editEdgeWithoutDrag(data, callback) {
    // filling in the popup DOM elements
    document.getElementById("edge-label").value = data.label;
    document.getElementById("edge-saveButton").onclick = saveEdgeData.bind(
        this,
        data,
        callback
    );
    document.getElementById("edge-cancelButton").onclick =
        cancelEdgeEdit.bind(this, callback);
    document.getElementById("edge-popUp").style.display = "block";
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

function exportNetwork() {
    let nodes = objectToArray(network.getPositions());
    nodes.forEach(addConnections);

    let request = new XMLHttpRequest();
    request.open("POST", "check_result", false);
    request.send(JSON.stringify(nodes, undefined, 2));
}

function objectToArray(obj) {
    return Object.keys(obj).map(function (key) {
        obj[key].id = key;
        return obj[key];
    });
}

function init() {
    draw();
}