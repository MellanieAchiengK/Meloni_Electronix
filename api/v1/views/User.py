#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify, request, abort
from views import app_views
from models.user import User
from models import storage
from hashlib import md5


@app_views.route(
    '/users',
    methods=['GET'],
    strict_slashes=False)
def users_all():
    users = storage.all(User).values()
    liste = []
    for loop in users:
        liste.append(loop.to_dict())
    return liste, 200
    

@app_views.route(
    '/user',
    methods=['POST'],
    strict_slashes=False)
def createUser():
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    user = User(**data)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/user/<user_id>',
                 strict_slashes=False, methods=['DELETE'])
def delUser(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@app_views.route('/user/<user_id>',
                 strict_slashes=False, methods=['PUT'])
def updateUser(user_id):
    data = request.get_json()

    if type(data) is not dict:
        abort(404, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")

    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    black_list = ["id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in black_list:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200


""" @app_views.route('/user/<user_id>',
                 strict_slashes=False, methods=['GET'])
def get_id_user_name(citie_name):
    users = storage.all(User).values()
    id = None
    for loop in users:
        dic = loop.to_dict()
        print(dic['name'])
        if citie_name == dic['name']:
            id = dic['id']
    return jsonify({"id": str(id)}), 200  """

@app_views.route('/user_registered/<user_email>',
                 strict_slashes=False, methods=['GET'])
def user_registered(user_email):
    rep = False
    user_all = storage.all(User).values()
    user_list = []
    user = None
    
    for loop in user_all:
        user_list.append((loop.to_dict().get('email')))
        if loop.to_dict().get('email') == user_email:
            user = loop.to_dict()
    
    
    if user_email in user_list:
        return jsonify({"rep":True, "user": user}), 200

    return jsonify({"rep":False, "user": user}), 200 