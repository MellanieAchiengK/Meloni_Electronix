#!/usr/bin/python3
"""
Melonie_Electronix implementation
"""

from views import app_views
from flask import Flask, render_template, request, redirect
from os import getenv
import requests
from models import storage
from models.country import Country
from models.city import City
from flask_cors import CORS


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
CORS(app)



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
    #return "hello landing page"
    return render_template(FRONTEND_TEMPLATE+'landing_page.html')


@app.route("/login", methods=['GET'])
def page_connexion_get():
    return render_template(FRONTEND_TEMPLATE+'connexion.html')


@app.route("/login", methods=['POST'])
def page_connexion_post():
    msg = 'erreur'
    verite = True
    username = request.form['username']
    password = request.form['password']
    if verite:
        return   redirect('/')
    return render_template(FRONTEND_TEMPLATE+'connexion.html', msg='')


@app.route("/register", methods=['GET'])
def page_regiter_get():
    # recuperer la liste de tous les paysù
    pays_all = None
    r = requests.get('http://{}:{}/api/v1/country'.format(
                     api_host, api_port))
    if r.status_code == 200:
        pays_all = r.json()
    context = {
        "msg": "Une erruer",
        "pays": pays_all
    }
    
    return render_template(FRONTEND_TEMPLATE+'register.html', msg=context)


@app.route("/register", methods=['POST'])
def page_regiter_post():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    contry =  request.form['contry']
    citie = request.form['citie']
    email = request.form['email']

    print("contry= {} citie={}".format(contry, citie))
     
    return "contry_id"


@app.route("/article/<int:pk>")
def get_article(pk):
    # return "afficher artcile id = {}".format(pk)
    r = requests.get('http://{}:{}/api/v1/article/{}'.format(
                     api_host, api_port, pk))
    """ print("r=",r.json()["article"]) """
    return render_template(FRONTEND_TEMPLATE+'articleDetail.html',
                           article=r.json()["article"])


@app.route("/categorie/<int:pk>")
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
    app.run(host=api_host, port=int(api_port), threaded=True, debug=True)
