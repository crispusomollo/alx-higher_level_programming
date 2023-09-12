#!/usr/bin/python3
"""

creates a Python obj from JSON file
"""


def load_from_json_file(filename):
    """Creates a Python obj from a JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)