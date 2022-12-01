#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for s in argv[1:]:
        total += int(s)
    print("{:d}".format(total))
