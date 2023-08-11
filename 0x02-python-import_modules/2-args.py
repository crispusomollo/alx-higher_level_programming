#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ln = argv[1:]
    lgt = len(ln)
    print("{:d} {:s}{:s}".
          format(lgt,
                 "arguments" if lgt != 1 else "argument",
                 "." if lgt == 0 else ":"))
    for i, arg in enumerate(ln):
        print("{:d}: {:s}".format(i + 1, arg))
