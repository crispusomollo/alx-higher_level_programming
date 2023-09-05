#!/usr/bin/python3
"""
Locked class
"""


class LockedClass:
    """
    Prevents a user from creating a new instace
    dynamically
    """

    __slots__ = "first_name"
