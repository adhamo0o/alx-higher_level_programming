#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is")
if number[:-1] > 5:
    print(f"and is greater than 5")
elif number[:-1] == 0:
    print(f"and is 0")
else number[:-1] < 6 and != 0:
    print(f"and is less than 6 and not 0")
