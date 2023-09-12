#!/usr/bin/python3
"""

writes a Python obj to a file using a JSON represenation
"""


def save_to_json_file(my_obj, filename):
    """Writes a Python obj to a file using JSON represenation
    Args:
        my_obj: python object
        filename: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
