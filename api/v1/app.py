#!/usr/bin/python3
"""
Melonie_Electronix implementation
"""

from views import app_views
from flask import Flask, render_template, request
from os import getenv
import requests


BACKOFFICE_TEMPLATE = '/backoffice/templates/'
BACKOFFICE_STATIC = '/backoffice/static/'
FRONTEND_TEMPLATE = '/frontend/templates/'
FRONTEND_STATIC = '/frontend/static/'

api_host = getenv('ME_MYSQL_HOST', default='0.0.0.0')
api_port = getenv('ME_MYSQL_PORT', default=5000)

app = Flask(__name__,
            static_url_path='',
            static_folder='../../web',
            template_folder='../../web')
app.register_blueprint(app_views)


@app.route("/")
def hello_world():
    r = requests.get('http://{}:{}/api/v1/categorie/'.format(
                     api_host, api_port))
    return render_template(FRONTEND_TEMPLATE+'home.html',
                           categorie=r.json().get('categorie'))


@app.route("/presentation")
def presentation():
    return render_template(FRONTEND_TEMPLATE+'presentation.html')


@app.route("/landing")
def landing_page():
    return render_template(FRONTEND_TEMPLATE+'landing_page.html')


@app.route("/article/<string:pk>")
def get_article(pk):
    # return "afficher artcile id = {}".format(pk)
    r = requests.get('http://{}:{}/api/v1/article/{}'.format(
                     api_host, api_port, pk))
    """ print("r=",r.json()["article"]) """
    return render_template(FRONTEND_TEMPLATE+'articleDetail.html',
                           article=r.json()["article"])


@app.route("/categorie/<string:pk>")
def articebycategorie(pk):
    r = requests.get('http://{}:{}/api/v1/categorie/{}'.format(
                     api_host, api_port, pk))
    return render_template(FRONTEND_TEMPLATE+'articleByCategory.html',
                           listecategorie=r.json().get('listecategorie'))


@app.route("/me-admin")
def dashboard():
    return render_template(BACKOFFICE_TEMPLATE+'dashboard.html')


@app.route("/me-admin/products")
def products_index():
    return render_template(BACKOFFICE_TEMPLATE+'products/index.html')


@app.route("/me-admin/categories")
def categories_index():
    return render_template(BACKOFFICE_TEMPLATE+'categories/index.html')


@app.route("/me-admin/categories/create", methods=["GET", "POST"])
def categories_create():
    if request.method == 'POST':
        print('request.form')
    return render_template(BACKOFFICE_TEMPLATE+'categories/create.html')


if __name__ == '__main__':
    app.run(host=api_host, port=int(api_port), threaded=True)
