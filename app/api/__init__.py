"""
author songjie
"""
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api', static_folder="../../static", template_folder="../../templates")
from app.api import test
from app.api import user
from app.api import book
from app.api import gift
from app.api import wish
