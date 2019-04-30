"""
author songjie
"""
from flask import Flask

from app.errors import register_error


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.config.from_object("config.secure")
    register_blueprint(app)
    register_error(app)
    return app


def register_blueprint(app):
    from app.api import api
    from app.admin import admin
    app.register_blueprint(api)
    app.register_blueprint(admin)
