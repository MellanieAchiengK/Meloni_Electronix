#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify
from views import app_views


@app_views.route(
    '/produit',
    methods=['GET'],
    strict_slashes=False)
def get_Produit():
    produit = ['accessoire','ordinateur','chargeur','ecouteur','baterie']
    return jsonify({'produit':produit})