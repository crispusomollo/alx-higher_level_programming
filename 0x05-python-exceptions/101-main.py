#!/usr/bin/python3

safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

res = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(res))

res = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(res))


def print_list(my_list, len):
    j = 0
    while j < len:
        print(my_list[j])
        j += 1
    return len

res = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(res))
