#!/usr/bin/python3
def print_tebahpla():
    for i in range(122, 96, -1):
        print("{:c}".format(i if i % 2 == 0 else i - 32), end="")
