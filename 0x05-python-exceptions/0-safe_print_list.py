#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for j in my_list[:x]:
            print("{}".format(j), end="")
            n += 1
        print()
        return n
    except IndexError:
        print()
        return n
