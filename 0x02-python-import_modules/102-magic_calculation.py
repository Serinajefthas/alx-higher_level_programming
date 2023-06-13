#!/usr/bin/python3
from calculator_1 import add, sub
def magic_calculation(a, b):
    if a < b:
        x = add(a, b)
        for i in range(4, 6):
            x = add(x, i)
        return x
    else:
        y = sub(a, b)
        return y
