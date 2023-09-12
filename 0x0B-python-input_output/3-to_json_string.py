#!/usr/bin/python3
"""

returns a JSON representation of obj (string)
"""


def to_json_string(my_obj):
    """Returns a JSON representation of obj (string)
    Args:
        my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)
