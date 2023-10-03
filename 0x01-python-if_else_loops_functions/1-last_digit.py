#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    i = number % -10
    print(f"Last digit of {number:d} is {i:d} and is less than 6 and not 0")
else:
    i = number % 10

if i > 5:
    print(f"Last digit of {number:d} is {i:d} and is greater than 5")
elif i == 0:
    print(f"Last digit of {number:d} is {i:d} and is 0")
elif 0 < i < 6:
    print(f"Last digit of {number:d} is {i:d} and is less than 6 and not 0")
