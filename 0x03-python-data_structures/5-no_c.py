#!/usr/bin/python3
def no_c(my_string):
    second = f""
    for x in my_string:
        if x != 'c' and x != 'C':
            second += f"{x}"
    return second
