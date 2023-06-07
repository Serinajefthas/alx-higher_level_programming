#!/usr/bin/python3
for i in range(00, 100):
    if i < 10:
        print("0" + str(i), end = ", ")
    elif i == 99:
        print(i)
    else:
        print(i, end = ", ")
