#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify
from views import app_views



@app_views.route(
    '/contry',
    methods=['GET'],
    strict_slashes=False)
def contry_all():
    return jsonify({'contry':"contry"})

