#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify
from views import app_views


@app_views.route(
    '/article',
    methods=['GET'],
    strict_slashes=False)
def article_all():
    article = ['accessoire','ordinateur','chargeur','ecouteur','baterie']
    return jsonify({'article':article})

@app_views.route(
    '/article/<int:pk>',
    strict_slashes=False)
def get_article(pk):
    
    return jsonify({'pk':pk})