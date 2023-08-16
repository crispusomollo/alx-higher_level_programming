#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return[(my_list[x] if my_list[x] != search else replace)
           for x in range(len(my_list)) ]
