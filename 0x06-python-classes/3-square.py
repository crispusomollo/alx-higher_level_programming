#!/usr/bin/python3
"""Square that defines a square based on 2-square.py"""


class Square:
    """Private instance attribute size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the squared value"""
        return self.__size ** 2
