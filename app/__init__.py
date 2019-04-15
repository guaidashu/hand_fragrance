"""
author songjie
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.settings")
    app.config.from_object("config.secure")
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.api import api
    app.register_blueprint(api)
