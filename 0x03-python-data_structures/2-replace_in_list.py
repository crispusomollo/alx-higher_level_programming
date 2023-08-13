#!/usr/bin/python
def replace_in_list(my_list, idx, element):
    if idx < len(my_list) and idx > - 1:
        my_list[idx] = element
        return my_list
    return my_list
