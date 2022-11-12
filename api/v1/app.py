#!/usr/bin/python3
"""
Melonie_Electronix implementation
"""

from flask import Flask, render_template
from views import app_views
from os import getenv
import requests


BACKOFFICE_TEMPLATE='/backoffice/templates/'
BACKOFFICE_STATIC='/backoffice/static/'
FRONTEND_TEMPLATE='/frontend/templates/'
FRONTEND_STATIC='/frontend/static/'

api_host = getenv('ME_MYSQL_HOST', default='0.0.0.0')
api_port = getenv('ME_MYSQL_PORT', default=5000)

app = Flask(__name__,
            static_folder='../../web',
            template_folder='../../web')
app.register_blueprint(app_views)


@app.route("/")
def hello_world():
    return render_template(FRONTEND_TEMPLATE+'home.html')


@app.route("/presentation")
def presentation():
    return render_template(FRONTEND_TEMPLATE+'presentation.html')


@app.route("/landing")
def landing_page():
    return render_template(FRONTEND_TEMPLATE+'landing_page.html')


@app.route("/article/<int:pk>")
def get_article(pk):
    return "afficher artcile id = {}".format(pk)

@app.route("/categorie/<int:pk>")
def articebycategorie(pk):
    r = requests.get('http://{}:{}/api/v1/categorie/{}'.format(
                     api_host, api_port, pk))
    print("hello debogue:", r.json())
    return render_template(FRONTEND_TEMPLATE+'articleByCategory.html',
                            listecategorie=r.json().get('listecategorie'))


if __name__ == '__main__':
    app.run(host=api_host, port=int(api_port), threaded=True)
