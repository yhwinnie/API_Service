from flask import Flask, request, url_for, jsonify
import requests
import json


app = Flask(__name__)

info = ""

@app.route('/hello')
def index():
    return 'hello'

@app.route('/pets', methods=['POST'])
def store():
    input_json = request.get_json()

    return jsonify(input_json)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
