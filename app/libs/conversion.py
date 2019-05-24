"""
author songjie
"""


class Conversion(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    @staticmethod
    def combined_multi_dict_to_dict(data):
        result = dict()
        for k, v in data.items():
            result[k] = v
        return result
