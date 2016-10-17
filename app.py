from flask import Flask, request, url_for, jsonify
import requests
import json


app = Flask(__name__)


pets = []

@app.route('/hello')
def index():
    return 'hello'


# curl -H "Content-Type: application/json" -X POST -d '{"name":"Pluto","age":"3","species":"dog"}' http://0.0.0.0:5000/pets
@app.route('/pets', methods=["POST"])
def post_pets():
    json_dict = request.get_json()
    try:
        name = json_dict['name']
        age = json_dict['age']
        species = json_dict['species']

        data = {"name": str(name), "age": str(age), "species": str(species)}

        for pet in pets:
            if pet["name"] == str(name):
                data = {"HTTP status": "409", "message": "Pet name already exists"}
                return jsonify(data)
        pets.append(data)
        return jsonify(data)
    except KeyError as error:
        print(error.message + "key not find")
        return jsonify({"HTTP status": "400", "message": error.message + " key not find"})


@app.route('/pets', methods=["GET"])
def get_pets():
    return jsonify(pets)

@app.route('/pets/<name>', methods=["PUT"])
def put_request(name):
    check_pet_exist(name)
    json_dict = request.get_json()
    for pet in pets:
        if pet["name"] == name:
            try:
                if pet["name"] == str(name):
                    pet["name"] = json_dict["name"]
                    pet["age"] = json_dict["age"]
                    pet["species"] = json_dict["species"]
                    return jsonify(pets)
                    break
            except:
                return jsonify({"HTTP status": "400", "message": "ERROR"})

    return jsonify({"HTTP status": "400", "message": "Key: " + name + " does not exist"})


@app.route('/pets/<name>', methods=["DELETE"])
def delete_pet(name):
    #check_pet_exist(name)
    json_dict = request.get_json()
    for pet in pets:
        if pet["name"] == str(name):
            try:
                pets.pop(pet)
                break
            except:
                return jsonify({"HTTP status": "400", "message": "Key: " + name + " does not exist"})

    return jsonify(pets)


@app.route('/pets/<name>', methods=["GET"])
def check_pet_exist(name):
    for pet in pets:
        if pet["name"] == name:
            return jsonify(pet)
    return jsonify({"HTTP status": "400", "message": "Key: " + name + " does not exist"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
