#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dgt = number % 10
if last_dgt > 5:
    print(f"Last digit of {number:d} is {last_dgt:d} and is greater than 5")
elif last_dgt == 0:
    print(f"Last digit of {number:d} is {last_dgt:d} and is 0")
elif 0 < last_dgt < 6:
    print(f"Last digit of {number:d} is {last_dgt:d} and is less than 6 and not 0")
