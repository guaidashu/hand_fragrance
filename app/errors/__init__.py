"""
author songjie
"""


def register_error(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return 'This page does not exist', 404

    @app.errorhandler(500)
    def page_error(error):
        return 'This page error', 500
