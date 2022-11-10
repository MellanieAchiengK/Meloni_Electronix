#!/usr/bin/python3
"""
Initializes views module
"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

#from backend.v1.views import *
#from backend.v1.views.Produit import *
from views import *
from views.Produit import *
from views.Category import *