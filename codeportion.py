from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

# Mock data
containers = {}
items = {}

# HTML Template for the Frontend
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cargo Management System</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
    input, button { padding: 10px; margin: 5px; }
    table { margin: 20px auto; border-collapse: collapse; width: 80%; }
    th, td { border: 1px solid #ddd; padding: 8px; }
    th { background-color: #f4f4f4; }
  </style>
</head>
<body>
  <h1>Cargo Management System</h1>

  <!-- Add Container -->
  <h2>Add Container</h2>
  <form id="addContainerForm">
    <input type="text" id="containerId" placeholder="Container ID" required>
    <input type="text" id="zone" placeholder="Zone" required>
    <input type="number" id="width" placeholder="Width (cm)" required>
    <input type="number" id="depth" placeholder="Depth (cm)" required>
    <input type="number" id="height" placeholder="Height (cm)" required>
    <button type="button" onclick="addContainer()">Add Container</button>
  </form>
  <pre id="containerResult"></pre>

  <!-- Add Item -->
  <h2>Add Item</h2>
  <form id="addItemForm">
    <input type="text" id="itemId" placeholder="Item ID" required>
    <input type="text" id="name" placeholder="Name" required>
    <input type="number" id="width" placeholder="Width (cm)" required>
    <input type="number" id="depth" placeholder="Depth (cm)" required>
    <input type="number" id="height" placeholder="Height (cm)" required>
    <input type="number" id="priority" placeholder="Priority (1-100)" required>
    <input type="date" id="expiryDate" placeholder="Expiry Date (YYYY-MM-DD)">
    <input type="number" id="usageLimit" placeholder="Usage Limit" required>
    <input type="text" id="preferredZone" placeholder="Preferred Zone">
    <button type="button" onclick="addItem()">Add Item</button>
  </form>
  <pre id="itemResult"></pre>

  <!-- Search Item -->
  <h2>Search Item</h2>
  <form id="searchForm">
    <input type="text" id="searchItemId" placeholder="Item ID" required>
    <button type="button" onclick="searchItem()">Search</button>
  </form>
  <pre id="searchResult"></pre>

  <script>
    function addContainer() {
      const container = {
        containerId: document.getElementById('containerId').value,
        zone: document.getElementById('zone').value,
        width: parseFloat(document.getElementById('width').value),
        depth: parseFloat(document.getElementById('depth').value),
        height: parseFloat(document.getElementById('height').value)
      };
      fetch('/api/add/container', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(container)
      })
        .then(response => response.json())
        .then(data => {
          document.getElementById('containerResult').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));
    }

    function addItem() {
      const item = {
        itemId: document.getElementById('itemId').value,
        name: document.getElementById('name').value,
        width: parseFloat(document.getElementById('width').value),
        depth: parseFloat(document.getElementById('depth').value),
        height: parseFloat(document.getElementById('height').value),
        priority: parseInt(document.getElementById('priority').value),
        expiryDate: document.getElementById('expiryDate').value,
        usageLimit: parseInt(document.getElementById('usageLimit').value),
        preferredZone: document.getElementById('preferredZone').value || null
      };
      fetch('/api/add/item', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(item)
      })
        .then(response => response.json())
        .then(data => {
          document.getElementById('itemResult').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));
    }

    function searchItem() {
      const itemId = document.getElementById('searchItemId').value;
      fetch(`/api/search?itemId=${itemId}`)
        .then(response => response.json())
        .then(data => {
          document.getElementById('searchResult').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error:', error));
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/api/add/container", methods=["POST"])
def add_container():
    data = request.get_json()
    container_id = data.get("containerId")
    if container_id in containers:
        return jsonify({"success": False, "message": "Container already exists"}), 400
    containers[container_id] = {
        "zone": data.get("zone"),
        "width": data.get("width"),
        "depth": data.get("depth"),
        "height": data.get("height"),
        "items": []
    }
    return jsonify({"success": True, "message": "Container added successfully"})

@app.route("/api/add/item", methods=["POST"])
def add_item():
    data = request.get_json()
    item_id = data.get("itemId")
    if item_id in items:
        return jsonify({"success": False, "message": "Item already exists"}), 400
    items[item_id] = {
        "name": data.get("name"),
        "width": data.get("width"),
        "depth": data.get("depth"),
        "height": data.get("height"),
        "priority": data.get("priority"),
        "expiryDate": data.get("expiryDate"),
        "usageLimit": data.get("usageLimit"),
        "preferredZone": data.get("preferredZone"),
        "containerId": None,
        "position": None
    }
    return jsonify({"success": True, "message": "Item added successfully"})

@app.route("/api/search", methods=["GET"])
def search_item():
    item_id = request.args.get("itemId")
    if item_id not in items:
        return jsonify({"success": False, "found": False, "message": "Item not found"}), 404
    item = items[item_id]
    return jsonify({
        "success": True,
        "found": True,
        "item": item
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
