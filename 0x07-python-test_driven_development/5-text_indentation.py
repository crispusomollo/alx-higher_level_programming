#!/usr/bin/python3
"""
Module 5-text_indentation
Has a method that prints text with 2 new lines after each ".", "?", ":"
Takes in a string
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    listlines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(listlines)
    print(revised, end="")
