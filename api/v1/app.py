#!/usr/bin/python3
"""
Melonie_Electronix implementation
"""

from views import app_views
from flask import Flask, render_template, request, redirect, flash, url_for
from os import getenv, path
import requests
from werkzeug.utils import secure_filename
from models import storage
from models.category import Category
from models.product import Product
from models.country import Country
from models.city import City
from flask_cors import CORS


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
app.config['SECRET_KEY'] = 'tmz5d7kioaayiWmW7-zM8g'
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
        first_country_id = pays_all[0].get('id')
        r = requests.get('http://{}:{}/api/v1/country/{}/cities'.format(
                     api_host, api_port, first_country_id))
        if r.status_code == 200:
            first_cities_all = r.json()
            # print(first_cities_all)
        else:
            first_cities_all = ""
    else:
        pays_all = ""

    context = {
        "msg": "Une erruer",
        "pays": pays_all,
        "first_cities_all": first_cities_all
    }

    return render_template(FRONTEND_TEMPLATE+'register.html', msg=context)


@app.route("/register", methods=['POST'])
def page_regiter_post():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    contry = request.form['contry']
    citie = request.form['citie']
    email = request.form['email']

    print("contry= {} citie={}".format(contry, citie))

    return "contry_id = {} citie_id= {}".format(contry, citie)


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
    """Returns admin dashboard"""
    product_count = storage.count(Product)
    category_count = storage.count(Category)
    return render_template(BACKOFFICE_TEMPLATE+'dashboard.html',
                           product_count=product_count,
                           category_count=category_count)


@app.route("/me-admin/products")
def product_index():
    """Returns product list"""
    products = storage.all(Product).values()
    return render_template(BACKOFFICE_TEMPLATE+'products/index.html',
                           products=products)


@app.route("/me-admin/products/create", methods=["GET", "POST"])
def product_create():
    """Returns create product page or creates a product"""
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
                                   'uploads/product', filename)
            file.save(path.join(UPLOADS_PATH, 'product', filename))
            name = request.form.get('name')
            category_id = request.form.get('category')
            cost_price = request.form.get('cost_price')
            selling_price = request.form.get('selling_price')
            quantity = request.form.get('quantity')
            descr = request.form.get('description')
            user_id = 1
            product = Product(name=name,
                              selling_price=selling_price,
                              cost_price=cost_price,
                              description=descr,
                              quantity=quantity,
                              category_id=category_id,
                              user_id=user_id,
                              image=image_path)
            product.save()
            flash('Product saved succesfully')
            return redirect(url_for('product_index'))
        else:
            flash('Allowed image types are: png, jpg, jpeg, gif')
    else:
        categories = sorted(list(storage.all(Category).values()),
                            key=lambda x: x.name)
        return render_template(BACKOFFICE_TEMPLATE+'products/create.html',
                               categories=categories)


@app.route("/me-admin/categories")
def category_index():
    """display table with the categories listed in alphabetical order"""
    categories = storage.all(Category).values()
    return render_template(BACKOFFICE_TEMPLATE+'categories/index.html',
                           categories=categories)


@app.route("/me-admin/categories/create", methods=["GET", "POST"])
def category_create():
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
            flash('Category saved succesfully')
            return redirect(url_for('category_index'))
        else:
            flash('Allowed image types are: png, jpg, jpeg, gif')
    else:
        return render_template(BACKOFFICE_TEMPLATE+'categories/create.html')


if __name__ == '__main__':
    app.run(host=api_host, port=int(api_port), threaded=True, debug=True)
