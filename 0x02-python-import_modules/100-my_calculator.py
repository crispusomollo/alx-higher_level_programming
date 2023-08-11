#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    oper = argv[2]
    fx = {"+": add, "-": sub, "*": mul, "/": div}
    if oper not in fx:
        print("Unknown operator. AVailable operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d} = {:d}".format(a, oper, b, fx[oper](a, b)))
