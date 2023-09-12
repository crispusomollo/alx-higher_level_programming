#!/usr/bin/python3
"""

writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """writes to a text file and return num charsacters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
