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
from models.user import User
from flask_cors import CORS
from hashlib import md5
from api.v1.views.lib.decorator import Melanie_Electronic_login_required


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
            # print(first_cities_all)
        else:
            first_cities_all = ""
    else:
        pays_all = ""

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

    if password != confirm_password:
        flash('No image selected for uploading')
        return redirect(request.url)
    
    print("apres contrainte password")
    
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
