#!/usr/bin/python3
"""
Liste of the Category product
"""

from flask import jsonify
from views import app_views
from models import storage
from models.category import Category
from models.product import Product


@app_views.route(
    '/categorie',
    methods=['GET'],
    strict_slashes=False)
def categories_all():
    objet_all = storage.all(Category).values()
    liste_categorie = []
    for loop in objet_all:
        liste_categorie.append(loop.to_dict())
    #print(liste_categorie)

    return jsonify({'categorie':liste_categorie}), 200

@app_views.route(
    '/categorie/<int:pk>',
    methods=['GET'],
    strict_slashes=False)
def liste_article_categories(pk):
    objet_all = storage.all(Product).values()
    listecategorie = []
    for loop in objet_all:
        if loop.to_dict().get("category_id") == pk:
            listecategorie.append(loop.to_dict())
    #print(listecategorie)

    return jsonify({"listecategorie": listecategorie}), 200
