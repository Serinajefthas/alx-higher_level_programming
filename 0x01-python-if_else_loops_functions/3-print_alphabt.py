#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) == 'p' or chr(i) == 'e':
        i += 1
    else:
        print("{:c}".format(i), end="")
