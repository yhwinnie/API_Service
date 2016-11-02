from flask import Flask, request, url_for, jsonify
import requests
import json
import uuid

app = Flask(__name__)


tasks = []

@app.route('/tasks')
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks', methods=["POST"])
def post_tasks():
    json_dict = request.get_json()

    try:
        id_generated = uuid.uuid4()
        text_input = json_dict["text"]
        task = {"id": str(id_generated), "text": str(text_input)}
        tasks.append(task)
        return jsonify(tasks)
    except:
        return jsonify("ERROR")


@app.route('/tasks/<id>')
def get_tasks_with_id(id):
    for task in tasks:
        if task[id] == id:
            return jsonify(task)


@app.route('/tasks/<id>', methods=["DELETE"])
def delete_tasks_with_id(id):
    for task in tasks:
        if task[id] == id:
            tasks.pop(task)
            break

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
