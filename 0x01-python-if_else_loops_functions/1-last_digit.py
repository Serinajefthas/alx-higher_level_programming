#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(number) % 10
if num > 5:
    print("Last digit of " + str(number)+ " is "+ str(num)+
    " and is greater than 5")
elif num == 0:
    print("Last digit of " + str(number)+ " is "+ str(num)+
            " and is 0")
else:
    print("Last digit of " + str(number)+ " is "+ str(num)+
    " and is less than 6 and not 0")
