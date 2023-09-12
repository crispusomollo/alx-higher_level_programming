#!/usr/bin/python3
"""

returns a python data structure from a JSON string
"""


def from_json_string(my_str):
    """Returns a python data structure from a JSON string
    Args:
        my_str: a json string representation
    Return:
        a python object
    """
    import json

    return json.loads(my_str)
