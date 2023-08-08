#!/usr/bin/python3
import random
number = random.randint(-10,10)

if number == 0:
    print(f"{number :d} is a zero")
elif number > 0:
    print(f"{number :d} is a positive number")
else:
    print(f"{number :d} is a negative number")
