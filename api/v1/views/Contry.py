#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify, request, abort
from views import app_views
from models.country import Country
from models import storage


@app_views.route(
    '/country',
    methods=['GET'],
    strict_slashes=False)
def contry_all():
    countries = storage.all(Country).values()
    liste = []
    for loop in countries:
        liste.append(loop.to_dict())
    return liste, 200
    

@app_views.route(
    '/country',
    methods=['POST'],
    strict_slashes=False)
def createContry():
    contries = storage.all(Country)
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    contry = Country(**data)
    storage.new(contry)
    storage.save()
    return jsonify(contry.to_dict()), 201


@app_views.route('/country/<country_id>',
                 strict_slashes=False, methods=['DELETE'])
def delCounty(country_id):
    state = storage.get(Country, country_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200

@app_views.route('/country/<country_id>',
                 strict_slashes=False, methods=['PUT'])
def updateContry(country_id):
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")

    state = storage.get(Country, country_id)
    if state is None:
        abort(404)
    black_list = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in black_list:
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200


@app_views.route('/country/<country_name>',
                 strict_slashes=False, methods=['GET'])
def get_id_country_name(country_name):
    countries = storage.all(Country).values()
    id = None
    for loop in countries:
        dic = loop.to_dict()
        print(dic['name'])
        if country_name == dic['name']:
            id = dic['id']
    return jsonify({"id": id}), 200 