from flask import Flask, request, jsonify

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = {"id": len(tasks) + 1, "task": data["task"]}
    tasks.append(task)
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = data["task"]
            return jsonify(task)
    return jsonify({"error": "Not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
