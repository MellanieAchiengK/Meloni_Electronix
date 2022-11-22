#!/usr/bin/python3
"""
Liste of the produit
"""

from flask import jsonify
from views import app_views
from models import storage
from models.product import Product
article1={
    "title":"Ordinateur",
    "src":"https://m.media-amazon.com/images/I/61aTywrhyBS._AC_SX569_.jpg",
    "description":"À propos de cet article CHUWI ordinateur portable Herobook pro équipé de Windows 11 OS pré-installé et du processeur Celeron N4020, avec cache de 4M, la fréquence de 1,1 GHz jusqu'à 2,8 GHz, construit en GPU Intel UHD Graphics 600, prend en charge le décodage vidéo fluide 4kAvec 8 Go DDR4 et 256 Go SSD, cet ordinateur portable rend le traitement multitâche plus efficace, la lecture et l’écriture plus vite, les Apps peuvent être exécutées avec efficacité, Micro SD prend en charge l'extension jusqu'à 128 Go, SSD max jusqu'à 1 To Ce pc portable avec écran IPS anti-éblouissement de 14,1 pouces vous offre une vue plus large, une image plus claire et vive, une résolution ultra haute de 1920 x 1080, en outre, le mode nuit aidant à réduire la fatigue visuelle Chromebook avec clavier pleine taille, livré avec des autocollants en silicone en espagnol. Batterie de 38 Wh qui permet une utilisation utile de plus de 9 heures par jour. Multi-interfaces : Micro SD, USB 2.0, USB 3.0, Mini HD, M.2, PD de charge rapide pour connectivité sans barrières CHUWI Offre un service de garantie gratuit pendant un an. Si vous avez des problèmes, n'hésitez pas à nous contacter directement dans la page de commande, nous vous répondrons dans les 24 heures et fournirons une assistance technique"
}

article2={
    "title":"iphone",
    "src":"https://www.apple.com/newsroom/images/product/iphone/standard/apple_iphone-12-spring21_purple_04202021_big.jpg.large.jpg",
    "description":"une descrpittion plus complet de l'article"
}

article = [article1,article2]

@app_views.route(
    '/article',
    methods=['GET'],
    strict_slashes=False)
def article_all():
    return jsonify({'article':article})

@app_views.route(
    '/article/<int:pk>',
    strict_slashes=False)
def get_article(pk):
    object = storage.get(Product, pk)
    article = object.to_dict()
    print(article)
    return jsonify({'article':article})