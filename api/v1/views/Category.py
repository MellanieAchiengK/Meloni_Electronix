#!/usr/bin/python3
"""
Liste of the Category product
"""

from flask import jsonify
from views import app_views
from models import storage
from models.category import Category
from models.product import Product

categorie = [
    {
        "id":"1",
        "image":"https://www.shutterstock.com/image-photo/document-management-system-dms-being-600w-1874749972.jpg",
        "name":"Oridnateurs"
    },
    {
        "id":"2",
        "image":"https://www.shutterstock.com/image-photo/smartphone-portable-game-consoles-ebook-600w-1827624617.jpg",
        "name":"Smart Phone"
    },
    {
        "id":"3",
        "image":"https://www.shutterstock.com/image-vector/semiconductor-electronic-circuit-board-isometric-600w-565557181.jpg",
        "name":"Composant electronique"
    },
    {
        "id":"4",
        "image":"https://farm3.staticflickr.com/2403/2127291233_899c16de27_d.jpg",
        "name":"Flickr picture by sea turtle"
    }
]

@app_views.route(
    '/categorie',
    methods=['GET'],
    strict_slashes=False)
def categories_all():
    objet_all = storage.all(Category).values()
    liste_categorie = []
    for loop in objet_all:
        liste_categorie.append(loop.to_dict())
    print(liste_categorie)

    return jsonify({'categorie':liste_categorie}), 200

@app_views.route(
    '/categorie/<int:pk>',
    methods=['GET'],
    strict_slashes=False)
def liste_article_categories(pk):
    #listecategorie = categorie
    objet_all = storage.all(Product).values()
    listecategorie = []
    for loop in objet_all:
        if loop.to_dict().get("category_id") == pk:
            listecategorie.append(loop.to_dict())
    print(listecategorie)

    return jsonify({"listecategorie": listecategorie}), 200