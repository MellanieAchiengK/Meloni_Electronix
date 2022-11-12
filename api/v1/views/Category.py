#!/usr/bin/python3
"""
Liste of the Category product
"""

from flask import jsonify
from views import app_views
from models import storage
from models.category import Category

categorie = [
    {
        "id":"1",
        "src":"https://www.shutterstock.com/image-photo/document-management-system-dms-being-600w-1874749972.jpg",
        "title":"Oridnateurs"
    },
    {
        "id":"2",
        "src":"https://www.shutterstock.com/image-photo/smartphone-portable-game-consoles-ebook-600w-1827624617.jpg",
        "title":"Smart Phone"
    },
    {
        "id":"3",
        "src":"https://www.shutterstock.com/image-vector/semiconductor-electronic-circuit-board-isometric-600w-565557181.jpg",
        "title":"Composant electronique"
    },
    {
        "id":"4",
        "src":"https://farm3.staticflickr.com/2403/2127291233_899c16de27_d.jpg",
        "title":"Flickr picture by sea turtle"
    }
]

@app_views.route(
    '/categorie',
    methods=['GET'],
    strict_slashes=False)
def categories_all():
    return jsonify({'categorie':categorie}), 200

@app_views.route(
    '/categorie/<int:pk>',
    methods=['GET'],
    strict_slashes=False)
def liste_article_categories(pk):
    listecategorie = categorie
    return jsonify({"listecategorie":listecategorie}), 200