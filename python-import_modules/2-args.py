#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    count = len(args) - 1

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    for i in range(1, len(args)):
        print("{}: {}".format(i, args[i]))
