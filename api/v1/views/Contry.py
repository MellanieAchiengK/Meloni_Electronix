#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify, request, abort
from views import app_views
from models.country import Country
from models import storage


@app_views.route(
    '/contry',
    methods=['GET'],
    strict_slashes=False)
def contry_all():
    countries = storage.all(Country).values()
    liste = []
    for loop in countries:
        liste.append(loop.to_dict())
    return liste, 200
    

@app_views.route(
    '/contry',
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


@app_views.route('/contry/<state_id>',
                 strict_slashes=False, methods=['DELETE'])
def delSate(state_id):
    state = storage.get(Country, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200