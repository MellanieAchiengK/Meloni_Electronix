#!/usr/bin/python3
"""
Melonie_Electronix implementation
"""

from flask import Flask, render_template
from views import app_views
from os import getenv


app = Flask(__name__,
            static_folder='../../frontend/static',
            template_folder='../../frontend/templates')
app.register_blueprint(app_views)


@app.route("/")
def hello_world():
    return render_template('acceuil.html')


@app.route("/presentation")
def presentation():
    return render_template('presentation.html')


@app.route("/landing")
def landing_page():
    return render_template('landing_page.html')


@app.route("/categorie/<int:pk>")
def articebycategorie(pk):
    return render_template('articleByCategorie.html', id=pk)


if __name__ == '__main__':
    api_host = getenv('MELONIE_ELECTRONIX_HOST', default='0.0.0.0')
    api_port = getenv('MELONIE_ELECTRONIX_PORT', default=5000)
    app.run(host=api_host, port=int(api_port), threaded=True)
