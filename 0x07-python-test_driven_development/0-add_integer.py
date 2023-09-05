#!/usr/bin/python3
"""
Module 0-add_integer
Contains a method that returns a sum of two integers
Accepts two integers and casts them to int before adding
"""


def add_integer(a, b=98):
    """
    Returns the value of a + b as int
    """


    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
