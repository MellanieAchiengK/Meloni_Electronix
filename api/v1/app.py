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
from models.user import User
from flask_cors import CORS
from hashlib import md5
from api.v1.views.lib.decorator import Melanie_Electronic_login_required


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
    email = request.form['email']
    password = request.form['password']
    
    r = requests.get('http://{}:{}/api/v1/user_registered/{}'.format(
                     api_host, api_port, email))
    user_db = r.json()

    if user_db.get("rep") and user_db.get("user").get("password") == md5(password.encode()).hexdigest():
        return   redirect('/')
    return redirect('/login')


@app.route("/register", methods=['GET'])
def page_regiter_get():
    pays_all = None
    r = requests.get('http://{}:{}/api/v1/country'.format(
                     api_host, api_port))
    if r.status_code == 200:
        pays_all = r.json()
        first_country_id = pays_all[0].get('id')
        r = requests.get('http://{}:{}/api/v1/country/{}/cities'.format(
                     api_host, api_port, first_country_id))
        if r.status_code == 200:
            first_cities_all = r.json()
            #print(first_cities_all)
        else:
            first_cities_all = ""
    else:
        pays_all= ""
    
    context = {
        "msg": "",
        "pays": pays_all,
        "first_cities_all": first_cities_all
    }
    
    return render_template(FRONTEND_TEMPLATE+'register.html', msg=context)


@app.route("/register", methods=['POST'])
def page_regiter_post():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    contry_id =  request.form['contry']
    citie_id = request.form['citie']
    email = request.form['email']

    
    user = User(first_name=first_name, last_name=last_name,
                password=password, city_id=citie_id, email=email)
    user.save()
    return redirect('/succes')
    
@app.route("/succes")
def succes_page():
    return render_template(FRONTEND_TEMPLATE+'success-page.html')

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
@Melanie_Electronic_login_required
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
