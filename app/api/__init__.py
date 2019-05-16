"""
author songjie
"""
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api', static_folder="../../static", template_folder="../../templates")

from app.api import test
from app.api import login
from app.api import user
