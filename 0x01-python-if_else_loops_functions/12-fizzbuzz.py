#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        j = i % 5 == 0
        k = i % 3 == 0
        l = j and k
        res = f"FizzBuzz" if l else f"Buzz" if j \
            else f"Fizz" if k else f"{i:d}"
        print(res, end=" ")
