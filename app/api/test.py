"""
author songjie
"""
from app.api import api


@api.route('/web')
def mytest():
    return 'test'
