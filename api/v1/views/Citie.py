#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify, request, abort
from views import app_views
from models.city import City
from models import storage


@app_views.route(
    '/cities',
    methods=['GET'],
    strict_slashes=False)
def city_all():
    countries = storage.all(City).values()
    liste = []
    for loop in countries:
        liste.append(loop.to_dict())
    return liste, 200
    

@app_views.route(
    '/cities',
    methods=['POST'],
    strict_slashes=False)
def createCity():
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    citie = City(**data)
    storage.new(citie)
    storage.save()
    return jsonify(citie.to_dict()), 201


@app_views.route('/citie/<citie_id>',
                 strict_slashes=False, methods=['DELETE'])
def delCity(citie_id):
    citie = storage.get(City, citie_id)
    if citie is None:
        abort(404)
    storage.delete(citie)
    storage.save()
    return jsonify({}), 200

@app_views.route('/citie/<citie_id>',
                 strict_slashes=False, methods=['PUT'])
def updateCity(citie_id):
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")

    citie = storage.get(City, citie_id)
    if citie is None:
        abort(404)
    black_list = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in black_list:
            setattr(citie, key, value)
    storage.save()
    return jsonify(citie.to_dict()), 200


@app_views.route('/citie/<citie_name>',
                 strict_slashes=False, methods=['GET'])
def get_id_city_name(citie_name):
    cities = storage.all(City).values()
    id = None
    for loop in cities:
        dic = loop.to_dict()
        print(dic['name'])
        if citie_name == dic['name']:
            id = dic['id']
    return jsonify({"id": id}), 200 