"""
author songjie
"""
from flask import Flask

from app.errors import register_error

from app.models.base import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.config.from_object("config.secure")
    register_blueprint(app)
    register_error(app)
    db.init_app(app)
    # db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.api import api
    from app.admin import admin
    app.register_blueprint(api)
    app.register_blueprint(admin)
