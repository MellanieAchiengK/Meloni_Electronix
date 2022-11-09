#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import render_template
from views import app_views


@app_views.route(
    '/produit',
    methods=['GET'],
    strict_slashes=False)
def get_Produit():
    return render_template('hello.html')