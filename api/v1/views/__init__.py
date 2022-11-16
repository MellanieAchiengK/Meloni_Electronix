#!/usr/bin/python3
"""
Initializes views module
"""

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views import *
from api.v1.views.Article import *
from api.v1.views.Category import *
from api.v1.views.Contry import *
from api.v1.views.Citie import *