#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
response = f"null"
last_digit = number % 10 if number > 0 else number % -10
if last_digit != 0:
    response = f"and is less than 5" if last_digit > 5 else f"and is less than 6 and not 0"
else:
    response = "and is 0"

print(f"Last digit of {number :d} is {last_digit :d} {response}")

