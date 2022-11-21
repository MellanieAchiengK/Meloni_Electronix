#!/usr/bin/python3
"""
Melonie_Electronix implementation
"""

from views import app_views
from flask import Flask, render_template, request, redirect, flash
from os import getenv, path
import requests
from werkzeug.utils import secure_filename
from models import db
from models.category import Category


BACKOFFICE_TEMPLATE = '/backoffice/templates/'
BACKOFFICE_STATIC = '/backoffice/static/'
FRONTEND_TEMPLATE = '/frontend/templates/'
FRONTEND_STATIC = '/frontend/static/'
UPLOADS_PATH = 'web'+BACKOFFICE_STATIC+'uploads/'
# Allowed image extensions
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

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
    return render_template(FRONTEND_TEMPLATE+'register.html', msg='')


@app.route("/register", methods=['POST'])
def page_regiter_post():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    contry =  request.form['contry']
    citie = request.form['citie']
    email = request.form['email']
    return "{} {} et {} enrigistré avec succes // {} habite a {} dans {}".format(username, password, email, confirm_password, contry, citie)


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
    """display table with the categories listed in alphabetical order"""
    categories = sorted(list(db.Db().all(Category).values()),
                        key=lambda x: x.name)
    return render_template(BACKOFFICE_TEMPLATE+'categories/index.html',
                           categories=categories)


@app.route("/me-admin/categories/create", methods=["GET", "POST"])
def categories_create():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            image_path = path.join(BACKOFFICE_STATIC,
                                   'uploads/category', filename)
            file.save(path.join(UPLOADS_PATH, 'category', filename))
            name = request.form.get('name')
            category = Category(name=name, image=image_path)
            category.save()
        else:
            flash('Allowed image types are: png, jpg, jpeg, gif')
        return render_template(BACKOFFICE_TEMPLATE+'categories/index.html')
    else:
        return render_template(BACKOFFICE_TEMPLATE+'categories/create.html')


if __name__ == '__main__':
    app.run(host=api_host, port=int(api_port), threaded=True, debug=True)
